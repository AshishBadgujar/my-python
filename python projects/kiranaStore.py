# sum=0
# while(True):
#     userInput=input("enter price of item:\n")
#     if(userInput !='q'):
#         sum=sum+int(userInput)
#         print(f"Your total is now:{sum}")
#     else:
#         print(f"your to total is {sum}")
#         print("thanks for  shopping with us...")
#         break





# def function(*args):
#     sum=0
#     for i in args:
#         sum=sum+ i
#     print(f"this is your total: {sum}")

prices=[]
i=0
while(True):
    b=input("enter price of your item: ")
    if(b !='q'):
        prices.append(int(b))
        i=i+1
        print
    else:
        break

# function(*prices)







from functools import reduce

def sum_num(a,b):
    return a+b

lil=reduce(sum_num,prices)
print(f"your total is: {lil}")
