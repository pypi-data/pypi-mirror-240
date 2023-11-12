import datetime, os, time; from colorama import *

class Shell():

    """
    # Shell for linux/windows by valahatiy

    ------ contacts:\n
    [+]    discord - teppopuct.ua\n
    [+]    telegram - @guardfsb
    """

    def __init__(self) -> None:
        init(True)

        self.date = datetime.date.today()

        print("\nShell By Valahatiy \nWrite --help before start program for get more info\n")

        while True:
            self.command = input(f'{self.date} | ')

            if self.command == "cls":
                self.cls()

            elif self.command == "install pkg":
                package = input(f'\n{self.date} | {Fore.GREEN}Package Name: {Fore.WHITE}').lower()

                self.pip_install(pkg=package)

            elif self.command == "pkgs":
                self.pkgs()

            elif self.command == "code":
                self.opencode()

            elif self.command == "usr":
                print(f"\n{self.date} | {Fore.GREEN}{self.login()}\n")

            elif self.command == "secret":
                print(f"\n{self.date} | {Fore.GREEN}Infinix note c30\n")

            elif self.command == "exit":
                print(f"\n{self.date} | {Fore.GREEN}Quiting...\n")
                time.sleep(2)

                self.quit()

            else:
                print(f'{self.date} | {Fore.RED}[{self.command}] > Is Invalid Command!')

    def cls(self):
        """
        # By Valahatiy\n
        [+] clearing console
        """
        os.system("cls")

    def pip_install(self, pkg):
        """
        # By Valahatiy\n
        [+] installing pkg with pip3 help
        """
        chose = input(f"{self.date} | {Fore.GREEN}Would You Like Install pkg[{pkg}], (Y/N): {Fore.WHITE}")
        print()

        if chose.lower() == "y":
            os.system(f"python.exe -m pip install {pkg}")
            print(f"\n{self.date} | {Fore.GREEN}Package[{pkg}] Successfuly Downloaded!\n")

        else:
            pass

    def pkgs(self):
        """
        # By Valahatiy\n
        [+] showing all packages from python path
        """
        os.chdir(fr"C:\Users\{os.getlogin()}\AppData\Local\Programs\Python\Python312\Lib\site-packages")
        count = 1

        for pkg in os.listdir():
            print(f"{self.date} | {Fore.GREEN}{count}. Package: {pkg} | Size: {os.path.getsize(pkg)} bytes")
            count += 1

        print(f"{Fore.WHITE}\n{self.date} | {Fore.GREEN}{count - 1} pkgs finded > {count - 1} pkgs active\n{Fore.WHITE}")

    def opencode(self):
        """
        # By Valahatiy\n
        [+] opening vscode.exe
        """
        print(f"\n{self.date} | {Fore.GREEN}Opening...\n")
        os.system("code")

    def login(self) -> os.getlogin():
        """
        # By Valahatiy\n
        [+] returning pc login
        """
        return os.getlogin()
    
    def quit(self):
        """
        # By Valahatiy\n
        [+] close shell
        """
        quit()