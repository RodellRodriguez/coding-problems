import collections


"""
Flattenning without using generators. The downside of this approach is that
we are concatening arrays together per each recursive call. This is fine for small 
arrays but when the scale increases and it becomes impossible to put the arrays in memory
it is much more effective to stream the values one value at a time via generators
"""
def flatten(nested_list):
   ret = []
   for data in nested_list:
       if is_a_list(data) and not is_a_string(data):
           ret += flatten(data)
       else:
           ret.append(data)
   return ret


"""
Idea is to recursively go inside the nested lists until a number is encountered
then yield that value to make it a generator function.
"""
def flatten_generator(nested_list):
    for data in nested_list:
        if is_a_list(data) and not is_a_string(data):
            yield from flatten_generator(data)
        else:
            yield data

def is_a_list(data):
    # isInstance() is a built in Python method
    return isinstance(data, collections.Iterable)

def is_a_string(data):
    return isinstance(data, (str, bytes))


def main():
    test_list = [1,[2,3,[[4,5],[6,[7],8,[[9,10]]]]]]
    print("Test list is {}".format(test_list))

    print("Flattened list without generator: {}".format(flatten(test_list)))
    new_list = [number for number in flatten_generator(test_list)]
    print("Flattened list with generator: {}".format(new_list))


main()