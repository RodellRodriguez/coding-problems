import types

def fib():
    """ Generator yielding Fibonacci numbers
    
    :returns: int -- Fibonacci number as an integer
    """
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

def is_a_generator_function(func):
    return type(func()) == types.GeneratorType

def main():
    if is_a_generator_function(fib):
        print("Good, The fib function is a generator.")
        counter = 0
        for n in fib():
            print(n)
            counter += 1
            if counter == 10:
                break

main()