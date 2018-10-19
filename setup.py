import setuptools
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()    # TODO

setuptools.setup(
    name="api-jokes",
    version="1.0",
    author="Elena Cherkasova",
    author_email="cherowl@yandex.ru",
    description="RESTful API created with Flask and using PostgreSQL. Generate jokes for users.",
    long_description="...",
    long_description_content_type="...",
    url="git@github.com:cherowl/api-jokes.git",
    packages=setuptools.find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3.7",
    #     "Operating System :: OS Linux",
    # ],
    install_requires=['flask', 'pip-tools', 'configparser', 'requests', 'flask-sqlalchemy', 'flask-exceptional'] # pysqlite3 or sqlite3 
)

# flask-migrate

subprocess.run("export FLASK_ENV=development")
subprocess.run("export FLASK_APP=run")