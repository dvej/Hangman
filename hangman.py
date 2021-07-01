
def grafika(pok,odg):
    print('za izlaz - kraj\n')
    stub = '  ||   '
    print('  ' + 8*'_')
    print(stub + '  |  ' + odg)
    print(stub + '  |',end='')
    if pok > 0: print(' /',end='')
    print('\n' + stub,end='')
    if pok > 0: print('  ' + 'O',end='')
    print('\n' + stub,end='')
    if pok == 2: print('  ' + '|',end='')
    if pok > 2:
        print(' ' + '/|',end='')
        if pok > 3: print('\ ',end='')
    print('\n' + stub,end='')
    if pok > 4:
        print('_/',end='')
        if pok > 5: print(' \_',end='')
    print('\n__||' + 10*'_',end='   ')


def besenje(neka_rec,gov):
    rec = (neka_rec).upper()
    prom,zivot = 0,6
    slova = []
    govor = gov['title']
    b = random.randint(1,3)
    while prom != zivot:
        pobeda = True
        for slov in rec[1:-1]:
            if slov not in slova and slov.isalpha():
                pobeda = False
        if pobeda:
            clear()
            grafika(prom,gov[f'win{b}'])
            return print(rec)
        clear()
        grafika(prom,govor)
        print(rec[0],end='')
        for slovo in rec[1:-1]:
            if slovo.isalpha() and (slovo not in slova):
                print('.',end='')
            else:
                print(slovo,end='')
        print(rec[-1])
        for element in slova:
            print(element.lower(),end=' ')
        s = input('\n' + 10*' ' + 'Slovo: ').upper()
        if s == 'KRAJ': exit()
        print()
        if (len(s) != 1) or (s.isalpha() == False):
            govor = gov['wrong']
        elif s in slova:
            govor = gov['letter']
        else:        
            slova.append(s)
            if s not in rec[1:-1]:
                prom += 1
                for i in range(1,6):
                    if prom == i:
                        govor = gov[f'miss{i}{b}']
        print()
    clear()
    grafika(prom,gov[f'end{b}'])
    print(rec)


govor = {'title':'<<<<< BEŠENJE >>>>>',
         'win1':'Konačno i ja da imam sreće',
         'win2':'Hvala nebesima!',
         'win3':'Lepo sam rekao',
         'letter':'Alooo, to slovo je bilo!',
         'wrong':'Nisi uneo slovo bre',
         'end1':'Ti si bolesnikkKRKLJJJJJ',
         'end2':'Ne mogu da veruj...GNHHHH',
         'end3':'Ovo nije istin..ARGHHHH',
         'miss11':'Šta je ovo??',
         'miss12':'Gde sam to?',
         'miss13':'Hej!',
         'miss21':'Ovo mi deluje nešto poznato',
         'miss22':'Da li je ovo Deja Vu?',
         'miss23':'Ma ovo nije ništa',
         'miss31':'Sad se sećam!',
         'miss32':'O neeee!',
         'miss33':'Smešno, evo smejem se: hahaha',
         'miss41':'Pomozi mi!',
         'miss42':'Milost!',
         'miss43':'To nema šanse meni da se desi',
         'miss51':'Šta samo sediš i gledaš?!!',
         'miss52':'Za sve je kriv Šomi!',
         'miss53':'Ja sam neustrašiv!'}

import random,os
clear = lambda: os.system('cls')
with open('recnik.txt', encoding="utf8") as f:
    redovi = f.readlines()
while True:
    word = random.choice(redovi).strip()
    besenje(word,govor)
    while True:
        game = (input('Nova igra? (da/ne) ')).lower()
        if game == 'da': break
        if game in ['ne','kraj']: exit()
