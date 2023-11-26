# Create a decorator
def sample_decorator(func):
    # define the inner function 
    def example_function(number):
        print("Before Funciton Call:", func.__name__)
        
        # call original function
        results = func(number)
        print("Cube: ", results)
     
        print("After Funciton Call:", func.__name__)
    # Return inner function
    return example_function

def cube(num):
    return num**3

# decorate the function
decorated_func = sample_decorator(cube)

# call the decorated function
decorated_func(2)