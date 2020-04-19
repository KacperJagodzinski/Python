number = int(input('Podaj liczbe\n'))
if number < 2:
  print("Liczba nie jest liczba pierwsza")
else:
  for i in range (2,number//2):
    if(number % i == 0):
      print("Liczba nie jest liczba pierwsza")
      break
    else:
      print("Liczba jest liczba pierwsza")
