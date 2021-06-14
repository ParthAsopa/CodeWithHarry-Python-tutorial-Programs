print('Weight converter')
print("Type 'help' to know instructions.")
command= ''
mass= ''
Unit= ''
while True:
    command= input('> ').lower()
    if command=='help':
        print('''Type:
convert: to convert your mass from kgs to lbs and vice versa
        (You have to type convert every next time you want to convert your mass).
quit: to quit/exit''')
    if command=='convert':
        mass= input('Enter your weight(only number): ')
        Unit= input('Unit - (L)bs or (K)g: ').upper()#
        if '.' in mass:
            mass= float(mass)
        else:
            mass= int(mass)
        if Unit == 'K':
            mass_in_lbs = mass * 2.205
            print(f'You are {mass_in_lbs}lbs.')
        elif Unit == 'L':
            mass_in_kg = mass / 2.205
            print(f'You are {mass_in_kg}kg.')
    if command=='quit':
        print('Good byeee!!!')
        break