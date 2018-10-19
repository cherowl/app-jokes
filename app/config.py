import os
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users_jokes.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

def config(filename='config_data.ini', section=None):
    try:
        open(filename)
    except IOError as e:
        print(e)
    else:    
        # create a parser
        parser = ConfigParser()
        parser.optionxform=str # case sensetive 

        # read config file
        parser.read(filename)

        # get section, default to postgresql
        data = {}
        if parser.has_section(section):
            for param, value in parser.items(section):
                data[param] = value
        else:
            raise Exception("No section {} in the file {}".format(section, filename))

        return data


# # test
# test = config(section='flask')
# if test:
#     for key, val in test.items():
#         print("{}: {}".format(key, val))
