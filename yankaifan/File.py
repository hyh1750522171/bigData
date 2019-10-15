def rA():
    f=open("E:\\时间简史.txt")
    lines=f.readlines()
    for line in lines:
        print(line)
    f.close()
def rB():
    f = open("E:\\时间简史.txt")
    line=f.readline()
    while line:
        print(line)
        line=f.readline()
    f.close()
def rC():
    for line in open("E:\\时间简史.txt"):
        print(line)
if __name__ == '__main__':
    rA()