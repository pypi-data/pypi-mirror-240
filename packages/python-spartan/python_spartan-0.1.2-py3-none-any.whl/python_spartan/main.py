import subprocess

import typer
from alembic import command
from alembic.config import Config
from .services.application import ApplicationService
from .services.response import ResponseService
from .services.request import RequestService
from .services.model import ModelService
from .services.handler import HandlerService
from .services.migrate import MigrateService
from .services.test import TestService

alembic_cfg = Config("alembic.ini")

app = typer.Typer()
model_app = typer.Typer()
app.add_typer(model_app, name="model")

handler_app = typer.Typer()
app.add_typer(handler_app, name="handler")

migrate_app = typer.Typer()
app.add_typer(migrate_app, name="migrate")

request_app = typer.Typer()
app.add_typer(request_app, name="request")

response_app = typer.Typer()
app.add_typer(response_app, name="response")

db_app = typer.Typer()
app.add_typer(db_app, name="db")

def run_poetry_command(command):
    try:
        result = subprocess.run(
            ["poetry", command], capture_output=True, text=True, check=True
        )

        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command output:", e.output)


def is_valid_folder_name(name):
    """
    Check if a given string is a valid folder name.
    """

    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")

    return all(char in valid_chars for char in name)

@model_app.command("create")
def model_create(name: str):
    service = ModelService(name)
    service.create_model_file()

@model_app.command("delete")
def model_delete(name: str):
    service = ModelService(name)
    service.delete_model_file()

@handler_app.command("create")
def handler_create(
    name: str,
    subscribe: str = typer.Option(None, "--subscribe", "-s", help="Subscribe option"),
    publish: str = typer.Option(None, "--publish", "-p", help="Publish option"),
):
    handler_service = HandlerService(name, subscribe=subscribe, publish=publish)
    handler_service.create_handler_file()

@handler_app.command("delete")
def handler_delete(name: str):
    handler_service = HandlerService(name)
    handler_service.delete_handler_file()

@request_app.command("create")
def request_create(name: str):
    service = RequestService(name)
    service.create_request_file()

@request_app.command("delete")
def request_delete(name: str):
    service = RequestService(name)
    service.delete_request_file()

@migrate_app.command("upgrade")
def migrate_upgrade():
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_upgrade()

@migrate_app.command("create")
def migrate_create(
    message: str = typer.Option("", "--message", "-m", help="Message option"),
):
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_create(message=message)

@migrate_app.command("downgrade")
def migrate_downgrade():
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_downgrade()

@migrate_app.command("refresh")
def migrate_refresh():
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_refresh()

@migrate_app.command("init")
def migrate_init(
    database: str = typer.Option("", "--database", "-d", help="Database option"),
):
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migration_initialize(db_type=database)

@db_app.command("drop")
def db_drop():
    print("Dropping the database")

@db_app.command("seed")
def db_seed():
    print("Seeding the database")
    subprocess.run(["python", "-m", "database.seeders.database_seeder"])
    print("Done")

@db_app.command("wipe")
def db_wipe():
    print("Wiping the database")

@app.command("serve")
def serve(port: int = typer.Option(8888, "--port", "-p", help="Set port number")):
    poetry_command = f"poetry run uvicorn public.main:app --reload --port {port}"

    try:
        subprocess.run(poetry_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running serving the app")

@app.command("test")
def test(coverage: str = typer.Option(None, "-c", "--coverage", help="Path for coverage. Omit to skip coverage."),
         report: str = typer.Option(None, "-r", "--report", help="Type of coverage report. For example: 'html'")):
    runner = TestService(coverage, report)
    runner.run()

@app.command("init")
def app_create(project_name: str):
    creator = ApplicationService(project_name)
    creator.create_app()

@response_app.command("create")
def response_create(name: str):
    service = ResponseService(name)
    service.create_response_file()

@response_app.command("delete")
def request_delete(name: str):
    service = ResponseService(name)
    service.delete_response_file()


if __name__ == "__main__":
    app()
