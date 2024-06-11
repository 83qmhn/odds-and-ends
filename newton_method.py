def newton_method(x):
    '''a function implements Newton's method'''
    var = x- ( (pow(x, 3) - pow(x, 2) - 1)/(3*pow(x, 2) - 2*x))
    if abs(var - x) < 0.00001:
        return var
    print(var)
    return newton_method(var)
print(newton_method(1))
