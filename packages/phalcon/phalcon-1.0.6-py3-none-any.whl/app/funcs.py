import docker
from termcolor import colored
from python_hosts import Hosts, HostsEntry
from python_hosts.exception import UnableToWriteHosts

def is_docker_available():
    running = False
    try:
        client = docker.from_env()
        client.ping()
        running = True
    except:
        print(f"{colored('Docker Unavailable:', 'yellow')} Asegurate que docker está instalado y corriendo.")
    return running

def add_new_host(names = []):
    try:
        hosts = Hosts()

        entry = HostsEntry(entry_type="ipv4", address="127.0.0.1", names=names)

        hosts.add(entries=[entry], force=True)

        hosts.write()

        print("Se agregó el host correctamente")
    except UnableToWriteHosts as e:
        print("Error:", e)


def remove_host(name):
    try:
        hosts = Hosts()
        if not hosts.exists(names=[name]):
            return 
        hosts.remove_all_matching(name=name)
        hosts.write()
        print("Se eliminó el host correctamente")
    except Exception as e:
        print("Error:", e)

