from os import listdir, write
from os.path import isfile, join
import sys

mypath = sys.argv[1]

for f in listdir(mypath):
    caminho_completo = join(mypath, f)
    if isfile(caminho_completo):
        with open(caminho_completo) as antigo:
            for line in antigo:
                if line.startswith("NB_BLOCKAGES"):
                    print("{0},{1}".format(f, line.split(" ")[1].replace('\n', '')))
                    break
                
