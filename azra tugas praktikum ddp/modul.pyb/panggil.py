import bangunRuang as br
import bangundatar as bd

print("~~~~ BANGUN RUANG ~~~~~")
print(f"Volume Kubus: {br.kubus(3)}")
print(f"Volume Balok: {br.balok(4,5,2)}")
print(f"Volume Prisma: {br.prisma(4,2,6)}")
print(f"Volume Tabung: {br.tabung(3,7)}")
print(f"Volume Kerucut: {br.kerucut(3.14,3,7)}")

print("\n~~~~ BANGUN DATAR ~~~~")
print(f"Luas Persegi: {bd.persegi(4)}")
print(f"Luas Persegi Panjang: {bd.persegi_panjang(4,6)}")
print(f"Luas Segitiga: {bd.segitiga(4,5)}")
print(f"Luas Lingkaran: {bd.lingkaran(7)}")
print(f"Luas Jajargenjang: {bd.jajargenjang(4,7)}")
