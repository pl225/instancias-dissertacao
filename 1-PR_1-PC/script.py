from os import listdir, write
from os.path import isfile, join

mypath = "BC"

for f in listdir(mypath):
    caminho_completo = join(mypath, f)
    if isfile(caminho_completo):
        with open(caminho_completo) as antigo:
            with open("BC_fix/" + f, "w") as novo:
                isReadingTerminals = False
                for line in antigo:
                    if not isReadingTerminals:
                        if not line.startswith("TERMINALS"):
                            novo.write(line)
                        else:
                            novo.write(line)
                            isReadingTerminals = True
                    else:
                        if line[0:-1].isnumeric():
                            novo.write("{0}\n".format(int(line) + 1))
                        else:
                            novo.write(line)
