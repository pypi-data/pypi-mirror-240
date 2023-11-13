from subprocess import Popen
import logging
import requests

import click
import uvicorn

from bitbuilder.src.listener.cloud_dev_env_listener import CloudDevEnvListener
from bitbuilder.src.models.workspaces.constants import HEALTH_CHECK_URL_ROUTE, LISTENER_PORT


CLI_VERSION = '0.1.3'

def create_listener_and_run(repo_dir: str, auth_token: str | None = None):
    try:
        listener = CloudDevEnvListener(repo_dir, auth_token=auth_token)
        app = listener.create_fastapi_app()
        print(f"Listener started on port {LISTENER_PORT}")
        uvicorn.run(app, port=LISTENER_PORT, log_level="debug")
    except Exception as e:
        logging.error("Error starting the listener: %s", str(e))
        print(e)

@click.group()
def cli():
    pass

@cli.command()
def version():
    click.echo(f"Version {CLI_VERSION}")

@cli.command()
def ping():
    click.echo("pong")

@click.group()
def listener():
    pass

@listener.command()
@click.argument('repo_dir')
def start(repo_dir: str):
    try:
        response = requests.get(f"http://localhost:{LISTENER_PORT}{HEALTH_CHECK_URL_ROUTE}")
        if response.status_code == 200:
            click.echo("Listener already running.")
            return
    except requests.exceptions.ConnectionError:
        pass
    background_process = Popen(['python', 'bitbuilder/_listener.py', repo_dir])
    click.echo(f"Starting listener in background process with PID {background_process.pid}...")


@listener.command()
def stop():
    try:
        response = requests.get(f"http://localhost:{LISTENER_PORT}{HEALTH_CHECK_URL_ROUTE}")
        click.echo(response.json())
        if response.status_code != 200:
            click.echo("Listener not running, nothing to stop.")
            return
    except requests.exceptions.ConnectionError:
        click.echo("Listener not running, nothing to stop.")
        return
    response_json = response.json()
    pid = response_json['pid']
    Popen(['kill', str(pid)])
    click.echo(f"Killed listener with PID {pid}.")

cli.add_command(ping)
cli.add_command(version)
cli.add_command(listener)

if __name__ == '__main__':
    cli()
