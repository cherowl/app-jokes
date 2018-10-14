from configparser import ConfigParser


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


# test
test = config(section='flask')
if test:
    for key, val in test.items():
        print("{}: {}".format(key, val))
