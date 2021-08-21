class NewString:

    def __init__(self):
        self.str = ''

    def get_string(self):
        self.str = input('Nhập string: ')

    def print_string(self):
        print(self.str.upper())


str = NewString()
str.get_string()
str.print_string()
