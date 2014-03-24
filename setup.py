from setuptools import setup, find_packages

_description = (
    "Form fields to make it easier to map CSV or JSON files to your own models"
)

setup(
    name='django-mapped-fields',
    version='0.0.2',
    description=_description,
    author="SF Software limited t/a Pebble",
    author_email="sysadmin@talktopebble.co.uk",
    url="https://github.com/mypebble/mapped-fields",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
