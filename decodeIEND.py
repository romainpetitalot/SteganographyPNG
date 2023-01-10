import struct

with open('firstEncoded.png', 'rb') as f:
    signature = f.read(8)

    if signature != b'\x89PNG\r\n\x1a\n':
        print('Not a valid PNG image')
        exit()

    data = f.read()

    newPNG = data[data.index(b"IEND")+8:] # On récupère toutes les données après le chunk IEND

with open('decodedIEND.png', 'wb') as f:
    f.write(newPNG)




