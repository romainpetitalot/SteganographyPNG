import struct

with open('decodedIEND.png', 'rb') as f:
    signature = f.read(8)

    if signature != b'\x89PNG\r\n\x1a\n':
        print('Not a valid PNG image')
        exit()

    newPNG = signature # On initialise la variable qui va stocké les datas de l'image par la signature

    # On itère à travers tous les chunk et on récupère les données du chunk itiZ
    while True:
        chunk_length_bytes = f.read(4)
        chunk_type = f.read(4)

        if chunk_length_bytes == b'':
            break

        chunk_length = struct.unpack('>i', chunk_length_bytes)[0]

        chunk_data = f.read(chunk_length)

        chunk_crc = f.read(4)

        if chunk_type == b"itiZ": # On recupère les données du chunk itiZ
            newPNG += chunk_data


with open('itiDecoded.png', 'wb') as f:
    f.write(newPNG)

