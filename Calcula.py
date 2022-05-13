import os

def conversordec(x,y): #Decimal para outras bases
    j = x        #conversor das letras para numeros
    nj = []
    while x > 0:
        d = x // y
        if x%y == 10:
            nj.append('A')
        elif x%y == 11:
            nj.append('B')
        elif x%y == 12:
            nj.append('C')
        elif x%y == 13:
            nj.append('D')
        elif x%y == 14:
            nj.append('E')
        elif x%y == 15:
            nj.append('F')
        else:
            nj.append(x%y)
        x = d
    nj.reverse() 
    print('O número ({}){} na base {} vale: '.format(j, 10, y) + ''.join(map(str,nj))) #printa o resultado

def conversoroutr(x,y,z): #outras bases para decimal
    p = x
    hexa = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10, 'B':11,'C':12,'D':13,'E':14,'F':15}    #Dicionario 
    if y == 16:
        res = 0
        xs = x.upper().strip()
        nd = len(xs) -1
        for digit in xs:
            res += hexa[digit]*16**nd
            nd -= 1
    else:
        n = int(x)
        res = 0
        for m in range(0, z+1):
            i = n
            u = n // 10
            i = i - (u * 10)
            c = i * (y ** m)
            res = res + c
            n = u
    print('O número ({}){} na base {} vale: {}'.format(p, y, 10, res))

while True: #menu
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\nConversor de Bases Numéricas:\n\n[1]Decimal para Outras Bases\n[2]Outras Bases para Decimal\n[0]Sair')
    c = int(input('Digite a função desejada: '))
    if c == 0:
        break
    if c == 1:
        while True: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\nConversor de Bases Numéricas\n\n[1]Decimal para Binário\n[2]Decimal para Octal\n[3]Decimal para Hexadecimal')           
            c = int(input('Digite a função desejada: '))
            if c == 1:
                b = 2
                
            elif c == 2:
                b = 8
            
            elif c == 3:
                b = 16
                
            n = int(input('Digite o número a ser convertido: '))
            conversordec(n, b)
            break
    elif c == 2:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\nConversor de Bases Numéricas\n\n[1]Binário para Decimal\n[2]Octal para Decimal\n[3]Hexadecimal para Decimal') 
            c = int(input('Digite a função desejada: '))
            if c == 1:
                b = 2
            elif c == 2:
                b = 8
            elif c == 3:
                b = 16


            n = input('Digite o número a ser convertido: ')
            t = len(str(n))
            conversoroutr(n, b, t)
            break
    break
    