def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)