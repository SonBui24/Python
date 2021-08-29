import os

def get_file_size(file):
    return os.path.getsize(file)

file = 'test.txt'
print(f'Dung lượng của {file} là {get_file_size(file)} bytes')
