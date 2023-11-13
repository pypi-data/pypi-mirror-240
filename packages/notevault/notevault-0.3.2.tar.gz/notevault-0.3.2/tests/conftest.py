import logging
from pathlib import Path

import pytest

from notevault.create_models import create_models
from notevault.environment import ROOT_DIR, config
from notevault.helper import load_schema
from notevault.main import Main
from notevault.orm import Orm
from tests.test_main import TEST_DOC_FILENAME

log = logging.getLogger(__name__)
log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=log_fmt, level=config.log_level, datefmt=datefmt)


@pytest.fixture
def main_instance():
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    Path(db_name).unlink(missing_ok=True)
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(TEST_DOC_FILENAME, doc_schema, orm)
    main.edit_and_parse(interactive=False)
    main.save()
    yield main
    Path(db_name).unlink(missing_ok=True)
