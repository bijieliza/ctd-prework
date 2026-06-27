#Program to submit your personal information
name = input('Enter your name: ')
age = int(input('Enter your age: '))
if age >=18:
    print(name + ", you are "+ str(age) + " so you are good to go.")
else:
    print(name + ", you are "+ str(age) + " so you are not eligible.")
