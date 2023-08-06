# backupSendgridTemplates
Backup the dynamic templates of a Sendgrid account.

Backup files can be stored on your local file system or a S3 bucket.


## Requirements
- python 3.8 or higher

## Installation
Create and activate a virtual environment. Then

`python -m pip install backupSendgridTemplates`

If you want to backup the templates on a S3 bucket, run

`python -m pip install backupSendgridTemplates[s3]`

## Setup
Some environment variables are required:
- `SENDGRID_API_KEY` - Sendgrid API key with full access (https://app.sendgrid.com/settings/api_keys)
- `SENDGRID_TEMPLATES_BUCKET_NAME` - the name of your bucket if you want to use S3 as destination
- `SENDGRID_TEMPLATES_BASE_PATH` - the path where to store files on your file system

The Sendgrid api key must have full access (more info [here](https://docs.sendgrid.com/ui/account-and-settings/api-keys)).


## Usage
### Run at command line
```
> backup_sg_on_file_system     # to create the backup files on your local file system
> backup_sg_on_s3              # to create the backup files on a S3 bucket
```

### Run inside a script
```
from backup_sendgrid_templates.service import BackupSendgridTemplatesService
from backup_sendgrid_templates.strategies import FileSystemStrategy, S3Strategy

BackupSendgridTemplatesService(strategy=FileSystemStrategy()).run()
# or BackupSendgridTemplatesService(strategy=S3Strategy()).run()
```

Two files are created for each template: a .json file containing the template metadata (like name, subject, etc)
and an HTML file with the template content.

### Restoring a template
Create a new template on the Sendgrid website.
In the `design` page, open the `Build` tab and expand the `advanced` section.

Click on `Import Drag & Drop HTML` and paste the html content retrieved from the backup.


## References

Send an email using a Sendgrid dinamyc transactional template: https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates

Sendgrid API:
https://docs.sendgrid.com/for-developers/sending-email/api-getting-started

Official Python wrapper by Sendgrid:
https://github.com/sendgrid/sendgrid-python
