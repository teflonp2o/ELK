import argparse
import json


parser = argparse.ArgumentParser(description='Manage ELK processes')
parser.add_argument('-a', dest='action', type=str, help='start, stop, status, start-core or stop-core')
parser.add_argument('-p', dest='process', type=str, help='elasticsearch, kibana, logstash or filebeat')
args = parser.parse_args()

es_home = "%USERPROFILE%"

with open(r'C:\Users\KPOLYGONE\ELK\config.json') as f:
    config = json.load(f)

class Process:
    def __init__(self, name, port, memory):
        print(name + ' ' + port + ' ' + memory)


def start(process, processes=None):
    if process in processes:
        command = config['ES_PATH_DIR'] + "\\" + process
        print(command)


def stop(process):
    if process in processes:
        command = config['']


def start_core(processes):
    for p in range(len(config["processes"])):
        start(config["processes"][i]['NAME'])


if __name__ == '__main__':
    if args.action == 'start-core':
        print(start_core(processes))
    elif args.action == 'start':
        print(start(args.process))
    elif args.action == 'stop':
        print(stop(args.process))
