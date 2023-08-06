import logging

from backup_sendgrid_templates.service import BackupSendgridTemplatesService
from backup_sendgrid_templates.strategies import FileSystemStrategy, S3Strategy

logging.basicConfig(level=logging.INFO)


def backup_templates_on_file_system(api_key: str = None):
    """
    Backup all existing templates found in a Sendgrid account. Save the templates and their versions on a local file
    system.
    Args:
        api_key (str): sendgrid api key. If not provided, the environment variable SENDGRID_API_KEY is used.
    Returns:
        None
    """
    BackupSendgridTemplatesService(api_key=api_key, strategy=FileSystemStrategy()).run()


def backup_templates_on_s3(api_key: str = None):
    """
    Backup all existing templates found in a Sendgrid account. Save the templates and their versions on a S3 bucket.
    Args:
        api_key (str): sendgrid api key. If not provided, the environment variable SENDGRID_API_KEY is used.
    Returns:
        None
    """
    BackupSendgridTemplatesService(api_key=api_key, strategy=S3Strategy()).run()


if __name__ == "__main__":
    backup_templates_on_file_system()
    # backup_templates_on_s3()
