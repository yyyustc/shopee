from function import *
from gui import *
import multiprocessing
from time import *
from shopeeapi import *
multiprocessing.freeze_support()
p2 = multiprocessing.Process(target = function2,args=(names,passwords,urls,shopidlist))
p3 = multiprocessing.Process(target = function6,args=(names,passwords,urls,shopidlist))
p4 = multiprocessing.Process(target = function3,args=(names,passwords,urls,shopidlist))
p5 = multiprocessing.Process(target = function1,args=(names,passwords,urls,shopidlist))
p6 = multiprocessing.Process(target = function4,args=(names,passwords,urls,shopidlist))
def mulfunction2(): 
    global p2
    p2.start()
def mulfunction3(): 
    global p3
    p3.start()

def mulfunction4(): 
   global p4
   p4.start()

def mulfunction5(): 
    global p5
    p5.start()

def mulfunction6(): 
    global p6
    p6.start()
if __name__ == "__main__":


    usr_name=''
    pass_word="......"
    login_status="离线"
    url=''
    names=[]
    passwords=[]
    urls=[]
    shopidlist=[]
    names=multiprocessing.Manager().list()
    passwords=multiprocessing.Manager().list()
    urls=multiprocessing.Manager().list()
    shopidlist=multiprocessing.Manager().list()
   
    #freeze_support()
    import login
    from tkinter import *
    t = multiprocessing.Process(target=login.main_login,args=(names,passwords,urls,shopidlist))
    
    # 守护进程必须在开启子进程前开启
    
    t.start()

       



     


    



 


