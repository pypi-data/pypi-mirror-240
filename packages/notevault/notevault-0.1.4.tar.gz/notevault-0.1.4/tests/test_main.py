from pathlib import Path

import pytest

TEST_DOC_NAME = "daily.md"
TEST_DOC_FILENAME = f"{TEST_DOC_NAME}.md"


@pytest.fixture
def doc_path():
    (Path.cwd() / TEST_DOC_FILENAME).unlink(missing_ok=True)
    yield Path.cwd() / TEST_DOC_FILENAME
    (Path.cwd() / TEST_DOC_FILENAME).unlink(missing_ok=True)


# @pytest.mark.skip("order of operations is not correct, works alone")
def test_export_success(main_instance):

    main_instance.export(TEST_DOC_NAME)

    # Assert that file is created and content is correct
    export_path = Path.cwd() / TEST_DOC_FILENAME
    assert export_path.exists()
    with open(export_path, 'r') as file:
        assert "lorem ipsum" in file.read()


@pytest.mark.skip("order of operations is not correct, works alone")
def test_export_non_existent(main_instance, capsys):

    main_instance.export("non_existent_doc")

    # Capture stdout and assert correct message
    captured = capsys.readouterr()
    assert "Document not found: non_existent_doc" in captured.out
