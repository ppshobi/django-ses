import pprint

import boto3
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class SesBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        for mail in email_messages:

            email = {
                'Destination': {
                    'ToAddresses': mail.to,
                    'CcAddresses': mail.cc,
                    'BccAddresses': mail.bcc
                },
                'Message': {
                    'Body': {
                        'Html': {
                            'Charset': 'utf-8',
                            'Data': mail.body,
                        },
                        'Text': {
                            'Charset': 'utf-8',
                            'Data': mail.body,
                        }
                    },
                    'Subject': {
                        'Charset': 'utf-8',
                        'Data': mail.subject,
                    },
                },
                'Source': mail.from_email,
            }
            client = boto3.client(
                'ses',
                aws_access_key_id=settings.AWS_ACCESS_KEY,
                aws_secret_access_key=settings.AWS_SECRET_KEY,
                region_name=settings.AWS_REGION_NAME or None
            )

            return client.send_email(**email)
