with open('./imageSource/third.png', 'rb') as f:
    data = f.read()

dataChunk = data.replace(b"\x89PNG\x0d\x0a\x1a\x0a", b"itiZ")


with open('./imageSource/second.png', 'rb') as f:
    dataGood = f.read()


print(len(dataChunk)) 

print(hex(len(dataChunk))) 

#On prend la taille en hexa de dataChunk à laquelle on enlève les 4 octets du crc qui n'est pas compté dans les datas
new = b"\x00\x0c\xbc\xdb" + dataChunk

new += b"\xc4\x82\xb3\x35" # il faut rajouter 4 octets à la fin qui font office de crc, pour garder le bon format des chunks
#On n'est pas obligé de mettre un crc valide car l'afficheur de l'image ne connaissant pas le chunk itiZ il va skip le nombre d'octets indiqué dans les infos du chunk


with open('./imageSource/secondEncoded.png', 'wb') as f:
    f.write(dataGood[:0x5af] + new + dataGood[0x5af:])
# On insert le chunk itiZ à l'offset 0x5af qui correspond à la suite du chunk tEXt

