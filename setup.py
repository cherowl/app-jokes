import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()    # TODO

setuptools.setup(
    name="app-jokes",
    version="1.0",
    author="Elena Cherkasova",
    author_email="cherowl@yandex.ru",
    description="RESTful API created with Flask using PostgreSQL. Generate jokes for users.",
    long_description="...",
    long_description_content_type="...",
    url={"Source Code":"git@github.com:cherowl/api-jokes.git"},
    packages=setuptools.find_packages(),
    install_requires=['flask', 'pip-tools', 'configparser', 'requests', 'flask-sqlalchemy', 'werkzeug', 'flask_basicauth', 'itsdangerous', 'flask_cors', 'flask_migrate', 'eventlet', 'psycopg2'] 
    # python_requires="python3.6.5"
    
)
# functools

# sudo apt install python3.6-dev
# python3 -m pip install psutil

# export FLASK_APP=run.py

# sqlite3 on server
# change it again to postgresql


