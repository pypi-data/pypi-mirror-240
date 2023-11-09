from InquirerPy import prompt
import os
from ..funcs import add_new_host
from multiprocessing import Process
import docker
import time
from termcolor import colored
from .github_service import GithubService
from ..constants import PHALCON_DATA_DIR
from git import Repo
import pkg_resources

import shutil


class PhalconService:

    def __init__(self):
        self.select_version()
        self.github_service = GithubService()
        self.docker_compose = pkg_resources.resource_filename("phalcon", f"versions/{self.version}/docker-compose.yml")
        self.template = pkg_resources.resource_filename("phalcon", f"template.conf")

    def select_version(self):
        questions = [
            {
                "type": "list",
                "name": "phalcon_version",
                "choices": [
                    "3.4.x",
                    "4.0.x"
                ],
                "message": "Que versión de phalcon deseas usar?"
            }
        ]

        self.version = prompt(questions)["phalcon_version"]

    def configure_new_project(self):
        questions = [{
            "type": "input",
            "name": "project_name",
            "message": "Ingrese nombre para el proyecto",
        }]

        return prompt(questions)

    def run_server(self):
        index_file = f"{PHALCON_DATA_DIR}/{self.version}/projects/index.php"
        if not os.path.exists(os.path.dirname(index_file)):
            os.makedirs(os.path.dirname(index_file))

        if not os.path.exists(index_file):
            with open(index_file, "w+") as f:
                f.write("""<?php
                        phpinfo();""")
                
        os.system(f"docker-compose -f {self.docker_compose} up --build")

    def stop_server(self):
        os.system(f"docker-compose -f {self.docker_compose} stop")

    def wait_container(self, container_name):
        client = docker.from_env()
        while True:
            container = client.containers.get(container_name)
            if container.attrs["State"]["Running"]:
                break
            time.sleep(1)
            print(f"{colored('Info:', 'blue')} Iniciando contenedor {container_name}...")

    def add_project_from_github(self):
        repos = self.github_service.get_repos()
        questions = [
            {
                "type": "list",
                "name": "repo",
                "message": "Escoja los proyectos que desea agregar al servidor",
                "choices": [repo.full_name for repo in repos],
            }
        ]
        answers = prompt(questions)

        selected = [repo for repo in repos if repo.full_name == answers["repo"]][0]
        dest = f"{PHALCON_DATA_DIR}/{self.version}/projects/{selected.name.lower()}"

        try:
            print(f"Clonando repositorio {selected.full_name}")
            Repo.clone_from(selected.ssh_url, dest)

            with open(self.template) as f:
                config = f.read()
            
            config = config.replace("PROJECT_NAME", selected.name.lower())

            with open(f"{PHALCON_DATA_DIR}/{self.version}/vhosts/{selected.name.lower()}.conf", "w+") as f:
                f.write(config)
        except Exception as e:
            print(f"{colored('Error:', 'red')} {e}")
        
    def remove_project(self):
        path = f"{PHALCON_DATA_DIR}/{self.version}/projects"
        projects = [project for project in os.listdir(path) if os.path.isdir(f"{path}/{project}")]
        
        if not len(projects) > 0:
            print("No hay proyectos instalados en este servidor")
            return 
        
        questions = [
            {
                "type": "checkbox",
                "name": "projects",
                "message": "Seleccione los proyectos que desea eliminar",
                "choices": projects
            }
        ]

        answers = prompt(questions)

        if not len(answers["projects"]):
            print("No se seleccionó ningun proyecto")
            return

        for project in answers["projects"]:
            if os.path.exists(f"{path}/{project}"):
                shutil.rmtree(f"{path}/{project}")

            vhost = f"{PHALCON_DATA_DIR}/{self.version}/vhosts/{project}.conf"
            if os.path.exists(vhost):
                os.unlink(vhost)

        

    def create_phalcon_project(self):
        container_name = f"phalcon_{self.version}_app"
        process = Process(target=self.run_server, daemon=True, name="phalcon_create_project")
        process.start()
        self.wait_container(container_name)
        
        answers = self.configure_new_project()
        os.system(f"docker exec {container_name} bash -c 'phalcon create-project {answers['project_name']} && exit'")
        
        add_new_host([
            f"{answers['project_name']}.local"
        ])

        with open("app/phalcon/template.conf") as f:
            config = f.read()

        config = config.replace("PROJECT_NAME", answers["project_name"])
        # config = config.replace("PROJECT_DOMAIN", answers["domain"])

        dest_file = f"{PHALCON_DATA_DIR}/{self.version}/vhosts/{answers['project_name']}.conf"
        with open(dest_file, "w+") as f:
            f.write(config)

        self.stop_server()

        process.terminate()
        process.join()
        print("Proyecto creado correctamente")

    