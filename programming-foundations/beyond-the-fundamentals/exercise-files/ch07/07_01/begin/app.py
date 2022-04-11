# There are three main types of bugs
# syntax, run-time ,and logic errors

# syntax error ex
# def checkTemp(temp)
# if temp < 60
# print('Bring a jacket')

# fixed bug
# def checkTemp(temp):
#     if temp < 60:
#         print('Bring a jacket!')
# checkTemp(59)


# run-time error ex
# checkTemp(59)

# fixed bug
# def checkTemp(temp):
#   if temp < 60:
#     print('Bring a jacket!')
# checkTemp(59)


# logic error
# i=10
# while i>0:
#   i+=1
#   print(i)

# fixed bug
# i=10
# while i>0:
#   i-=1
#   print(i)
