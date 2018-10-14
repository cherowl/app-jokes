from configparser import ConfigParser


def config(filename='./config_data.ini', section=None):
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
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return data


# # test
# test = config(section='flask')
# for key, val in test.items():
#     print("{}: {}".format(key, val))
