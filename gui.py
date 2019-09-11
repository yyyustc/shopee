# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from time import *
from function import *
from PIL import Image
from PIL import ImageTk
insert_lock=0#为0insert
screen_width=1920
screen_height=1080
def main():
    global names,passwords,urls,shopidlist
    from multi import mulfunction2,mulfunction3,mulfunction4,mulfunction5,mulfunction6
    window=Tk()
    window.title("店铺管理系统")
    #window_width = screen_width * 0.8
    #window_height = screen_height *0.8
    #window.geometry("%dx%d" % (window_width, window_height))
    # w = window.winfo_screenwidth()
    #h = window.winfo_screenheight()
    #window.geome  1try("%dx%d" %(w, h))
    
 
    # 第5步，在窗口界面设置放置Button按键
    p1=Image.open("p\\店铺登陆1.jpg")
    p1 = ImageTk.PhotoImage(p1)
    
    
    p2=Image.open("p\\待发货订单1.jpg")
    p2 = ImageTk.PhotoImage(p2)

    p3=Image.open("p\\运送中订单1.jpg")
    p3 = ImageTk.PhotoImage(p3)

    p4=Image.open("p\\订单利润1.jpg")
    p4 = ImageTk.PhotoImage(p4)

    p5=Image.open("p\\产品数量1.jpg")
    p5 = ImageTk.PhotoImage(p5)
    
    p6=Image.open("p\\产品成本1.jpg")
    p6 = ImageTk.PhotoImage(p6)
   
    
    b1 = tk.Button(window,image=p1, width=150, height=150, command=function5)
    b1.grid(column=0,row=0)
    Label(window,text='店铺基本数据').grid(column=0,row=1)
    
    b2 = tk.Button(window, image=p2, width=150, height=150, command=mulfunction2)
    b2.grid(column=1,row=0)
    Label(window,text='待发货订单').grid(column=1,row=1)
    
    b3 = tk.Button(window, image=p3, width=150, height=150, command=mulfunction3)
    b3.grid(column=2,row=0)
    Label(window,text='运送中订单').grid(column=2,row=1)

    
    b4= tk.Button(window, image=p4, width=150, height=150, command=mulfunction4)
    b4.grid(column=3,row=0)
    Label(window,text='店铺财务数据明细').grid(column=3,row=1)
    
    b5= tk.Button(window, image=p5, width=150, height=150,command=mulfunction5)
    b5.grid(column=4,row=0)
    Label(window,text='店铺经营统计').grid(column=4,row=1)
    
    
    b6 = tk.Button(window, image=p6, width=150, height=150, command=mulfunction6)
    b6.grid(column=5,row=0)
    Label(window,text='采购及配货汇总').grid(column=5,row=1)

    b7 = tk.Button(window, text='点击导入账号', command=loadaccount)
    b7.grid(column=0,row=2)
    tree=ttk.Treeview(window)#表格
    tree["columns"]=("2","3","4","5","6","7","8",'9','10','11','12','13','14','15','16','17','18','19','20','21','22')
    #表示列,不显示
    tree.column('#0',width=100,anchor='w')
    tree.column("2",width=30)
    tree.column("3",width=50)
    tree.column("4",width=50)   #表示列,不显示
    tree.column("5",width=60)
    tree.column("6",width=80)   #表示列,不显示
    tree.column("7",width=100)
    tree.column("8",width=60)
    tree.column("9",width=60)   #表示列,不显示
    tree.column("10",width=60)

    tree.column("11",width=50)   #表示列,不显示
    tree.column("12",width=60)
    tree.column("13",width=60)
    tree.column("14",width=60)   #表示列,不显示
    tree.column("15",width=60)
    tree.column("16",width=50)   #表示列,不显示
    tree.column("17",width=50)
    tree.column("18",width=80)
    tree.column("19",width=60)   #表示列,不显示
    tree.column("20",width=60)

    tree.column("21",width=80)   #表示列,不显示
    tree.column("22",width=80)
    
     
    tree.heading("#0",text="国家/地区")  #显示表头
    tree.heading("2",text="No.")
    tree.heading("3",text="用户名")
    tree.heading("4",text="密码")
    tree.heading("7",text="站点网址")
    tree.heading("5",text="登录状态")
    tree.heading("6",text="店铺ID")  #显示表头
    tree.heading("8",text="产品数量")
    tree.heading("9",text="粉丝数量")
    tree.heading("10",text="关注数量")

    tree.heading("11",text="店铺名")
    tree.heading("12",text="账户余额")
    tree.heading("13",text="店铺评价")
    tree.heading("14",text="惩罚计分")  #显示表头
    tree.heading("15",text="浏览量")
    tree.heading("16",text="访客量")
    tree.heading("17",text="订单量")

    tree.heading("18",text="已下单金额")
    tree.heading("19",text="客单价")
    tree.heading("20",text="转化率")
    tree.heading("21",text="数据开始时间")  #显示表头
    tree.heading("22",text="数据截止时间")
    entryedit1 = Text(window,width=40,height = 1)
    entryedit1.grid(column=2,row=2,columnspan=2)
    entryedit2 = Text(window,width=40,height = 1)
    entryedit2.grid(column=2,row=3,columnspan=2)
    import datetime
    todate=datetime.datetime.now()
    fromdate=datetime.datetime.now()-datetime.timedelta(days=15)
    fromts=datetime2timestamp(fromdate.year,fromdate.month,fromdate.day)
    tots=datetime2timestamp(todate.year,todate.month,todate.day)
    def saveedit():
        
        nonlocal fromdate,todate,fromts,tots
        try:
            if(entryedit1.get(0.0, "end")!=None):
                value=entryedit1.get(0.0, "end")
                fromdate=value.strip().split('-')
                fromts=datetime2timestamp(int(fromdate[0]),int(fromdate[1]),int(fromdate[2]))
            if(entryedit2.get(0.0, "end")!=None):
                value=entryedit2.get(0.0, "end")
                todate=value.strip().split('-')
                tots=datetime2timestamp(todate[0],todate[1],todate[2])
        except:
            pass
    stb1 = ttk.Button(window, text='按年-月-日设置开始时间，如2018-09-22', width=50, command=saveedit)
    stb1.grid(column=4,row=2,columnspan=2)
    stb2 = ttk.Button(window, text='按年-月-日设置结束时间，如2018-09-22', width=50, command=saveedit)
    stb2.grid(column=4,row=3,columnspan=2)
    Label(window,text='开始时间与结束时间不能大于15天\n一分钟更新一次').grid(column=1,row=3)
    class Timer:
        def __init__(self, parent):
            

#
            '''
            zhan = ['1','马来-01','马来-02']
            num= ['01','01','01']
            qu=['A','A','a']
            for i in range(len(num)):# 写入数
            '''
            #p=Image.open("i\\fei.jpg")
            # p = ImageTk.PhotoImage(p)
            #tree.insert('','end',image=p,value=('1','2','3'))
            #tree.insert('','end',value=('5','6','7'))
            tree.grid(columnspan=6)
            # start the timer
            tree.after(1000, self.refresh_data)

        def refresh_data(self):
            """ refresh the content of the label every second """
            data=[]
            datas=[]
            resp1={}
            resp2={}

            def get_datas(datas):
                nonlocal data
                i=0
                #import datetime
                #global starttime
                #starttime = datetime.datetime.now()
                #no
                if len(shopidlist)==0:
                    pass
                else:
                 print (shopidlist)
                 for shopid in shopidlist:
                    tmp='{:02}'.format(i+1)
                    data.append(tmp)
                    data.append(names[i])
                    data.append("******")
                    
                    shopid=int(shopidlist[i])
                    client = pyshopee.Client( shopid, partnerid, API_key )
                    #tmp=client.public.get_shops_by_partner(partnerid=partnerid)
                    #print("\n",i,'\n')
                    url=urls[i]
                    connectlock=1
                    try:
                        resp1=client.shop.performance()
                        resp2=client.shop.get_shop_info()
                        connectlock=0
                    except:
                        print("程序报错")
                        try:
                            resp1=client.shop.performance()
                            resp2=client.shop.get_shop_info()
                        except:
                            connectlock=0
                    if('error' in resp1 or connectlock==1):
                      data.append("失败")
                    else:
                      data.append("成功")
                    connectlock=1
                    data.append(shopid)
                    data.append(urls[i])
                    data.append('暂缺')#产品数量	
                    data.append('暂缺')#粉丝数量
                    data.append('暂缺')#关注数量
                    data.append(resp2['shop_name'])
                    data.append('暂缺')#账户余额
                    data.append(resp1['overall_review_rating']['my'])
                    data.append('暂缺')#惩罚计分
                    data.append('暂缺')#浏览量	
                    data.append('暂缺')#访客量	
                    data.append('暂缺')#订单量	
                    data.append('暂缺')#已下单金额	
                    data.append('暂缺')#客单价	
                    data.append('暂缺')#转化率
                    #2010年1月1日时间戳1262275200
                    if(fromts<1262275200 or tots<1262275200):
                        data.append('暂缺')#数据开始时间	
                        data.append('暂缺')#数据截止时间
                    elif(fromts>=tots):
                        data.append('开始时间应')#数据开始时间	
                        data.append('早于截止时间')#数据截止时间
                    elif(tots-fromts>1296000):#不能大于15天
                        data.append('开始时间应')#数据开始时间	
                        data.append('早于截止时间')#数据截止时间
                    else:
                        import datetime
                        if(not isinstance(fromdate,list)):
                            data.append(str(fromdate)[:10])
                        elif(isinstance(fromdate,list)):
                            data.append(fromdate[0]+'-'+fromdate[1]+'-'+fromdate[2])
                        if(not isinstance(todate,list)):
                            data.append(str(todate)[:10])
                        elif(isinstance(todate,list)):
                            data.append(todate[0]+'-'+todate[1]+'-'+todate[2])
                    datas.append(data)
                    i=i+1
                    data=[]
                
                #global endtime
                #endtime = datetime.datetime.now()
                #print (endtime - starttime)
                return datas
            datas=get_datas(datas)
            x=tree.get_children()
            i=0
            for item in x:
                #tree.insert("",i,values=(i,5,5))
                p=Image.open("i\\fei.jpg")
                p = ImageTk.PhotoImage(p)
                #for i in range(len(shopidlist)):
                tree.item(item, image=p, values=datas[i],open=True)
                i+=1
                #tree.item(item, text="blub", values=datas[i])
               
                tree.grid()
            # request tkinter to call self.refresh after 1s (the delay is given in ms)
            if(shopidlist==[]):
                tree.after(2000, self.refresh_data)
            else:
                global insert_lock
                if insert_lock==0:
                    for i in range(len(shopidlist)):
                    #tree.insert("",i,values=(i,5,5))
                        p=Image.open("i\\fei.jpg")
                        p = ImageTk.PhotoImage(p)
                        tree.insert('',END,image=p, values=(datas[i]))                      
                        insert_lock=1
                #tree.item(item, text="blub", values=datas[i])
               
                tree.grid()
               
                
                tree.after(60000, self.refresh_data)
            #一分钟更新一次数据
    timer = Timer(window)
    #主事件循环
    window.mainloop()
if __name__ == '__main__':
    main()   
    
    

