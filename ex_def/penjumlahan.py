import operasi_aritmatik as oa



a = input("masukan nilai a: ")
b = input("masukan nilai b: ")
nilai1 = float(a)
nilai2 = float(b)
jumlah = oa.penjumlahan(nilai1,nilai2)

print(f"hasil penjumahan dari {a} dan {b} adalah ",jumlah)
print(oa.penjumlahan(10,11))