
#Tao file moi hoac ghi de
f = open("test.txt", 'w') 
f.write("HELLO WORLD\n")
f.write("XIN CHAO MOI NGUOI\n")
f.write("Minh ten la Quan")
f.close()

with open("test.txt", 'w') as f:
    f.write("Hello\n")
    f.write("World\n")

with open("test.txt", 'r') as f:
    conten = f.read()
    print(conten)

with open("test.txt", 'r') as f:
    for line in f:
        print(line.strip())