with open("test.txt", mode='r') as f:
    f.seek(3, 0)
    content = f.read()
print(content)
