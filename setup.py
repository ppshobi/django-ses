import setuptools
from distutils.core import setup
with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_ses_email_backend",
    version="0.0.1",
    author="Shobi P P",
    author_email="ppshobi@gmail.com",
    description="A Drop in Replacement for default django email backend based on Amazon SES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ppshobi/django-ses",
    packages=setuptools.find_packages(),
    install_requires=[
       'boto3>=1.8.5',
       'Django>=1.9',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)