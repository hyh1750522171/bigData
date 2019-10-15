file = open("README")

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    print(text)

file.close()
