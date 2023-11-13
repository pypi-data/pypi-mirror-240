from datetime import datetime
from pathlib import Path

import typer

from notevault.create_models import create_models
from notevault.environment import ROOT_DIR
from notevault.helper import load_schema
from notevault.main import Main
from notevault.orm import Orm

app = typer.Typer()

# DOC_SCHEMA_PATH = f"{ROOT_DIR}/schemas/daily.yaml"
DOC_SCHEMA_PATH = f"{ROOT_DIR}/tests/resources/schema.yaml"


@app.command()
def daily(no_interactive: bool = False):
    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(DOC_SCHEMA_PATH)
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_name, doc_schema, orm)
    main.edit_and_parse(interactive=not no_interactive)
    main.save()
    # main.create(doc_name, md_text)
    if main.exists():
        print(f"Document found: {doc_name}.")


@app.command()
def export(name: str, force: bool = False):
    """ """
    if (Path.cwd() / f"{name}.md").exists() and not force:
        # write red typer error in color red
        typer.secho(f"Document exists: {name}. Use --force", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    if force:
        Path.cwd() / f"{name}.md".unlink(missing_ok=True)

    doc_schema = load_schema(DOC_SCHEMA_PATH)
    db_name = doc_schema["Config"]["database"]
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(name, doc_schema, orm)
    main.export(name)


if __name__ == "__main__":
    app()
