# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal;

import os
from time import sleep

print('=' * 5, ' ' * 4, 'Conversion Base', ' ' * 4, '=' * 5)

#Home Menu

def menu():
    print("""\
Welcome to the program that performs conversion bases!!""")

    continua = input('\nPress Enter to continue')

    valor_menu = int(input('\nEnter the numer you want to convert: '))

    opcao_menu = int(input("""\
\n(1) for Binary
(2) for Octal
(3) for Hexadecimal

Select conversion option: """))
    return converter(opcao_menu, valor_menu)

# Converter

def converter(opcao_menu, valor_menu):
    conversoes_loop = 0
    while (conversoes_loop <= 0):

        if opcao_menu == 1:
            print('\n{} converted to Binary corresponds to {}'.format(valor_menu, bin(valor_menu)[2:]))
            continuar = int(input("""\n
Want to perform a new conversion?

(1) Yes
(2) No
Select: """))
            if continuar == 1:
                os.system('cls')
                sleep(0.5)
                menu()
            elif continuar == 2:
                print('Thanks for using the converter!')
                encerrar = input('Press ENTER to close...')
                sleep(0.5)
                conversoes_loop += 1

        elif opcao_menu == 2:
            print('\n{} converted to Octal corresponds to {}'.format(valor_menu, oct(valor_menu)[2:]))
            continuar = int(input("""\
Want to perform a new conversion?

(1) Yes
(2) No
Select: """))
            if continuar == 1:
                os.system('cls')
                sleep(0.5)
                menu()
            elif continuar == 2:
                print('Thanks for using the converter!')
                encerrar = input('Press ENTER to close...')
                sleep(0.5)
                conversoes_loop += 1

        elif opcao_menu == 3:
            print('\n{} converted to Hexadecimal corresponds to {}'.format(valor_menu, hex(valor_menu)[2:]))

            continuar = int(input("""\
Want to perform a new conversion?

(1) Yes
(2) No
Select: """))
            if continuar == 1:
                os.system('cls')
                sleep(0.5)
                menu()
            elif continuar == 2:
                print('Thanks for using the converter!')
                encerrar = input('Press ENTER to close...')
                sleep(0.5)
                conversoes_loop +=1

        elif opcao_menu != 1 and opcao_menu != 2 and opcao_menu != 3:
            print('\nYou selected an invalid option!')
            retornar_ao_menu = input('\nPress ENTER to reset the program')
            os.system('cls')
            sleep(0.5)
            return menu()
    conversoes_loop += 1


if __name__ == '__main__':
    menu()
