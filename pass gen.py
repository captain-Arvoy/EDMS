import random,string
import tkinter as t
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
chng='jkr'
if dat:
    pass
else:
    showwarning("My SQL Database","no table existes thus creating table ")
    
    sql="create table passwords(account_name char(200) unique, passwrd char(200) unique);"
    curso.execute(sql)
siz=random.randint(8,16)
p1=['@','#','!','%','^','*','|','blah','ghusuri']
def men(var=1):
    pop=t.Tk()
    def wd1():
        pop.destroy()
        wd()
    def xd1():
        pop.destroy()
        xd()
    def yd1():
        pop.destroy()
        yd()       
    t.Button(pop,text='Create password',command=wd1,font='Nougat').grid(row=0,column=15,padx=25,pady=7)
    t.Button(pop,text='Delete passwords',command=xd1,font='Nougat').grid(row=1,column=15,padx=25,pady=7)
    t.Button(pop,text='Insert passwords',command=yd1,font='Nougat').grid(row=2,column=15,padx=25,pady=7)
    if var==2:
        t.Button(pop,text='forgot',command=yd1,font='Nougat').grid(row=3,column=15,padx=25,pady=7)
    pop.mainloop()
def fgt():
    global chng
    showinfo('password manager','Enter the Email address')
    eml=input()
    if eml=='sanjaydas740786@gmail.com':
        chng=input('Enter new password')
    else:
        showwarning('Password manager','Wrong password')
        men(var=1)
def zd():
    usr=input('Enter the password: ')
    if usr==chng:
        curso.execute('select * from passwords')
        dat=curso.fetchall()
        for i in dat:
            print(i)
    else:
        showwarning('Password Manager',"Authentication error")
        men(var=2)
def wd():
    global pas,name
    name=input('Enter the account name- ')
    pas=''
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
def xd():
    acntnm=input('Enter the account name: ')
    sql=f"delete from passwords where account_name={acntnm}"
    curso.execute(sql)
    showinfo('Password manager','Password along with the account deleted')
    men()
def yd():
    try:
        acntnm=input('Enter the account name: ')
        pa=input('Enter password for the account: ')
        sql=f"Insert into passwords values('{acntnm}','{pa}')"
        curso.execute(sql)
        showinfo('Password manager','Registered!')
        men()
    except Exception as e:
        showwarning('Password manager',f'{e}')
        men()
pop2=t.Tk()
def wd1():
    pop2.destroy()
    wd()
def xd1():
    pop2.destroy()
    xd()
def yd1():
    pop2.destroy()
    yd()   
def zd1():
    pop2.destroy()
    zd()
t.Button(pop2,text='Create password',command=wd1,font='Nougat').grid(row=0,column=15,padx=25,pady=7)
t.Button(pop2,text='Delete passwords',command=xd1,font='Nougat').grid(row=1,column=15,padx=25,pady=7)
t.Button(pop2,text='Insert passwords',command=yd1,font='Nougat').grid(row=2,column=15,padx=25,pady=7)
t.Button(pop2,text='Check passwords',command=zd1,font='Nougat').grid(row=3,column=15,padx=25,pady=7)
pop2.mainloop()
