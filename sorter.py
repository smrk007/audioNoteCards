from os import listdir
from os.path import isfile, join
from os import system
onlyfiles = [f for f in listdir("audioData/") if isfile(join("audioData", f))]

sizes = dict()

for f in onlyfiles:
    new_path = f[:8] + "0"*(17-len(f)) + f[8:]
    system("mv audioData/"+f+" audioData/"+new_path)
