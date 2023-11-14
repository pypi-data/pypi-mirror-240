import os
import subprocess
import tempfile
from datetime import datetime

from notevault.create_models import convert_instance_pydantic_to_sqlalchemy, create_all
from notevault.create_schemas import generate_models_from_yaml
from notevault.dal import load_document
from notevault.db import Session
from notevault.environment import ROOT_DIR
from notevault.helper import load_schema
from notevault.parse_md import parse_markdown

schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
document_structure = schema["DocumentStructure"]
model_spec = schema["Model"]

generated_schemas = generate_models_from_yaml(model_spec)
sqlalchemy_models = create_all(generated_schemas)

doc_name = f"{datetime.now().strftime("%Y-%m-%d")}.md"
with Session() as session:
    document = load_document(session, doc_name)
    if document:
        print(f"Document loaded {document.name=}.")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
            tmp.write(document.content.encode("utf-8"))
            tmp_path = tmp.name

        print(f"Document found {doc_name}.")
        # editor = os.environ.get('EDITOR', 'vim')  # Default to vim if EDITOR is not set
        # subprocess.call([editor, tmp_path])

        with open(tmp_path, "r") as file:
            md_text = file.read()

        parsed_objects = parse_markdown(md_text, document_structure, generated_schemas)

        document.content = md_text
        for obj in parsed_objects:
            sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
                obj, sqlalchemy_models[obj.__class__.__name__]
            )
            sqlalchemy_instance.document = document  # foreign key

            # Update session document
            # TODO: this portion is not generic any more
            if isinstance(sqlalchemy_instance, sqlalchemy_models["General"]):
                print(f"General: {sqlalchemy_instance}")
                document.generals = [sqlalchemy_instance]
            else:
                headings = [m.name for m in document.meetings]
                if sqlalchemy_instance.name in headings:
                    idx = headings.index(sqlalchemy_instance.name)
                    print(f"Meeting {sqlalchemy_instance.name} already exists {idx=}.")
                    document.meetings[idx] = sqlalchemy_instance
                    # meeting = next(m for m in document.meetings if m.name == sqlalchemy_instance.name)
                    # meeting = sqlalchemy_instance
                    # document.meetings.append(sqlalchemy_instance)
                else:
                    print(f"Meeting: {sqlalchemy_instance}")
                    document.meetings.append(sqlalchemy_instance)
                # session.add(sqlalchemy_instance)

        session.commit()

    else:
        print(f"Document not found {doc_name}.")
