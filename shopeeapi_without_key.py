import pyshopee
shopid=123456
partnerid=123456
API_key='******'
usr_name=''
pass_word="......"
login_status="离线"
url=''
names=[]
passwords=[]
urls=[]
shopidlist=[]
def shouquan():
    """
    try:
        client1 = pyshopee.Client( 123456, partnerid, API_key )
        resp=client1.public.get_shops_by_partner()
        for shop in resp['authed_shops']:
            for name in names:
                if(name==shop['country']):
                    pass
    except:
    """
    import tkinter as tk
    window=tk.Tk()
    window.title('初次使用授权')
    window.geometry('1000x200')
    text= '点击下方链接进行新用户授权:\n  https://partner.shopeemobile.com/api/v1/shop/auth_partner?id=843417&token=11d41c6380ac0fdb4179b2fcb37f67f4f665aa5d4fb69458a95b061b3d7fe4e0&redirect=https://www.baidu.com'
    url="https://partner.shopeemobile.com/api/v1/shop/auth_partner?id=843417&token=11d41c6380ac0fdb4179b2fcb37f67f4f665aa5d4fb69458a95b061b3d7fe4e0&redirect=https://www.baidu.com"
    def redirect(text,url,parent):
        import tkinter as tk
        import webbrowser
    
        # 设置label标签
        link = tk.Label(window, text=text, font=('Arial', 10))
        link.pack()
        
        # 此处必须注意，绑定的事件函数中必须要包含event参数
        def open_url(event):
            webbrowser.open(url, new=0)
 
        # 绑定label单击时间
        link.bind("<Button-1>", open_url)
    redirect(text,url,window)
   
    e=tk.StringVar()
    shuru= tk.Entry(window,validate='key', textvariable=e, width=50)
    L1 = tk.Label(window, text="请输入最后跳转网址显示的shopid,按回车更新",font = 'Helvetica -20 bold')
    L1.pack()
    shuru.pack()
    def rtnkey(event=None):
        global shopid
        tmp=shopid
        a=e.get()
        shopid=int(e.get())
        print(e.get())
        if(tmp!=shopid):
            #print(shopid,type(shopid)) 
            window.destroy()
    shuru.bind('<Return>', rtnkey)
    shopid=shuru.get()
          
    window.mainloop()
#shouquan()

def getshopid():
    import tkinter as tk
    from tkinter.filedialog import askopenfile,asksaveasfilename
    global names
    global passwords
    global urls
    global shopidlist
    
    def selectPath():
        global shopid
        global accounts
        
       
        file = askopenfile()
        content=file.read()
        accounts=content.split('\n')
        for account in accounts:
            tmp=account.split('----')
            names.append(tmp[0])
            passwords.append(tmp[1])
            urls.append(tmp[2])
            try:
                shopidlist.append(tmp[3])
            except:
                shouquan()
                shopidlist.append(shopid)
                all_the_text=''
                for i in range(len(names)):
                    all_the_text+=names[i]
                    all_the_text+='----'
                    all_the_text+=passwords[i]
                    all_the_text+='----'
                    all_the_text+=urls[i]
                    all_the_text+='----'
                    all_the_text+=str(shopidlist[i])
                    all_the_text+='\n'
                ftypes = [('text file', '.txt'), ('All files', '*')]
                file1= asksaveasfilename(filetypes=ftypes,defaultextension='.txt')
                file_object = open(file1, 'w')
                read_value=file_object.write(all_the_text)
                file_object.close( )
                root.destroy()
    root = tk.Tk()
    file = tk.StringVar()
    tk.Label(root,text = "账户信息文件:").grid(row = 0, column = 0)
    tk.Entry(root, textvariable = file).grid(row = 0, column = 1)
    tk.Button(root, text = "文件选择", command = selectPath).grid(row = 0, column = 2)
    root.mainloop()            
    

#names,passwords,urls,shopidlist=getshopid()
import datetime
import time
def timestamp(timeorigin=datetime.datetime.now().timetuple()):
    #time.struct_time(tm_year=2019, tm_mon=9, tm_mday=2, tm_hour=0, tm_min=33, tm_sec=24, tm_wday=0, tm_yday=245, tm_isdst=-1)
    
    ts=int(time.mktime(timeorigin))
    print(ts)
    return ts
def datetime2timestamp(year,month,date):
  ''' Converts a datetime object to UNIX timestamp in milliseconds. '''
  dt=datetime.datetime(year, month, date)
  if isinstance(dt, datetime.datetime):
    timestamp=int(time.mktime(dt.timetuple()))
    return timestamp
#timestamp=datetime2timestamp(2010, 1, 1)
#print(timestamp)

#https://partner.shopeemobile.com/api/v1/shop/auth_partner?id=843417&token=11d41c6380ac0fdb4179b2fcb37f67f4f665aa5d4fb69458a95b061b3d7fe4e0&redirect=https://www.baidu.com
def ordersn_list(resp):
    tmp=[]
    try:
        tmp.append(resp['orders'][0]['ordersn'])
    except:
        pass
    return tmp
def READY_TO_SHIP(client):
    resp= client.order.get_order_by_status (order_status='READY_TO_SHIP',partner_id=partnerid,shopid=shopid,timestamp=timestamp())
    return resp
"""
for i in range(len(names)):
    usr_name=names[i]
    url=urls[i]
    shopid=int(shopidlist[i])
    client = pyshopee.Client( shopid, partnerid, API_key )
    resp1 = client.order.get_order_by_status (order_status='ALL')
    resp=READY_TO_SHIP(client)
    
    #1566287712=datetime.datetime.strptime('Aug 20, 2019 03:55:12 PM', '%b %d, %Y %I:%M:%S %p').timestamp()
    resp = client.order.get_order_list(create_time_from=1566287712,create_time_to=timestamp(),partner_id=partnerid,shopid=shopid,timestamp=timestamp())
    print("resp",resp)
    respd = client.order.get_order_detail(ordersn_list=ordersn_list(resp),partner_id=partnerid,shopid=shopid,timestamp=timestamp())
    print("detail",respd)
    pass
"""
