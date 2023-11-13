from setuptools import setup, find_packages

readme = """
![](https://raw.githubusercontent.com/CheeseCake87/Flask-Imp/master/_assets/Flask-Imp-Small.png)

# Flask-Imp

![Tests](https://github.com/CheeseCake87/Flask-Imp/actions/workflows/tests.yml/badge.svg)

## What is Flask-Imp?

Flask-Imp's main purpose is to help simplify the importing of blueprints, resources and models.
It has a few extra features built in to help with securing pages and password authentication.

## Documentation

[https://cheesecake87.github.io/Flask-Imp/](https://cheesecake87.github.io/Flask-Imp/)

## Getting Started

### Setup.

Create a new project folder and navigate to it.

```text
# Linux
cd /path/to/project-folder

# Windows
cd C:\path\\to\project-folder
```

### Create a virtual environment and activate it.

**Linux / MacOS**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
```

```bash
.\\venv\Scripts\\activate
```

### Install Flask-Imp

```bash
pip install flask-Imp
```

### Create a new project.

```bash
flask-Imp init
```
"""

setup(
    name='Flask-Imp',
    version='2.7.7',
    url='https://github.com/CheeseCake87/Flask-Imp',
    license='GNU Lesser General Public License v2.1',
    author='David Carmichael',
    author_email='carmichaelits@gmail.com',
    description='A Flask auto importer that allows your Flask apps to grow big.',
    long_description=f'{readme}',
    long_description_content_type='text/markdown',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
    ],
    install_requires=[
        'click',
        'Flask',
        'Flask-SQLAlchemy',
        'toml',
        'more-itertools'
    ],
    zip_safe=False,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'flask-imp = flask_imp_cli:cli',
        ]
    }
)
