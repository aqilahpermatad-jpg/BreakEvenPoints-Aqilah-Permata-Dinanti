#Mendefinisikan fungsi (Introduction)

def greet(AqilahPermataDinanti): 
    print(f"Hello, {AqilahPermataDinanti}!")
greet("AqilahPermataDinanti")   

#1. Fungsi Untuk Modularitas

#Contoh Tanpa Fungsi 

print("Luas Persegi")
sisi = 7 
luas = sisi * sisi 
print("luas:", luas)
print("Luas Persegi")
sisi = 9
luas = sisi * sisi
print("luas:", luas)

#contoh dengan fungsi 
def hitung_luas_persegi(sisi): 
    luas = sisi*sisi
    print("Luas:", luas)
print("Luas Persegi") 
hitung_luas_persegi(7)  
print("Luas Persegi")
hitung_luas_persegi(9)

#2 fungsi untuk reusability 
 
def sapa():
    print("selamat datang di bisnis digital")
sapa() 
sapa()
sapa()

def concessions():
    print("Food/Drink Options:")
    print("Popcorn : $9-10")
    print("Candy: $4-5")
    print("Soft Drink :$12-13")

concessions()

#Control Flow With Function 

def park_greet():
    print("Selamat datang, di kebun binatang")
    print("Buka dari pagi hingga sore")
park_greet()

#Arguments dan Parameter 

def greet(Aqilah):
    print("Halo, Aqilah")
greet("Aqilah")

#Contoh Parameter Lebih Dari Satu

def tambah(a, b):
    hasil = a + b 
    print("Hasil:", hasil)
tambah(10, 30)

#Fungsi Dengan List Sebagi Argument
def print_list(items):
    for item in items:
        print(item)
data = ["Aqilah", "Permata","Dinanti"]
print_list(data)

#Mengapa Menggunakan Parameter 
data = [10, 30, 40]
def print_data():
    print(data)

print_data()

#Contoh yang lebih baik 
def print_data(data):
    print(data)
print_data([10,30,50])

#Return

#Fungsi +
def tambah (a,b):
    return a + b 
hasil = tambah(10, 30)
print("Hasil penambahan: ", hasil)

#Fungsi // 

#Menggunakan Fungsi Untuk Membagi Dua Angka
def bagi (a, b):
    if b == 0:
     return a/b
hasil = bagi(10, 40)
print("Hasil pembagian:", hasil)

#Menggunakan Pembagian Dengan Nol 

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol"
    else:
        return a / b

hasil = bagi(15, 0)
print("Hasil pembagian:", hasil)

#Fungsi Di views (Menggunakan Return)

def home(request):
    print("View home dipanggil")
    return render(request, 'home.html')
