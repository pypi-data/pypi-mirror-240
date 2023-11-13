from pathlib import Path
from pprint import pprint

from pydantic_settings import BaseSettings

ROOT_DIR = Path(__file__).parent.parent.parent.absolute()


class Environment(BaseSettings, extra="allow"):
    run_env: str = "local"
    log_level: str = "INFO"
    # notevault_doc_schema_path: str = f"{ROOT_DIR}/schemas/daily.yaml"
    notevault_doc_schema_path: str

    def __init__(self, **values):
        super().__init__(**values)

    def log_config(self) -> dict:
        cfg = self.model_dump(mode="json")
        skip_keys = ()
        sanitized_cfg = {k: v for k, v in cfg.items() if k not in skip_keys}
        return sanitized_cfg


config = Environment()
_ = None
