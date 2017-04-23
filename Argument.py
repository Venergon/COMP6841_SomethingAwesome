import random
from argtype_dict import ARG_TYPES
from argtype_dict import DEFAULT_ARG_TYPE

class Argument:
    def __init__(self, arg_name, arg_val, arg_type=None):
        self.arg_name = arg_name
        self.arg_val = arg_val
        
        #Set the argument type, which makes it more or less likely to change to certain characters
        if arg_type is None:
            arg_type_name = input("What is the argument type for '{}'? ".format(arg_name))
            if arg_type_name in ARG_TYPES:
                self.arg_type = ARG_TYPES[arg_type_name]
            else:
                print("No arg type listed for '{}', using default instead".format(arg_type_name))
                self.arg_type = DEFAULT_ARG_TYPE
        else:
            self.arg_type = arg_type

    def change(self):
        new_arg_list = list(self.arg_val)

        #Change the argument based on the arg type
        index_to_change = random.randint(0, len(new_arg_list)-1)
        new_arg_list[index_to_change] = self.arg_type.new_char(new_arg_list[index_to_change])
        self.arg_val = "".join(list(new_arg_list))
        

    def __str__(self):
        return self.arg_name + "=" + self.escape(self.arg_val)

    def unescape_str(self):
        return self.arg_name + "=" + self.arg_val

    def escape(self, part):
        result = ""
        for char in part:
            result += "%"+hex(ord(char))[2:]

        return result

    def get_arg_name(self):
        return self.arg_name

    def get_arg_val(self):
        return self.arg_val
