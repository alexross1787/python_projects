# hello function
def hello():
    print('Hello from inside the file!')

hello()

#pack function 
def pack(a, b, c):
    return [a, b, c]

result = pack(1, 2, 3)
print(result)

# eat_lunch function 
def eat_lunch(list):
    for item in list: 
        if(item == list[0]):
            print(f'First I eat my {item}')
        else:
            print(f'Next I eat my {item}')
    print('My lunchbox is empty')
    
food = ['sandwich', 'apple', 'granola bar']
eat_lunch(food)