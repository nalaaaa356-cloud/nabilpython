import pandas as pd

vowels = 'aeiou'


ip_str = str(input("Masukkan sebuah kalimat: "))


ip_str = ip_str.casefold()


count = {}.fromkeys(vowels,0)


for char in ip_str:
   if char in count:
       count[char] += 1


count_table = pd.DataFrame(count, index=['Jumlah'])
print(count_table)
