dictionary = {'hello': 'cześć','goodbye':'do widzenia'}
word = input('Podaj wyraz\n')
if dictionary.__contains__(word):
  print(dictionary[word])
else:
  print("Nie znam tego slowa")

if word in dictionary:
  print(dictionary[word])
else:
  print("Nie ma")
