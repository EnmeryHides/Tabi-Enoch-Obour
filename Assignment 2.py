for value in range( 1, 101):
    print(value)
    if value %3 == 0 and value %5 == 0:
        print('Fizz_Buzz')
    elif value %3 == 0:
        print('Fizz')
    elif value %5 == 0:
        print('Buzz')
    else:
        print('value')