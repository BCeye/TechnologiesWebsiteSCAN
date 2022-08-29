witryna = input('witryna:')
punktypodejrzenia = 0
punktyabsolutne = 0
dodawacz = 1

with open(r'1data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Znaleziono w bazie danych')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Nie znaleziono w 1 bazie danych')

with open(r'2data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Znaleziono w 2 bazie danych')
        punktyabsolutne = punktypodejrzenia + dodawacz

    else:
        print('Nie znaleziono w 2 bazie danch')

with open(r'3data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Znaleziono w 3 bazie danych')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Nie znaleziono w 3 bazie danch')

with open(r'4data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Znaleziono w 4 bazie danych')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Nie znaleziono w 4 bazie danch')

with open(r'5dataCERT.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Znaleziono w 5 bazie danych stworzonej przec CERT')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Nie znaleziono w 5 bazie danch')
print(punktyabsolutne)
if punktypodejrzenia == 0:
    print("Witryna jest bezpieczna")
if punktypodejrzenia == 1:
    print("Witryna jest podejrzana. Zachowaj ostrożnośc")
if punktypodejrzenia == 2:
    print("Witryna jest pojejrzana i niebezpieczna. Nie otwieraj linku oraz zgłoś zdarzenie do CERT Polska")
if punktypodejrzenia == 3:
    print("Witryna jest niebezpieczna. Pod ŻADNYM POZOREM NIE OTWIERAJ LINKU")
if punktypodejrzenia == 4:
    print("Witryna jest silnie niebezpieczna. POD ŻADNYM POZOREM NIE OTWIERAJ LINKU")
if punktypodejrzenia == 5:
    print("Witryna jest bardzo silnie niebezzpieczna. NIE OTWIERAJ LINKU!!")









