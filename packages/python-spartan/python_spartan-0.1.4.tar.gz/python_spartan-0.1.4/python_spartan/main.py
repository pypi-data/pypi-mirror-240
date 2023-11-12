import subprocess

import typer
from alembic import command
from alembic.config import Config
from python_spartan.services.application import ApplicationService
from python_spartan.services.response import ResponseService
from python_spartan.services.request import RequestService
from python_spartan.services.model import ModelService
from python_spartan.services.handler import HandlerService
from python_spartan.services.migrate import MigrateService
from python_spartan.services.test import TestService
from python_spartan.services.inspire import InspireService
from python_spartan.services.deployment import DeploymentService

alembic_cfg = Config("alembic.ini")

app = typer.Typer()
model_app = typer.Typer()
app.add_typer(model_app, name="model", help="Manages the creation and deletion of model classes.")

handler_app = typer.Typer()
app.add_typer(handler_app, name="handler", help="Manages the creation and deletion of lambda files in the application.")

migrate_app = typer.Typer()
app.add_typer(migrate_app, name="migrate", help="Manages database changes, like updates, rollbacks, and making new tables.")

request_app = typer.Typer()
app.add_typer(request_app, name="request", help=" Manages the creation and deletion of request classes.")

response_app = typer.Typer()
app.add_typer(response_app, name="response", help=" Manages the creation and deletion of response classes.")

db_app = typer.Typer()
app.add_typer(db_app, name="db", help="Prepare your database tables.")

deploy_app = typer.Typer()
app.add_typer(deploy_app, name="deploy", help="Optimize your serverless project for deployment.")

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

@model_app.command("create", help="Create a new model class.")
def model_create(name: str):
    service = ModelService(name)
    service.create_model_file()

@model_app.command("delete", help="Delete an existing model class.")
def model_delete(name: str):
    service = ModelService(name)
    service.delete_model_file()

@handler_app.command("create", help="Create a new handler file with optional subscribe and publish options.")
def handler_create(
    name: str,
    subscribe: str = typer.Option(None, "--subscribe", "-s", help="Subscribe option."),
    publish: str = typer.Option(None, "--publish", "-p", help="Publish option."),
):
    handler_service = HandlerService(name, subscribe=subscribe, publish=publish)
    handler_service.create_handler_file()

@handler_app.command("delete", help="Delete an existing handler file.")
def handler_delete(name: str):
    handler_service = HandlerService(name)
    handler_service.delete_handler_file()

@request_app.command("create", help="Create a new request class.")
def request_create(name: str):
    service = RequestService(name)
    service.create_request_file()

@request_app.command("delete", help="Delete an existing request class.")
def request_delete(name: str):
    service = RequestService(name)
    service.delete_request_file()

@migrate_app.command("upgrade", help="Upgrade the database schema to the latest version.")
def migrate_upgrade():
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_upgrade()

@migrate_app.command("create", help="Create a new database migration with an optional message.")
def migrate_create(
    message: str = typer.Option("", "--message", "-m", help="Message option."),
):
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_create(message=message)

@migrate_app.command("downgrade", help="Downgrade the database schema to a previous version.")
def migrate_downgrade():
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_downgrade()

@migrate_app.command("refresh", help="Refresh the database migrations.")
def migrate_refresh():
    migrate_service = MigrateService(alembic_cfg)
    migrate_service.migrate_refresh()

@migrate_app.command("init", help="Initialize database migration with a specified database type.")
def migrate_init(
        database: str = typer.Option(None, '--database', '-d', help="The database type (sqlite, mysql, or psql)..")
):
    migrate_service = MigrateService(alembic_cfg)

    # Validate the database type
    if database not in ['sqlite', 'mysql', 'psql']:
        typer.echo("Invalid or no database type specified. Please choose from 'sqlite', 'mysql', or 'psql'.")
        raise typer.Exit()

    # Proceed with migration initialization
    migrate_service.migrate_initialize(database)
    typer.echo(f"Migration initialized for database type: {database}")

@db_app.command("seed", help="Seed the database with initial data.")
def db_seed():
    print("Seeding the database")
    subprocess.run(["python", "-m", "database.seeders.database_seeder"])
    print("Done")

@deploy_app.command("config", help="Copy a YAML file for infrastructure as code.")
def deploy_config(source: str = typer.Argument(..., help="Source file path (absolute or relative)")):
    deployment_service = DeploymentService()
    deployment_service.config(source)

@app.command("serve", help="Serve the application on a specified port.")
def serve(port: int = typer.Option(8888, "--port", "-p", help="Set port number.")):
    poetry_command = f"poetry run uvicorn public.main:app --reload --port {port}"

    try:
        subprocess.run(poetry_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running serving the app")

@app.command("test", help="Run tests with optional coverage and report.")
def test(coverage: str = typer.Option(None, "-c", "--coverage", help="Path for coverage. Omit to skip coverage.."),
         report: str = typer.Option(None, "-r", "--report", help="Type of coverage report. For example: 'html'.")):
    runner = TestService(coverage, report)
    runner.run()

@app.command("init", help="Initialize a new serverless project.")
def app_create(project_name: str):
    creator = ApplicationService(project_name)
    creator.create_app()

@app.command("inspire", help="Displays a random inspirational quote and its author for the Spartan like you.")
def inspire_display():
    inspiration_service = InspireService()
    quote = inspiration_service.get_random_quote()
    typer.echo(quote)

@response_app.command("create", help="Create a new response class.")
def response_create(name: str):
    service = ResponseService(name)
    service.create_response_file()

@response_app.command("delete", help="Delete an existing response class.")
def request_delete(name: str):
    service = ResponseService(name)
    service.delete_response_file()


if __name__ == "__main__":
    app()
