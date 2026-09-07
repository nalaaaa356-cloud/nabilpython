number_of_year = int(input("Berapa banyak tahun yang ingin kamu ketahui? "))
year_input = []
for _ in range(0,number_of_year):
  year_input.append(int(input("Masukkan tahun= ")))


for i in year_input:
  if (i % 100 == 0) and (i % 400 == 0):
    res = 'Kabisat'


  elif (i % 100 != 0) and (i % 4 == 0):
    res = 'Kabisat'
    
  else:
    res = 'Bukan Kabisat'


  print(i,res)
