f=open("pawan.txt")
# print(f.tell()) #tell us cursor location
print(f.readline())
f.seek(10) #to move cursor on position
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()