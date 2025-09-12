def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    if x < y and y > z:
        return y
    elif y < x and x > z:
        return x
    elif x < z and z > y:
        return z

