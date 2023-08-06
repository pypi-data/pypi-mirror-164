from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = '0.0.2'
DESCRIPTION = 'A cross-platform design theme framework.'


# Setting up
setup(
    name="blendedux",
    version=VERSION,
    author="Himanshu",
    author_email="<hbhadu@cognam.com>",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'certifi==2022.5.18.1',
        'click==8.1.3',
        'colorama==0.4.4',
        'Flask==0.11.1',
        'itsdangerous==2.0.1',
        'Jinja2==2.8',
        'MarkupSafe==2.0.1',
        'Pillow==8.0.1',
        'python-dateutil==2.8.2',
        'six==1.16.0',
        'urllib3==1.26.9',
        'Werkzeug==2.0.3',
        'blendedUx-Lang==1.0.0'
    ]
)