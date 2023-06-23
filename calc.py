def sum(*args):
    total = 0
    for number in args:
        total += number
    return total   

def multiply(*args):
    # if args.len() == 0:
    #     return 0
    total = 1
    for number in args:
        total *= number
    return total  
