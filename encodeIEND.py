
with open('./imageSource/first.png', 'rb') as f:
    data1 = f.read()

with open('./imageSource/secondEncoded.png', 'rb') as f:
    data2 = f.read()




with open('firstEncoded.png', 'wb') as f:
    f.write(data1+data2)