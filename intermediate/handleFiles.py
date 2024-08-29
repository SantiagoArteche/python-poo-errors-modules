import os

my_file = open('intermediate/hola.txt', 'r+')
print(my_file.read())
my_file.write('\nNew line')

my_file.close()


os.remove('intermediate/hola.txt')