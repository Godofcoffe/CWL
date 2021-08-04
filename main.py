from os import path, mkdir
from time import sleep
from colorama import init
from src.generator import main
from src.interface.menu import color_text, main_menu
from requests import get
from re import findall

__version__ = "1.0.3"


def choose(valid):
    while True:
        try:
            entry = str(input(valid)).strip().lower()[0]
        except IndexError:
            pass
        else:
            if entry == 'y':
                return True
            elif entry == 'n':
                return False
            else:
                print(color_text('yellow', 'Choose between the two options!'))
                pass


def update():
    try:
        r = get("https://raw.githubusercontent.com/Godofcoffe/CWL/main/main.py")

        remote_version = str(findall('__version__ = "(.*)"', r.text)[0])
        local_version = __version__

        if remote_version != local_version:
            print(color_text('yellow', "Update Available!\n" +
                             f"You are running version {local_version}. Version {remote_version} "
                             f"is available at https://github.com/Godofcoffe/CWL"))
    except Exception as error:
        print(color_text('red', f"A problem occured while checking for an update: {error}"))


# saida de arquivos .txt
OUT_TXT = 'characters.txt'
OUT_NUM = 'numbers.txt'
OUT_WIFI = 'WiFi.txt'
OUT_ROT = 'Router.txt'
folder = 'well/'
init()
if not path.exists(folder):
    mkdir(folder)

while True:
    print(color_text("red", r"""
_________  __      __.____     
\_   ___ \/  \    /  \    |    
/    \  \/\   \/\/   /    |    
\     \____\        /|    |___ 
 \______  / \__/\  / |_______ \
        \/       \/          \/
"""))
    update()
    opc = main_menu(['Standard', 'Wifi'])
    # A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha

    # A opção wifi se aplica a senhas de segurança baixa,
    # como números de telefone ou nomes de pessoas com datas ou números aleátorios.
    # ou quando voce sabe pelo menos um pedaço da senha

    if opc == 1:
        while True:
            symbols = choose(color_text("white", 'Do you want to add symbols? [y/n]: '))
            cap_letters = choose(color_text("white", 'Do you want to add capital letters? [y/n]: '))
            numbers = choose(color_text("white", 'Want it to contain numbers? [y/n]: '))
            print()
            print(color_text("yellow", "Procedures:"))
            print(f"{color_text('green', 'symbols')}: {symbols}")
            print(f"{color_text('green', 'capital letters')}: {cap_letters}")
            print(f"{color_text('green', 'numbers')}: {numbers}")
            print()
            if choose('Continue...? [y/n]: '):
                if symbols and cap_letters and numbers:
                    main(folder + OUT_TXT, uppers=True, numbers=True, symbols=True)

                elif not symbols and not cap_letters and not numbers:
                    main(folder + OUT_TXT)

                elif not symbols and cap_letters and not numbers:
                    main(folder + OUT_TXT, uppers=True)

                elif symbols and not cap_letters and not numbers:
                    main(folder + OUT_TXT, symbols=True)

                elif not symbols and not cap_letters and numbers:
                    main(folder + OUT_TXT, numbers=True)

                elif symbols and cap_letters and not numbers:
                    main(folder + OUT_TXT, symbols=True, uppers=True)
                
                elif symbols and not cap_letters and numbers:
                    main(folder + OUT_TXT, symbols=True, numbers=True)
                break
            else:
                break

    elif opc == 2:
        opc2 = main_menu(['Numbers', 'Keyword', 'Default password'])
        if opc2 == 1:
            main(folder + OUT_NUM, only_num=True)

        elif opc2 == 2:
            selection = choose('Do you want the word to be at the beginning? [y/n]: ')
            name = str(input('What is the word: '))
            print('Spaces will be filled with random characters...')
            sleep(3)
            spaces_num = choose('Do you want spaces to be numbers? [y/n]: ')
            print()
            print(color_text("yellow", "Procedures:"))
            print(f"{color_text('green', 'Word at the beginning')}: {selection}")
            print(f"{color_text('green', 'Word')}: {name}")
            print(f"{color_text('green', 'numbers')}: {spaces_num}")
            print()
            if choose('Continue...? [y/n]: '):
                if selection and spaces_num:
                    main(folder + OUT_WIFI, word=name, position=selection, numbers=spaces_num)
                elif selection and not spaces_num:
                    main(folder + OUT_WIFI, word=name, position=selection)
                elif not selection and spaces_num:
                    main(folder + OUT_WIFI, word=name, numbers=spaces_num)

        elif opc2 == 3:
            # A diferença aqui que em vez de 8 caracteres serão 10.
            # aqui será usado normalmente para roteadores com senhas SSIDs de fabrica
            main(folder + OUT_ROT, limit=10)

        elif opc2 == 4:
            print(color_text('white', 'exiting...'))
            sleep(1)
            break
    elif opc == 3:
        print(color_text('white', 'exiting...'))
        sleep(1)
        break
