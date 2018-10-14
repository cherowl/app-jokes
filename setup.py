import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="api-jokes",
    version="0.0.1",
    author="Elena Cherkasova",
    author_email="cherowl@yandex.ru",
    description="RESTful API created with Flask and using PostgreSQL. Generate jokes for users.",
    long_description="...",
    long_description_content_type="...",
    url="git@github.com:cherowl/api-jokes.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    ],
    install_requires=['flask', 'pip-tools', 'psycopg2', 'configparser', 'requests']
)

export FLASK_ENV=development
export FLASK_APP=yourapplication