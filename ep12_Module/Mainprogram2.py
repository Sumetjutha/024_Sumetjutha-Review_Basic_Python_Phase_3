def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("ผลบวกมีค่าเท่ากับ = ",total)
    
def subtraction(num1,num2):
    print("ผลลบมีค่าเท่ากับ = ", (num1 - num2))
    
addition(40,50,60)