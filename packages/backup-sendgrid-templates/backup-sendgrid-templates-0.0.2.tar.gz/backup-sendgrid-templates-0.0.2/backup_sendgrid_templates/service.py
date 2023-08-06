import datetime
import json
import logging
import os

from sendgrid import SendGridAPIClient

from backup_sendgrid_templates.strategies import FileSystemStrategy


class BackupSendgridTemplatesService:
    def __init__(self, backup_only_active_versions=False, api_key=None, strategy=None):
        self.backup_only_active_versions = backup_only_active_versions
        _api_key = api_key or os.environ.get("SENDGRID_API_KEY")
        if not _api_key:
            raise Exception("SENDGRID_API_KEY environment variable not set")
        self.sendgrid_client = SendGridAPIClient(_api_key).client
        self.now = datetime.datetime.utcnow().isoformat()
        self.strategy = strategy or self.get_default_strategy()

    @staticmethod
    def get_default_strategy():
        return FileSystemStrategy()

    def run(self):
        """Backup sendgrid templates"""
        logging.info("Backupping sendgrid templates...")
        templates_metadata = self.get_templates_metadata()
        template_count, version_count, error_count = 0, 0, 0
        for template_data in templates_metadata:
            templates, versions, errors = self.retrieve_template_and_backup_it(
                template_data
            )
            template_count += templates
            version_count += versions
            error_count += errors
        logging.info("\nSendgrid templates backupped.")
        logging.info(
            f"{template_count} templates, {version_count} versions, {error_count} errors."
        )
        return {
            "template_count": template_count,
            "version_count": version_count,
            "error_count": error_count,
        }

    def get_templates_metadata(self):
        """Get templates from sendgrid"""
        # As of today, Sendgrid docs wrongly report the parameter of get() method if you want to retrieve all the
        # existing templates.
        response = self.sendgrid_client.templates.get(
            None, {"generations": "legacy,dynamic"}
        )
        if response.status_code == 200:
            response_body = json.loads(response.body)
            templates = response_body["templates"]
            logging.info(f"Found {len(templates)} templates")
            logging.debug(templates)
            return templates
        logging.info(
            f"Request to sendgrid failed: {response.body} (status code: {response.status_code})"
        )
        return []

    def retrieve_template_and_backup_it(self, template):
        """Backup the provided template depending on the selected strategy"""
        uploaded_versions = 0
        errors = 0

        template_id = template["id"]
        template_name = template["name"]
        logging.info(f"TEMPLATE {template_id} - {template_name}")

        response = self.sendgrid_client.templates._(template_id).get()
        if response.status_code != 200:
            logging.info(
                f"Error retrieving template {template_id}, nothing uploaded on S3..."
            )
            return 0, 0, 1

        # template_data contains the html content for each version.
        template_data = json.loads(response.body)

        for version_data in template_data["versions"]:
            if self.backup_only_active_versions and not version_data["active"]:
                logging.info(
                    f"Skipping inactive version \"{version_data['name']}\" (id {version_data['id']})"
                )
                continue

            if self.strategy.backup_template_version(
                template_name, version_data, self.now
            ):
                uploaded_versions += 1

        # if at least 1 version has been uploaded on S3 then increment also the number of uploaded templates.
        uploaded_templates = 1 if uploaded_versions > 0 else 0
        logging.info(
            f"{uploaded_templates} templates uploaded, {uploaded_versions} versions uploaded, {errors} errors"
        )
        return uploaded_templates, uploaded_versions, errors
