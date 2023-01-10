# SteganographyPNG - Romain Petitalot & Mamoun Ibn-Abdeljalil

### Ce projet a pour but de faire une démonstration sur des techniques de stéganographie associées aux fichiers PNG


#### Etapes pour encoder les images :
1 - $ python3 encodeITI.py

Ce script utilise les images ./imageSource/third.png et ./imageSource/second.png et cache l'image third.png dans un des chunks de second.png en créant l'image ./imageSource/secondEncoded.png


2 - $ python3 encodeIEND.py

Ce script utilise les images ./imageSource/first.png et ./imageSource/secondEncoded.png et cache l'image secondEncoded.png à la suite de first.png en créant l'image firstEncoded.png

Finalement, on aura third.png cachée dans second.png qui elle-même est caché dans first.png

#### Etapes pour décoder les images :
1 - $ python3 decodeIEND.py

Ce script utilise l'image ./firstEncoded.png et récupère toutes les données après le chunk IEND pour créer l'image decodedIEND.png

2 - $ python3 decodeChunkITI.py

Ce script utilise l'image ./decodedIEND.png et récupère les données du chunk itiZ pour créer l'image itiDecoded.png

Finalement, à partir d'un seul fichier PNG on peut extraire deux nouveaux fichiers PNG
