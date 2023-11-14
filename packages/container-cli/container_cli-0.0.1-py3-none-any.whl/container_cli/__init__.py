import json
import re
import subprocess
import time

from loguru import logger
import checkopt
import questionary


def __close_docker():
    while 1:
        logger.info("正在关闭docker")
        status, output = subprocess.getstatusoutput("sudo systemctl stop docker")
        if status == 0:
            break
        else:
            logger.error("未能正确关闭docker")
            time.sleep(5)


def __get_container_id(container_name):
    while 1:
        status, output = subprocess.getstatusoutput("sudo docker inspect python | grep Id")
        if status != 0:
            logger.error("container name error")
            continue
        pattern = '"Id": "([a-zA-Z0-9]{64}?)",'

        # 使用正则表达式匹配并提取中间的内容
        match = re.search(pattern, output)
        if not match:
            logger.error("can't use re to match id")
            continue
        return match.groups()[0]


def __ask_ports():
    target_ports = {}  # {host_port: container_port}
    while 1:
        h = questionary.text("Please input host port, empty to exit").ask()
        if h == "":
            break
        c = questionary.text("Please input container port, empty to exit").ask()
        target_ports[h] = c
    return target_ports


def __update_ports(id, ports: dict):
    '''

    :param id: container id
    :param ports: {host_port: container_port}
    '''
    hostconfig_path = f"/var/lib/docker/containers/{id}/hostconfig.json"
    config_path = f"/var/lib/docker/containers/{id}/config.v2.json"

    hostconfig = json.load(open(hostconfig_path, 'r'))
    config = json.load(open(config_path, 'r'))

    new_PortBindings = {}
    new_ExposedPorts = {}
    new_Ports = {}
    for item_key in ports:
        host_port = item_key
        container_port = str(ports[item_key]) + "/tcp"
        new_PortBindings[container_port] = [{"HostIp": '', "HostPort":str(host_port)}]

        new_ExposedPorts[container_port]={}

        new_Ports[container_port]=[
            {"HostIp":"0.0.0.0","HostPort":host_port},
            {"HostIp":"::","HostPort":host_port},
        ]

    hostconfig["PortBindings"]=new_PortBindings
    config["Config"]["ExposedPorts"]=new_ExposedPorts
    config["NetworkSettings"]["Ports"]=new_Ports

    json.dump(hostconfig, open(hostconfig_path, 'w'))
    json.dump(config, open(config_path, 'w'))


def main():
    # opts,args=checkopt.checkopt("debug=")# --debug [path]
    # if "debug" in opts:
    #     logger.level("debug")
    container_name = questionary.text("Please input container name").ask()
    if not questionary.confirm("close docker?").ask():
        return -1
    __close_docker()
    id = __get_container_id(container_name)
    target_ports=__ask_ports()
    __update_ports(id,target_ports)
    logger.info("finished")



if __name__ == "__main__":
    main()
