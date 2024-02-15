name = input('введить свое імя:')
while True:
   a1 = input('імя:')
   if a1.isalpha():
        break
   else:
        print('помилка')

while True:
   a2 = input('призвище')
   if a2.isalpha():
        break
   else:
       print('помилка')

while True:
   a3 = input('по батькови')
   if a3.isalpha():
        break
   else:
       print('помилка')
print(f"{a2.capitalize()} {a1[0].capitalize()}.{a3[0].title()}.")










































