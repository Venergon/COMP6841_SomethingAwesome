KEY_WORDS = ["warning", "error"]
class SeenLines:
    def __init__(self):
        self.lines = set()
    
    def add(self, line, arg_list):
        self.lines.add(line)
        line = self.escape(line, arg_list)
        self.lines.add(line)

    def contains(self, line, arg_list):
        return line in self.lines or self.escape(line, arg_list) in self.lines

    def escape(self, line, arg_list):
        for arg in arg_list:
            line = line.replace(arg.get_arg_val(), "<argument-{}>".format(arg.get_arg_name()))
        return line

    def show(self, line, arg_list, show_unimportant):
        line = self.escape(line, arg_list)
        if self.has_key_word(line):
            line = "\033[31;1m" + line + "\033[39;49m"
        elif not show_unimportant:
            #Don't show this line
            return None
        return line

    def has_key_word(self, line):
        for word in KEY_WORDS:
            if word.lower() in line.lower():
                return True
        
        return False

         
