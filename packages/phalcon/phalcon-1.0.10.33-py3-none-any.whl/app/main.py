import click
from .funcs import is_docker_available
from .services.phalcon_service import PhalconService

@click.group()
@click.version_option("1.0.10.33")
def cli():
    pass

@cli.command()
def serve():
    """Start a complete php server with phalcon installed."""
    if not is_docker_available():
        return
    
    svc = PhalconService()
    svc.run_server()

@cli.command()
@click.option("-o", "--override", "override", is_flag=True)
def add(override):
    """Add new project to the server (sudo required)."""
    svc = PhalconService()
    svc.add_project_from_github(override)


@cli.command()
def remove():
    """Remove an existing project from the server (sudo required)."""
    svc = PhalconService()
    svc.remove_project()

@cli.command()
def new():
    """Creates a new phalcon project"""
    svc = PhalconService()
    svc.create_phalcon_project()