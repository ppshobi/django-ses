import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.utils.html import strip_tags


class SesBackend(BaseEmailBackend):
    DEFAULT_SES_REGION = 'us-east-1'

    def __init__(self, fail_silently=False, **kwargs):
        super(SesBackend, self).__init__(fail_silently=fail_silently, **kwargs)

    def send_messages(self, email_messages):
        client = self.get_ses_client()
        for mail in email_messages:
            email = {
                'Destinations': mail.recipients(),
                'RawMessage': {
                    'Data': mail.message().as_bytes(linesep='\r\n'),
                },
                'Source': mail.from_email,
            }

            try:
                return client.send_raw_email(**email)
            except ClientError as e:
                if not self.fail_silently:
                    raise e

    def get_ses_client(self):
        return boto3.client(
            'ses',
            aws_access_key_id=settings.SES_ACCESS_KEY,
            aws_secret_access_key=settings.SES_SECRET_KEY,
            region_name=settings.SES_REGION_NAME or self.DEFAULT_SES_REGION
        )
