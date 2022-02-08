import random,string
from tkinter.messagebox import showinfo, showwarning
import mysql.connector as c
u='test'
pa='12345678'
con=c.connect(host='localhost',user='root',password=f'{pa}',database=f'{u}',autocommit=True)# trouble shoot the executable version
curso=con.cursor()
if con.is_connected():
   print('successfully connected')
else:
   print('not connected')
sql="show tables like 'passwords'"
curso.execute(sql)
dat=curso.fetchone()
if dat:
    pass
else:
    showwarning("My SQL Database","no table existes thus creating table ")
    
    sql="create table passwords(account_name char(200) unique, passwrd char(200) unique);"
    curso.execute(sql)
siz=random.randint(8,16)
p1=['@','#','!','%','^','*','|','blah','ghusuri']
name=input('Enter the account name- ')
pas=''
def wd():
    global pas,name
    p=string.punctuation
    feed='y'
    while feed=='y' and len(pas)<17:
        #algorithm to generate password
        for i in range(siz):
            if i%2==0:
                pas=pas+random.choice(p)
            a=random.randint(65,119)
            pas=pas+chr(a)
        #end of algorithm
        passql=f"insert into passwords values('{name}','{pas}')"
        print('Password',pas)
        confir=input()
        if confir=='ok':
            try:
                curso.execute(passql)
                showinfo('Password manager','Successfully created')
            except Exception as e:
                showwarning('My SQL database',f'warning: {e}')
                pro=input('Procced?[y/n/change account name]\n')
                if pro=='change account name':
                    name=input('Enter account name: ')
                    wd()
                if pro=='no problem' or pro=='ignore' or pro=='ok' or pro=='proceed' or pro=='yes'or pro=='y':
                    pass
                else:
                    pas=''
                    print('Regenerating....\n')
                    wd()
            else:
                feed='n'
            finally:
                pas=''
        else:
            pas=''
            print('---------------O--------------\n')
    else:
        con.close()
wd()