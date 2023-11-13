import os
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import TypeVar, Any

from pydantic import BaseModel

from notevault.create_models import (
    convert_instance_pydantic_to_sqlalchemy, create_models
)
from notevault.orm import Orm
from notevault.create_schemas import generate_models_from_yaml
from notevault.helper import load_schema
from notevault.parse_md import parse_markdown

T = TypeVar("T", bound=BaseModel)


class Main:
    def __init__(self, name: str, doc_schema: dict[str, Any], orm: Orm) -> None:
        self.name = name
        self.content: str = ""
        schema = doc_schema
        self.document_spec = schema["DocumentStructure"]
        self.model_spec = schema["Model"]
        self.orm = orm
        self.template = schema["Config"]["template"]

        # Generate the models
        self.generated_schemas = generate_models_from_yaml(self.model_spec)
        self.sqlalchemy_models = self.orm.create_all(self.generated_schemas)
        self.parsed_objects: list[BaseModel] = []

    def exists(self) -> bool:
        document = self.orm.load_document(self.name)
        if document:
            return True
        else:
            return False

    def read_or_init(self) -> None:
        document = self.orm.load_document(self.name)
        if document:
            self.content = document.content
        else:
            print(f"Document not found: {self.name}, using template: {self.template}.")
            with open(self.template, "r") as file:
                self.content = file.read()

    def edit_and_parse(self, interactive: bool = False) -> None:
        self.read_or_init()
        tmp_path = self._edit_content(interactive)
        self._parse_content(tmp_path)

    def _edit_content(self, interactive: bool) -> str:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
            tmp.write(self.content.encode('utf-8'))
            tmp_path = tmp.name

        if interactive:
            editor = os.environ.get('EDITOR', 'vim')
            subprocess.call([editor, tmp_path])

        return tmp_path

    def _parse_content(self, tmp_path: str) -> None:
        with open(tmp_path, "r") as file:
            self.content = file.read()

        self.parsed_objects = parse_markdown(self.content, self.document_spec, self.generated_schemas)

    def save(self):
        document = self.orm.load_document(self.name)
        if not document:
            document = self.orm.document_model(name=self.name, content=self.content)
            for obj in self.parsed_objects:
                obj_type = obj.__class__.__name__
                sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
                    obj, self.sqlalchemy_models[obj_type]
                )
                sqlalchemy_instance.document = document
            self.orm.session.add(document)
        else:
            print(f"Document loaded {document.name=}.")
            document.content = self.content
            for obj in self.parsed_objects:
                obj_type = obj.__class__.__name__
                sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
                    obj, self.sqlalchemy_models[obj_type]
                )
                sqlalchemy_instance.document = document

                # Update session document
                is_list = next(
                    s["section"]["is_list"] for s in self.document_spec["Sections"] if
                    s["section"]["type"] == obj_type
                )
                instrumented_list = obj_type.lower() + "s"
                if not is_list:
                    print(f"{obj_type}: {sqlalchemy_instance}")
                    setattr(document, instrumented_list, [sqlalchemy_instance])  # 1:1 relationship
                else:
                    current_value = getattr(document, instrumented_list)  # 1:n relationship -> InstrumentedList
                    headings = [m.name for m in current_value]
                    if sqlalchemy_instance.name in headings:
                        idx = headings.index(sqlalchemy_instance.name)
                        print(f"{obj_type} {sqlalchemy_instance.name} already exists {idx=}.")
                        current_value[idx] = sqlalchemy_instance
                        # document.meetings[idx] = sqlalchemy_instance
                    else:
                        print(f"{obj_type}: {sqlalchemy_instance}")
                        # document.meetings.append(sqlalchemy_instance)
                        current_value.append(sqlalchemy_instance)
            self.orm.session.commit()

    def export(self, name: str) -> None:
        document = self.orm.load_document(name)
        if not document:
            print(f"Document not found: {name}")
            return

        file_path = Path.cwd() / f"{name}.md"
        with open(file_path, 'w') as file:
            file.write(document.content)
        print(f"Document exported to {file_path}")


if __name__ == "__main__":
    interactive = True
    if interactive:
        # Attach debugger
        user_input = input("Please enter some data: ")
        # print("You entered:", user_input)

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema("tests/resources/schema.yaml")
    db_name = load_schema("tests/resources/schema.yaml")["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_name, doc_schema, orm)
    main.edit_and_parse(interactive=interactive)
    main.save()
    # main.create(doc_name, md_text)
    if main.exists():
        print(f"Document found: {doc_name}.")
