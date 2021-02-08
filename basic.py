l=[]
def push(elem):
    l.append(elem)
def pop():
    l.pop()

def printStack():
    for i in l:
        print(i)

def start():

    print("Enter your Choice")

    while(True):
        ch = int(input("1- Push \n 2-POp \n 3-Print \n 4- Exit"))
        if(ch==1):
            push(input("Enter number \n"))
        elif(ch==2):
            pop()
        elif(ch==3):
            printStack()
        elif(ch==4):
            break





start()