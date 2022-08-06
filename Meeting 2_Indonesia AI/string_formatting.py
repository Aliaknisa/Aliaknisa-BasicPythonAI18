nama = "Andi"
umur = 35

biodata = "nama saya adalah {}, saya berumur {} tahun". format(nama, umur)
biodata_2 = f"nama saya adalah {nama}, saya berumur {umur} tahun"
biodata_3 = "nama saya adalah {0}, saya berumur {1} tahun". format(nama, umur)

print(biodata_3)

# BOOLEANS
x = 9
y = 10
z = 10

print(x > y)
print(x < y)
print(y == z)

# IF ... Else
x = 100
y = 200

if x > y:
    print("x lebih besar dari y")
else:
    print("x lebih kecil dari y")

a = 200
b = 30
if a < b:
    print("a lebih kecil dari b")
elif a == b:
    print("a sama dengan b")
elif a <= b:
    print("a kurang dari sama dengan b")
else:
    print("a lebih besar dari b")

a = 100
b = 200
c = 200
if b == c and a < b:
    print("Ini adalah benar")
else:
    print("Ini adalah salah")

#Ini_kebalikan 
if not a < b: 
    print("a lebih kecil dari b")
else:
    print("Program ini selesai")


# LIST
mylist = [1, 2, 3, 4, 5]
print(mylist)
print(type(mylist))

mylist2 = [1, 'Indonesia', True, 2.0]
mylist2.append(55) # Penambahan Suatu Nilai 
print(mylist2)

