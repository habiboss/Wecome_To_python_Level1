def power(num, x=1):
    result = 1
    for i in range(x):
        result = result *num

    return result


def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

if __name__ == "__main__":
    #print(power(2))
    #print(power(2,3))
    #print(power(x=3, num=2))
    print(multi_add(1,2,3,4,5,6))
