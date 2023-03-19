import sqlite3
from termcolor import colored


class Connect_db:
    def __init__(self):
        self.con = sqlite3.connect("linkedin.db")
        self.cur = self.con.cursor()
       # check if table exists

    def check_credentials(self):
        res = self.cur.execute("SELECT name FROM sqlite_master WHERE name='linkedin'")
        if res.fetchone():
            # print(" table exists")
             # check if there are any emails
            res_mail = self.cur.execute("SELECT email FROM linkedin")
            mail = res_mail.fetchone()

            res_password = self.cur.execute("SELECT password FROM linkedin")

            pass_=res_password.fetchone()

            if mail and pass_:
                print(pass_)

                print('There is an email already')

            return mail[0],pass_[0]

        else:
            self.cur.execute("CREATE TABLE linkedin(email, password,connected_usernames)")

            email = input("Enter your email:")
            password = input("Enter your password:")
            self.cur.execute('insert into linkedin(email,password) values (?,?)', (email, password))
            self.con.commit()

            print(colored('[ ] Saved linked in credentials', "yellow"))


