### Challenges ###


from functools import reduce

""""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

listObj = [i for i in range(1,101) ]

for i in listObj:
    if(i % 3 == 0 and i % 5 ==0):
        print('fizzbuzz')
    elif(i % 3 == 0):
        print('fizz')
    elif(i % 5 == 0):
        print('buzz')
    else:
        print(i)

print('\n')
"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagram(word_one , word_two):
    if(word_one.lower() == word_two.lower()):
        return False
    else:
        word_one_list, word_two_list = [character for character in word_one], [character for character in word_two]
        word_one_list.sort(), word_two_list.sort()
        word_one, word_two = '', ''
        
        for i in word_one_list:
            word_one += i

        for i in word_two_list:
            word_two += i
            
        return word_two.lower() == word_one.lower()
      
print(is_anagram('hola', 'ohlA'))
print('\n')

# 
#  Escribe un programa que imprima los 50 primeros números de la sucesión
#  de Fibonacci empezando en 0.
#  - La serie Fibonacci se compone por una sucesión de números en
#    la que el siguiente siempre es la suma de los dos anteriores.
#    0, 1, 1, 2, 3, 5, 8, 13...
#  

def fibonacci():
    prev, next = 0, 1
    for index in range(0,50):
        print(f'Index: {index} \n Value:{prev}')
        fib = prev + next
        prev = next
        next = fib
        
fibonacci()

# 
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
# 

def is_prime_number(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


print(is_prime_number(97) )
print('\n')

# # 
# # Crea un programa que invierta el orden de una cadena de texto
# # sin usar funciones propias del lenguaje que lo hagan de forma automática.
# # - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
# # 

def reverse_string(my_string):
    reversed_string, my_string_array = '', [i for i in my_string]

    for _ in my_string:
        reversed_string += my_string_array.pop()

    return reversed_string

print(reverse_string('Messi is the best player of the world'))


def is_equilibrate(defs):
    
    array = [i for i in str(defs)]
    
    if(array.count('[') == array.count(']') and array.count('{') == array.count('}')and array.count('(') == array.count(')')):
        return True
    else:
        return False

print(is_equilibrate(is_equilibrate))       

numbers = [1, 5 ,3, 1, 12, 121, 31]
def filt(n):
    if n < 10:
        return True
    
    return False


print(list(filter(filt, numbers)))

print(reduce(lambda a, b : a + b, numbers))

