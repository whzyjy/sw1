source=input(":")
target=input(":")

with open("c:/data/linetest.txt","r") as f:
    texts=f.read()
with open("c:/data/copylinetest.txt","w") as fp:
    fp.write(texts)

    print(target+"aaa")