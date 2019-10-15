L1=[]
def sushu(number):
        for j in range(2,number):             #if 能被2到i-1整除
            if number%j==0:                   #than 不是素数
                print(number,"不是素数",sep='')
                break
        else:
            print(number,"是素数",sep='')
if __name__ == '__main__':
    while True:
        panduan = input("请输入数字：")
        if panduan == "N":
            break
        number=int(panduan)
        sushu(number)
