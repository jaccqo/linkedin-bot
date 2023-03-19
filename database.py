import os
import random
import sqlite3
import time

from termcolor import colored
import sys

class ConnectDb:
    def __init__(self):
        self.con = sqlite3.connect("linkedin.db")
        self.cur = self.con.cursor()
        ''' check if table exists '''

    def check_credentials(self):
        res = self.cur.execute("SELECT name FROM sqlite_master WHERE name='linkedin'")
        if res.fetchone():

            '''check if there are any emails'''

            res_mail = self.cur.execute("SELECT email FROM linkedin")
            mail = res_mail.fetchone()

            res_password = self.cur.execute("SELECT password FROM linkedin")

            pass_=res_password.fetchone()

            if mail and pass_:

                return mail[0],pass_[0]

            else:
                print(colored("Delete database and try again","red"))

        else:
            self.cur.execute("CREATE TABLE linkedin(email, password,connected_usernames)")

            email = input("Enter your email:")
            password = input("Enter your password:")
            self.cur.execute('insert into linkedin(email,password) values (?,?)', (email, password))
            self.con.commit()

            print(colored('[ ] Saved linked in credentials', "yellow"))

            return email,password


class Art:
    def __init__(self):
        colors=["red","green","cyan",'yellow',"magenta"]

        art = f'''  
        ┬ ┌┐┬┌┌─┌┬┌┐┌  ┌┐┌─┌┬┐
        │ ││├┴├┤ ││││  ├┴│ ││ 
        ┴─┘└┴ └──┴┘└┘  └─└─┘┴ 
           {time.ctime()}
           < --------------- > code by jack
           '''
        for e in range(10):
            color_picker = colors[random.randrange(len(colors) - 1)]
            sys.stdout.write(colored(fr"{art}",f"{color_picker}"))
            sys.stdout.flush()
            time.sleep(0.5)
            if e<9:
                os.system("cls")



        print("\n\n")

