from colorama import Fore
from anonfile import AnonFile
from pathlib import Path
anon = AnonFile()
import sys
print(Fore.BLUE +"""
 ▄▄▄    ██▒   █▓ ▄▄▄       ██▓    ▄▄▄       ███▄    █  ▄████▄   ██░ ██ ▓█████ 
▒████▄ ▓██░   █▒▒████▄    ▓██▒   ▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ 
▒██  ▀█▄▓██  █▒░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒██▀▀██░▒███   
░██▄▄▄▄██▒██ █░░░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ 
 ▓█   ▓██▒▒▀█░   ▓█   ▓██▒░██████▒▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░▓█▒░██▓░▒████▒
 ▒▒   ▓▒█░░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░
  ▒   ▒▒ ░░ ░░    ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░
  ░   ▒     ░░    ░   ▒     ░ ░    ░   ▒      ░   ░ ░ ░         ░  ░░ ░   ░   
      ░  ░   ░        ░  ░    ░  ░     ░  ░         ░ ░ ░       ░  ░  ░   ░  ░                    
                                                                    -Vulcain""")

print(Fore.BLUE+'''                            Que voulez vous faire ? \n
                           [1]Upload Vers Anonfile \n
                           [2]Télécharger Via Anonfiles\n''')


user = input(Fore.BLUE + "Option [1/2]: ")

if user == '1':
    pass
    path = input(Fore.RED + "Entrez le chemin d'accès au fichier: ")
    up = input(Fore.RED + "Voulez vous l'upload maintenant ? [Y/n]")
    if 'Y' in up:
        pass
    elif 'n'in up:
        print(Fore.BLUE+"Programme terminé par l'utilisateur")
        sys.exit()
    else:
        print(Fore.RED + "Entrée invalide.")
        sys.exit()
    upload = anon.upload(path, progressbar=True)
    print(upload.url.geturl())
elif user == "2":
    pass
    target_dir = Path.home().joinpath('Downloads')
    link = input("Entrez le lien du fichier: ")
    filename = anon.download(link, path=target_dir)
    print(filename)
else:
    sys.exit()

