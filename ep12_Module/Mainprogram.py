# โปรแกรมหลัก
# หาผลรวมของตัวเลข
def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("ผลบวกมีค่าเท่ากับ = ",total)
    
addition(5,10,20)