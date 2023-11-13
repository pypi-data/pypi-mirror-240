#!/usr/bin/python
## -*- coding: utf-8 -*-  

import os
import sys
import shlex
from subprocess import PIPE, Popen, STDOUT
import subprocess
import json
import time
import signal
import re
import argparse

py_version = sys.version[0] 
if py_version == "3":
    import importlib
    importlib.reload(sys)
elif py_version == "2":
    reload(sys)
    sys.setdefaultencoding('utf8')

def py_version():
    return sys.version[0] 

def runcmd(cmd):
    P = Popen(cmd, shell=True, stdout=PIPE,stderr=STDOUT)
    p = P.stdout.readlines()
    py_ver = py_version()
    if p:
        if py_ver == '2':
            return p[0].strip('\r\n')
        elif py_ver == '3':
            return p[0].decode('utf-8').strip('\r\n')
    else:
        return None

HOME_PATH = runcmd('echo ${HOME}')
global base_dir
base_dir=os.path.dirname(__file__)

def check_root():
    global HOME_PATH
    if HOME_PATH != '/root':
        print("Error: please perform the operation with root privileges")
        sys.exit(1)

def run_cmd(cmd):
  if isinstance(cmd, str):
    cmd = shlex.split(cmd)

  p = Popen(cmd, stdout=PIPE, stderr=PIPE)
  out, err = p.communicate()
  return (out, err)

def gpu_product_name():
    #https://codeyarns.com/tech/2019-04-26-nvidia-smi-cheatsheet.html
    try:
        stdout, stderr = run_cmd(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"])
        stdout = stdout.decode("utf-8")
        name = stdout.split('\n')[0]
    except:
        name = None
    return name

def gpu_memory():
    try:
        stdout, stderr = run_cmd(
            ["nvidia-smi", "--query-gpu=memory.free", "--format=csv,noheader"])
        stdout = stdout.decode("utf-8")
        mems = []
        for memory in stdout.split('\n'):
            if memory.strip():
                mems.append(int(memory.split()[0]))
    except:
        mems = []
    return mems

def ip_check(IP):
    IP = [int(s) for s in IP.split('.')]
    if len(IP) != 4 or min(IP) < 0 or max(IP) > 255:
        print("Error: the IP address obtained automatically is invalid, \
               please configure the IP manually")
        sys.exit(1)

def get_host_ip():
    def ip_check(IP):
        IP = [int(s) for s in IP.split('.')]
        if len(IP) != 4 or min(IP) < 0 or max(IP) > 255:
            print("Error: the IP address obtained automatically is invalid, \
                   please configure the IP manually")
            sys.exit(1)

    P = Popen("echo `ip addr show | grep inet\  | grep -v host\ lo | \
               grep -v docker0 | awk '{print $2}' | awk -F/ '{print $1}' | \
               head -n 1`", shell=True, stdout=PIPE)
    IP = P.stdout.readlines()
    assert len(IP) == 1
    IP = IP[0].decode('utf-8').strip('\r\n')
    ip_check(IP)
    return IP

def install_hasp():
    check_root()
    cmd = f"if [ ! -d '/etc/hasplm' ];then mkdir /etc/hasplm; fi; \
           cp {base_dir}/config/hasplm.ini /etc/hasplm/hasplm.ini; \
           cd {base_dir}/aksusbd; ./dinst;"
    os.system(cmd)

def uninstall_hasp():
    check_root()
    cmd = f"cd {base_dir}/aksusbd; ./dunst;"
    os.system(cmd)

def hasp_finger(args):
    print("generating fingerprint file")
    args.y = os.path.realpath(args.y)

    os.system(f"cd {base_dir};\
               if [ ! -d './license_data' ];then mkdir license_data; fi; \
               cd bin;./hasp_mgr f ../license_data/fingerprint.c2v;\
               cp ../license_data/fingerprint.c2v %s" % (args.y))

def hasp_lock(args):
    print("generating lock file")

    args.y = os.path.realpath(args.y)

    os.system(f"cd {base_dir}; \
               if [ ! -d './license_data' ];then mkdir license_data; fi; \
               cd bin;./hasp_mgr i ../license_data/lock.c2v;\
               cp ../license_data/lock.c2v %s" % (args.y))

def hasp_id(args):
    print("generating id file")

    args.y = os.path.realpath(args.y)

    os.system(f"cd {base_dir}; \
               if [ ! -d './license_data' ];then mkdir license_data; fi; \
               cd bin;./hasp_mgr c ../license_data/transfer.id;\
               cp ../license_data/transfer.id %s" % (args.y))

def hasp_rehost(args):
    print("generating rehost file")

    id_file = os.path.realpath(args.x)
    args.y = os.path.realpath(args.y)
    if not os.path.exists(id_file):
        print("Error: id file not exists")
        sys.exit(1)

    if not os.path.basename(args.x).endswith("id"):
        print("Error: invalid suffix of id file")
        sys.exit(1)
    
    os.system(f"cd {base_dir}; \
               if [ ! -d './license_data' ];then mkdir license_data; fi; \
               cp %s ./license_data/transfer.id;cd bin; \
               ./hasp_mgr r ../license_data/transfer.id \
               ../license_data/rehost.h2h;\
               if [ $? -eq 0 ]; then cp ../license_data/rehost.h2h %s; \
               fi" % (id_file, args.y))


def hasp_update(args):
    print("updating authorize file")

    authorize_file = os.path.realpath(args.x)
    if not os.path.exists(authorize_file):
        print("Error: authorize file not exists")
        sys.exit(1)

    if not (os.path.basename(authorize_file).endswith("h2h") or \
        os.path.basename(authorize_file).endswith("h2r") or \
        os.path.basename(authorize_file).endswith("V2CP")):
        print("Error: invalid suffix of authorize file")
        sys.exit(1)
    # copy file to license_data
    os.system(f"if [ ! -d '{base_dir}/license_data' ]; \
                   then mkdir license_data; fi")
    if os.path.basename(authorize_file).endswith("h2h"):
        bak_file = f"{base_dir}/license_data/rehost.h2h"
        os.system("cp %s %s" % (authorize_file,bak_file))
    if os.path.basename(authorize_file).endswith("V2CP"):
        bak_file = f"{base_dir}/license_data/authorize.V2CP"
        os.system(f"cp %s %s" % (authorize_file,bak_file))
    if os.path.basename(authorize_file).endswith("h2r"):
        bak_file = f"{base_dir}/license_data/authorize.h2r"
        os.system("cp %s %s" % (authorize_file,bak_file))

    os.system(f"cd {base_dir}/bin;./hasp_mgr u %s" % (bak_file))


def get_host_ip():
    def ip_check(IP):
        IP = [int(s) for s in IP.split('.')]
        if len(IP) != 4 or min(IP) < 0 or max(IP) > 255:
            print("Error: the IP address obtained automatically is invalid, \
                   please configure the IP manually")
            sys.exit(1)

    P = Popen("echo `ip addr show | grep inet\  | grep -v host\ lo | \
               grep -v docker0 | awk '{print $2}' | awk -F/ '{print $1}' | \
               head -n 1`", shell=True, stdout=PIPE)
    IP = P.stdout.readlines()
    assert len(IP) == 1
    IP = IP[0].decode('utf-8').strip('\r\n')
    ip_check(IP)
    return IP


def load_json(config_file):
    # get home path
    global HOME_PATH
    config_path = os.path.join(HOME_PATH, ".sae", "config", config_file)

    if not os.path.exists(config_path):
        print("Error: json file not exists, please check json file name")
        sys.exit(1)
    try:
        with open(config_path,'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print("Error: invalid json format,please check json content")
        sys.exit(1)


def get_container_names():
    cmd = "docker ps -a --format 'table {{.Names}}' | grep -v 'NAMES'"
    P = Popen(cmd, shell=True, stdout=PIPE)
    names_array = P.stdout.readlines()
    exists_names = list()
    for name in names_array:
        name = name.decode('utf-8').strip('\r\n')
        exists_names.append(name)

    return exists_names

def _get_version():
    res = runcmd("docker --version")
    if res is not None and "Docker version" in res:
        return res
    else:
        return None

def _check_docker():
    
    P = Popen("docker info", shell=True, stdout=PIPE,stderr=STDOUT)
    p = P.stdout.readlines()
    p = [e.decode('utf-8') for e in p]
    # 系统未安装 docker
    if len(p) == 1 and "docker: command not found" in p[0]:
        print("Docker is not installed in the current environment")
        sys.exit(1)

    # 系统安装了 docker,诊断 docker 是否正常
    s = ["ERROR" in elem for elem in p]
    if True not in s:
        res = _get_version()
        ver = re.findall("\d+",res.split()[2])  #eg:['23','0','0']
        ver = "".join([one if len(one) == 2 else one + '0' for one in ver ])
        
        # 环境已经安装docker,但版本不符合要求
        if float(ver) < float(19039):
            print("Error: the docker currently installed in the system is " + 
                "lower than 19.03.9 version required by the sdk, " + 
                "and docker is being reinstalled")
            sys.exit(1)
        else:
            print("INFO: the current system has already installed docker, " + 
                "and the version meets the requirements")
            return True
    else:
        print("Error: The current environment has installed docker, " + 
              "but there is a problem with the installation status, " + 
              "you can use `docker info` to view")
        sys.exit(1)

def is_enable_gpu():
    P = Popen("lspci | grep -i nvidia", shell=True, stdout=PIPE,stderr=STDOUT)
    p = P.stdout.readlines()
    if p:
        return True
    else:
        return False

def _check_docker2():
    if not is_enable_gpu():
        print("error: no gpu resource in current environment")
        sys.exit(1)
    P = Popen("rpm -qa | grep nvidia-docker", shell=True, 
            stdout=PIPE, stderr=STDOUT)
    p = P.stdout.readlines()
    p = [e.decode('utf-8') for e in p]
    
    Q = Popen("rpm -qa | grep nvidia-container-toolkit", shell=True,
            stdout=PIPE, stderr=STDOUT)
    q = Q.stdout.readlines()
    q = [e.decode('utf-8') for e in q]
    
    if len(p) or len(q):
        print("Info: the current environment has installed nvidia-docker2")
        return True
    else:
        print("error: nvidia-docker2 is not installed in the current environment")
        sys.exit(1)

def _check_driver():
    def get_driver_version():
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=driver_version', '--format=csv,noheader'])
        driver_version = output.decode('utf-8').strip().split('\n')
        driver_version = min([float(m.split('.')[0]) for m in driver_version])
        return driver_version

    if not is_enable_gpu():
        print("error: no gpu resource in current environment")
        sys.exit(1)
    P = Popen("nvidia-smi", shell=True, stdout=PIPE,stderr=STDOUT)
    p = P.stdout.readlines()
    p = [e.decode('utf-8') for e in p]
    s = ["Driver Version" in elem for elem in p]
    if True in s:
        print("Info: the current environment has installed nvidia-driver")
        driver_version = get_driver_version()
        if driver_version < 515:
            print("error: the current nvidia driver version is less than 515, please deploy manually")
            sys.exit(1)
        else:
            return True
    else:
        print("Info: nvidia-docker2 is not installed in the current environment")
        sys.exit(1)

def env_check():

    _check_docker()
    _check_docker2()
    _check_driver()

def stop_container(args):
    print("closing container")
    config_file = args.container_name + '.json'
    config = load_json(config_file)
    CONTAINER_NAME = config.get('container_name', None)
    if not CONTAINER_NAME:
        print("Error: empty 'container_name', please specify it in json file")
        sys.exit(1)
    os.system("docker stop %s" % (CONTAINER_NAME))
    os.system("docker rm %s" % (CONTAINER_NAME))


def run_container(args):
    config_file = args.container_name + '.json'
    config = load_json(config_file)
    CHECK_KEYS = ['license_token', 'gpus', 'image_name']
    for key in CHECK_KEYS:
        if key not in config:
            print("ERR: please set {0} in {1}".format(key, config_file))
            sys.exit(1)

    ports = config.get('api_ports', '8502,8506,8507').split(',')

    IMAGE_NAME = config.get("image_name")
    HOST_PATH = config.get('mount_path', 
        "{}/serving/exchange_file".format(HOME_PATH))
    CONTAINER_NAME = config.get("container_name")
    GPUS = config.get("gpus",'0')
    if config["gpus"] == "":
        GPUS = '0'
    token = config.get("license_token")

    if token == "local":
        token = get_host_ip()

    container_names = get_container_names()
    if CONTAINER_NAME in container_names:
        print("ERR: container name already exist, please change another name")
        sys.exit(1)

    if len(ports) == 3:
        ports_params = "-p {}:8502 -p {}:8506 -p {}:8507".format(ports[0], ports[1], ports[2])
    elif len(ports) == 4:
        ports_params = "-p {}:8502 -p {}:8506 -p {}:8507 -p {}:6556".format(ports[0], ports[1], ports[2], ports[3])
    else:
        print("ERR: wrong ports value in config {}".format(config_file)) 

    if gpu_product_name():
        run_gpus = GPUS if GPUS == "all" else '"device=%s"'%GPUS
    else:
        run_gpus = ""

    cmd = "docker run --shm-size 4g -itd \
            --restart always --name {} {} --gpus '{}' \
            -v {}:/home/serving/exchange_file \
            -v /etc/localtime:/etc/localtime:ro \
            {} --token={} --entrypoint /opt/sae/bin/entrypoint.sh".format(
                CONTAINER_NAME, ports_params, run_gpus, HOST_PATH,
                IMAGE_NAME, token)
    status = os.system(cmd)
    if status == 0:
       print(
         "INFO: succ to start %s use image %s" % (CONTAINER_NAME, IMAGE_NAME))
    else:
       print(
         "INFO: failed to start %s use image %s" % (CONTAINER_NAME, IMAGE_NAME))

def get_argparser():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(help='sub commands')

    hasp = sub_parsers.add_parser('hasp', help='install hasp or uninstall hasp')
    hasp.add_argument('--subcommand', default='hasp')
    hasp.add_argument("x", type=str,help="install or uninstall")

    hasp_mgr = sub_parsers.add_parser('hasp_mgr', 
            help='operate hasp license function')
    hasp_mgr.add_argument('--subcommand', default='hasp_mgr')
    hasp_mgr.add_argument('-u', '--update',
            help='updates Sentinel protection key/attaches a detached license', 
            type=str, default=None)
    hasp_mgr.add_argument('-i', '--retrieve_key',
            help='retrieves Sentinel protection key information, \
                output to <c2v_file> if specified', 
            type=str, default=None)
    hasp_mgr.add_argument('-c', '--retrieve_info',
            help='retrieves receipient information, \
                output to <id_file> if specified', 
            type=str, default=None)
    hasp_mgr.add_argument('-r', '--rehost',
            help='rehost a license from Sentinel SL-AdminMode/SL-UserMode key,\
                output to <h2h_file> if specified', 
            type=str, default=None)
    hasp_mgr.add_argument('-f', '--retrieve_fingerprint',
            help='retrieves fingerprint information, \
                output to <c2v_file> if specified', 
            type=str, default=None)

    hasp_f = sub_parsers.add_parser('hasp_f', help='generate fingerprint.c2v')
    hasp_f.add_argument('--subcommand', default='hasp_f')
    hasp_f.add_argument("y", type=str,help="output file path")

    hasp_u = sub_parsers.add_parser('hasp_u', help='update authorize file')
    hasp_u.add_argument('--subcommand', default='hasp_u')
    hasp_u.add_argument("x", type=str,help="input file")

    hasp_i = sub_parsers.add_parser('hasp_i', help='generate lock.c2v')
    hasp_i.add_argument('--subcommand', default='hasp_i')
    hasp_i.add_argument("y", type=str,help="output file path")

    hasp_r = sub_parsers.add_parser('hasp_r', help='generate rehost.h2h')
    hasp_r.add_argument('--subcommand', default='hasp_r')
    hasp_r.add_argument("x", type=str,help="input file")
    hasp_r.add_argument("y", type=str,help="output file path")

    hasp_c = sub_parsers.add_parser('hasp_c', help='generate transfer.id')
    hasp_c.add_argument('--subcommand', default='hasp_c')
    hasp_c.add_argument("y", type=str,help="output file path")

    check = sub_parsers.add_parser('env_check', help='env check')
    check.add_argument('--subcommand', default='env_check')

    run = sub_parsers.add_parser('run', help='start sdk container')
    run.add_argument('--subcommand', default='run')
    run.add_argument('container_name', type=str, help='json file name')

    run = sub_parsers.add_parser('stop', help='stop sdk container')
    run.add_argument('--subcommand', default='stop')
    run.add_argument('container_name', type=str, help='json file name')

    args = parser.parse_args()
    return args

def cli():
    args = get_argparser()
    if not hasattr(args, 'subcommand'):
        print('Wrong cmd parameters')
        return

    if args.subcommand == "hasp":
        if args.x == "install":
            install_hasp()
        elif args.x == "uninstall":
            uninstall_hasp()
        else:
            print("ERR: unsupported operations, "\
                  "can only be selected from install and uninstall")
            sys.exit(1)

    elif args.subcommand == "hasp_mgr":
        if args.update:
            os.system(f"cd {base_dir}/; ./hasp_mgr u %s"%(args.update))
            print("Executed: hasp_mgr u " + args.update)

        elif args.retrieve_key:
            os.system(f"cd {base_dir}; ./hasp_mgr i %s"%(args.retrieve_key))
            print("Executed: hasp_mgr i " + args.retrieve_key)

        elif args.retrieve_info:
            os.system(f"cd {base_dir}; ./hasp_mgr c %s"%(args.retrieve_info))
            print("Executed: hasp_mgr c " + args.retrieve_info)

        elif args.rehost:
            os.system(f"cd {base_dir}; ./hasp_mgr r %s"%(args.rehost))
            print("Executed: hasp_mgr r " + args.rehost)

        elif args.retrieve_fingerprint:
            os.system(f"cd {base_dir}; ./hasp_mgr f %s"%
                (args.retrieve_fingerprint))
            print("Executed: hasp_mgr f " + args.retrieve_fingerprint)


    # only support the container start, normal conatiner manager use docker cmd
    elif args.subcommand == "run":
        run_container(args)

    elif args.subcommand == "stop":
        stop_container(args)

    elif args.subcommand == "env_check":
        env_check()

if __name__ == '__main__':
    cli()
