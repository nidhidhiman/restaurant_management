stack = []
def push(stack):
    pushItem = input("Enter the item to be pushed :")
    stack.append(pushItem)
    print("Item Pushed")
    print(stack)
    pass
def pop(stack):
    n = stack[0]
    stack = stack[1:]
    print("Item popped")
    print(stack)
    pass

print("Enter your choice: \n    1. Push\n   2. Pop")
ch = int(input("Enter your Choice:" ))
if ch==1:
    push(stack)
elif ch==2:
    pop(stack)