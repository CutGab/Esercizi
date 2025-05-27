def outer_function (a:int, b: int):

    return inner(a,b) + 5

def inner(a:int, b:int):
    return a + b

print(outer_function(10,5))

    
    