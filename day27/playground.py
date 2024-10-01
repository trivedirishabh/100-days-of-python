# *arg argument

def add (*args):
    count = 0
    for number in args:
        count += number
    return count

print(add(4,5,6,7,8))

# keyword arguments
