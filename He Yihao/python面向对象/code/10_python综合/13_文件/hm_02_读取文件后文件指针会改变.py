# 1. 打开文件
file = open("README")

# 2. 读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

text = file.read()
print(text)
print(len(text))

# 3. 关闭文件
file.close()
