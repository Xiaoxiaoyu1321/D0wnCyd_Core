path = "Packages"
with open(path,'r',encoding="utf-8",newline="\n") as f:
    filea = f.read()

fileb = filea.split("\n")

time = 0
while time < len(fileb):
    filec = fileb[time].split(":")
    if filec[0] == "Name":
        print(filec[1])
    
    time = time + 1
    
