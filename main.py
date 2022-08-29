witryna = input('witryna:')
punktypodejrzenia = 0
punktyabsolutne = 0
dodawacz = 1

with open(r'1data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Website marked as Suspicious')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Not Found')

with open(r'2data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Websie marked as Suspicious')
        punktyabsolutne = punktypodejrzenia + dodawacz

    else:
        print('Not found')

with open(r'3data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Website marked as Suspicious')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Not found')

with open(r'4data.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Website marked as Suspicious')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Not found')

with open(r'5dataCERT.txt', 'r') as file:
    # read all content from a file using read()
    content = file.read()
    # check if string present or not
    if witryna in content:
        print('Website marked as Suspicious')
        punktyabsolutne = punktypodejrzenia + dodawacz
    else:
        print('Not found')








