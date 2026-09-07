a = float(input("Jarak a= "))
b = float(input("Jarak b= "))
c = float(input("Jarak c= "))


s = (a+b+c)/2


area = (s*(s-a)*(s-b)*(s-c))**0.5


print(f"Luas area segitiga adalah {round(area,2)} satuan unit luas")
