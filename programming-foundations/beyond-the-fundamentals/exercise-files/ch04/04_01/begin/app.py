from multiprocessing import Value


value = input('Enter a number : ')
print(value + ' is my favorite number')
print('when you multiply it by 10 , you get :')
value_int = int(value)
print(value_int * 10)
