from ArgType import ArgType
import string

default_charset = string.printable
default_charset_dict = {}
for c in default_charset:
    if c in string.punctuation:
        #Care more about punctuation as that is most likely to screw stuff up
        default_charset_dict[c] = 10
    else:
        default_charset_dict[c] = 1

DEFAULT_ARG_TYPE = ArgType(default_charset_dict)

ARG_TYPES = {}

#These are the main sql things that I can think of right now
sql_charset_dict = {'NULL':10, '\'':30, '--':10, '\\':30}

sql_charset_num = {".":1, "-":1}
for i in range(100):
    sql_charset_num[str(i)]=10

ARG_TYPES['sql'] = ArgType(sql_charset_dict)

ARG_TYPES['const'] = ArgType(None)

ARG_TYPES['num'] = ArgType(sql_charset_num)
