import math
def get_delta(start, stop, n):
    return (stop-start)/n

def get_params(start, stop, n):
    delta = get_delta(start, stop, n)
    p_list= [start]
    for x in range(n):
        new_elem = p_list[-1] + delta
        p_list.append(new_elem)
    return p_list

def get_fx_list(start, stop, n, the_func):
    input_list = get_params(start, stop, n)
    fx_list = []
    for e in input_list:
        fx = the_func(e)
        fx_list.append(fx)
    return fx_list


def get_res_trapezium(upper, lower, n, a_func):
    delta = get_delta(upper, lower, n)
    fx_list = get_fx_list(upper, lower, n, a_func)
    agg = 0
    tracker = 0
    for e in fx_list:
        if tracker == 0:
            agg = agg+1/2*e
        elif tracker == len(fx_list)-1:
            agg = agg+1/2*e
        else:
            agg = agg + e
        tracker = tracker + 1
    return agg*delta

def get_res_simpson(upper, lower, n, a_func):
    if n%2 != 0:
        return 'simpson rule requires an even interval'
    delta = get_delta(upper, lower, n)
    fx_list = get_fx_list(upper, lower, n, a_func)
    agg = 0
    tracker = 0
    for e in fx_list:
        if tracker == 0:
            agg = agg + e
        elif tracker == len(fx_list)-1:
            agg = agg + e
        elif tracker%2 == 0:
            agg = agg + 2 * e
        else:
            agg = agg + 4 * e
        tracker = tracker + 1
    return agg*(delta/3)

def my_func(i):
    return math.log(i, math.e)

print(get_fx_list(1,4,6, my_func))
print(get_res_trapezium(1,4,6, my_func))
print(get_res_simpson(1,4,6, my_func))