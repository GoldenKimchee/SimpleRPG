import engine

"""In parameters with default arguments, if it is a mutable type, any change 
imposed on it will stay even in next function call"""
# using immutable type, int
def something(number: int, appending = 10):
    appending += number
    return appending

# using mutable type, list
def something_array(number: int, appending = []):
    appending.append(number)
    return appending

# using mutable type, dictionary
def something_dict(number: int, sentence: str, appending: dict = {}):
    appending[sentence] = number
    return appending

print(something(10))
print(something(5))
print()
print(something_array(9))
print(something_array(1))
print()
print(something_dict(7, "my fav"))
print(something_dict(13, "unlucky"))