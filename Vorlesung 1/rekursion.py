def my_print(x):
    print(x)
    # if statement to prevent endless loop
    if x == 0:
        return
    else:
        my_print(x-1)
    

my_print(5)

