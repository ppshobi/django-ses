[![Build Status](https://travis-ci.org/ppshobi/django-ses.svg?branch=master)](https://travis-ci.org/ppshobi/django-ses)
[![codecov](https://codecov.io/gh/ppshobi/django-ses/branch/master/graph/badge.svg)](https://codecov.io/gh/ppshobi/django-ses)
# Django Ses 
Another Django Email Backend on top of Amazon Simple Email Service (SES). Supports `Django 1.9`, `1.10`, `1.11`, `2.0`, `2.1`
. Using the latest boto3 to make API Calls, Tested using `moto` 
 
## What is this package about
Every web application needs to send email at some point, may it be verification, password resets, updates etc..., Django by default supports SMTP protocol, simply specify smtp credentials and you are ready to go.
But when you use Amazon Services such as SES the preferred way is to access it via its API.  
 
So Here it is guys. Simply install it, give the SES credentials, and start sending Emails.
More over if your application is hosted in AWS first ~60000 emails are free every month
 
## Table of Contents
   - [Installation](#installation)
   - [SES Credential Setup](#ses-credential-setup)
   - [Usage](#usage)
   - [TODO](#todo)
   - [Contribution](#contribution)

### Installation
This package is available via pip, So install it using pip

`pip install django-ses`

and add it in your INSTALLED_APPS section of settings.py
```
INSTALLED_APPS = [
    'django_ses',
     ...
]
```

### SES Credential Setup
Obviously you need to have access to an AWS SES account, generate credentials by following [this guide](https://www.formget.com/amazon-ses-iam/) or if you already have access keys use it.

in your settings.py add it as follows
````
SES_ACCESS_KEY = 'xxx'
SES_SECRET_KEY = 'xxx'
SES_REGION_NAME = 'us-east-1'  
````
`SES_REGION_NAME` is optional defaults to `us-east-1`

 **You need to [verify domain](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html) or [verify email](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) in order to send emails outside** 

### Usage
Once the setup is done you can send emails as usual, your existing calls to emails should work without any modifications

#### example 1 - Using `send_mail()`
    send_mail(subject="Test Subject", message="Message", from_email="from@example.com", recipient_list=['to@example.com'])

#### example 2 - Using `EmailMessage`
    email = EmailMessage(
        'Subject 1',
        'Body1 goes here',
        'from@example.com',
        ['to1@example.com', 'to2@example.com'],
        reply_to=['another@example.com'],
    )
    
    email.send()

https://docs.djangoproject.com/en/2.1/topics/email for more details

### TODO
   * Pre Send, Post Send Signals
### Contribution 
   * Submit issues to [Github Issues](https://github.com/ppshobi/django-ses/issues)
   * Submit patches to the `develop` branch 
   * Kindly write tests to justify any additions