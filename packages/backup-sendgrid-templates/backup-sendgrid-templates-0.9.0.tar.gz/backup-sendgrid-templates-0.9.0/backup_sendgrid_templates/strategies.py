import json
import logging
import os
from abc import ABC, abstractmethod
from pathlib import Path

from backup_sendgrid_templates.aws_utils import create_file_on_s3


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    See https://refactoring.guru/design-patterns/strategy/python/example
    """

    @abstractmethod
    def backup_template_version(
        self, template_name: str, version_data: any, backup_root: str
    ) -> bool:
        pass


class FileSystemStrategy(Strategy):
    def __init__(self, base_path: str = None):
        self._base_path = base_path or os.environ.get("SENDGRID_TEMPLATES_BASE_PATH")
        if not self._base_path:
            raise Exception("SENDGRID_TEMPLATES_BASE_PATH environment variable not set")

    @staticmethod
    def create_file_on_file_system(
        version_path: Path, file_name: str, file_content: str
    ) -> bool:
        (version_path / file_name).write_text(file_content, encoding="utf-8")
        return True

    def backup_template_version(
        self, template_name: str, version_data: any, backup_root: str
    ) -> bool:
        template_id = version_data[
            "template_id"
        ]  # template_id is repeated inside the version object
        version_name = version_data["name"]
        active = version_data["active"]
        html_content = version_data.pop("html_content")

        version_path = Path(self._base_path) / backup_root
        version_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Storing template files in directory {version_path}")

        file_prefix = (
            f"{template_id}_{template_name}{'_active' if active else ''}_{version_name}"
        )

        meta_file_name = f"{file_prefix}_metadata.json"
        _meta_created = self.create_file_on_file_system(
            version_path, meta_file_name, json.dumps(version_data)
        )
        content_file_name = f"{file_prefix}_content.html"
        _content_created = self.create_file_on_file_system(
            version_path, content_file_name, html_content
        )
        return _meta_created and _content_created


class S3Strategy(Strategy):
    def __init__(self, bucket_name: str = None):
        self._bucket_name = bucket_name or os.environ.get(
            "SENDGRID_TEMPLATES_BUCKET_NAME"
        )
        if not self._bucket_name:
            raise Exception(
                "SENDGRID_TEMPLATES_BUCKET_NAME environment variable not set"
            )

    def backup_template_version(
        self, template_name: str, version_data: any, backup_root: str
    ) -> bool:
        template_id = version_data[
            "template_id"
        ]  # template_id is repeated inside the version object
        version_name = version_data["name"]
        active = version_data["active"]
        html_content = version_data.pop("html_content")

        key_prefix = f"{backup_root}/{template_id}_{template_name}{'_active' if active else ''}_{version_name}"

        meta_key = f"{key_prefix}_metadata.json"
        _meta_created = create_file_on_s3(
            self._bucket_name, meta_key, json.dumps(version_data)
        )

        html_content_key = f"{key_prefix}_content.html"
        _content_created = create_file_on_s3(
            self._bucket_name, html_content_key, html_content
        )
        return _meta_created and _content_created
