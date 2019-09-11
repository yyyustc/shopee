from tkinter import *
from  tkinter import ttk 
import tkinter as tk
from time import *
from shopeeapi import *
screen_width=1920
screen_height=1080
insert_lock2=0
insert_lock3=0
insert_lock4=0
insert_lock5=0
def function1(names,passwords,urls,shopidlist):
     win=Tk() 
     win.title('店铺经营统计')
     tree=ttk.Treeview(win,show='headings')#表格
     
     tree["columns"]=("站点","实时订单","销售额","分区订单","销售总量排名【按照SKU排名】")
     tree.column("站点",)   #表示列,不显示
     tree.column("实时订单")
     tree.column("销售额")
     tree.column("分区订单")   #表示列,不显示
     tree.column("销售总量排名【按照SKU排名】",width=200)
  


     
     tree.heading("站点",text="站点")  #显示表头
     tree.heading("实时订单",text="实时订单")
     tree.heading("销售额",text="销售额")
     tree.heading("分区订单",text="分区订单")
     tree.heading("销售总量排名【按照SKU排名】",text="销售总量排名【按照SKU排名】")

     #tree.insert("",0,text="line1" ,values=("1","2","3")) #插入数据，
     #tree.insert("",1,text="line1" ,values=("1","2","3"))
     #tree.insert("",2,text="line1" ,values=("1","2","3"))
     #tree.insert("",3,text="line1" ,values=("1","2","3"))
      
     tree.pack(expand=1,fill=BOTH)
     class Timer:
        
        def __init__(self, parent):
            tree.pack(expand=1,fill=BOTH)
            # start the timer
            tree.after(1000, self.refresh_data)
        def refresh_data(self):
            """ refresh the content of the label every second """
            data=[]
            datas5=[]
            resp21={}

            def get_datas(datas5):
                nonlocal data
                import datetime
                #global starttime
                #starttime = datetime.datetime.now()
                #no
                if len(shopidlist)==0:
                    pass
                else:
                    i=0
                    datas5=[]
                    for shopid in shopidlist:
                        data5=[]
                        data5.append(datetime.datetime.now())#站点
                        #实时订单
                        #销售额
                        #分区订单
                        #销售总量排名【按照SKU排名】

                        datas5.append(data5)
                        
                    
                
                    #global endtime
                    #endtime = datetime.datetime.now()
                    #print (endtime - starttime)
                    return datas5
            datas5=get_datas(datas5)
            x=tree.get_children()
            i=0
            count=0
            if(len(x)>0):
               for i in range(len(datas5)):
                    if(count<len(x)):
                        item=x[count]
                        count+=1
                        tree.item(item,values=datas5[i])
                    else:
                        tree.insert('','end', values=(datas5[i]))

               
                    #tree.item(item, text="blub", values=datas[i])
               
               tree.pack(expand=1,fill=BOTH)
                        # request tkinter to call self.refresh after 1s (the delay is given in ms)            if(shopidlist==[]):
               tree.after(60000, self.refresh_data)
            
            else:
                global insert_lock5
                if insert_lock5==0:
                    for i in range(len(shopidlist)):
                    #tree.insert("",i,values=(i,5,5))
                        #p=Image.open("i\\fei.jpg")
                        #p = ImageTk.PhotoImage(p)
     
                            #tree.insert("",i,values=(i,5,5))
                            tree.insert('','end', values=(datas5[i]))                      
                    insert_lock5=1
                #tree.item(item, text="blub", values=datas[i])
               
                    tree.pack(expand=1,fill=BOTH)
               
                
                tree.after(60000, self.refresh_data)
        #一分钟更新一次数据
     timer = Timer(win)
     win.mainloop()




def function2(names,passwords,urls,shopidlist):
     
     win=Tk() 
     win.title('待发货订单')
     #window_width = screen_width * 0.8
     #window_heisght = screen_height *0.8
     #win.geometry("%dx%d" % (window_width, window_height))
     tree=ttk.Treeview(win,show='headings')#表格
     tree["columns"]=("1","2","3","4","5","6","7","8",'9','10','11')
     
     tree.column("1",width=100)   #表示列,不显示
     tree.column("2",width=100)
     tree.column("3",width=80)
     tree.column("4",width=80)   #表示列,不显示
     tree.column("5",width=20)
     tree.column("6",width=100)   #表示列,不显示
     tree.column("7",width=100)
     tree.column("8",width=10)
     tree.column("9",width=80)   #表示列,不显示
     tree.column("10",width=80)
     tree.column("11",width=200)
    


     
     tree.heading("1",text="站点")  #显示表头
     tree.heading("2",text="订单编码")
     tree.heading("3",text="订单分区")
     tree.heading("4",text="订单号")
     tree.heading("5",text="首图")
     tree.heading("6",text="产品编码【SKU】")  #显示表头
     tree.heading("7",text="订单金额")
     tree.heading("8",text="数量")
     tree.heading("9",text="属性")
     tree.heading("10",text="下单时间")
     tree.heading("11",text="备注")


     
     #tree.insert("",0,text="line1" ,values=("1","2","3")) #插入数据，
     #tree.insert("",1,text="line1" ,values=("1","2","3"))
     #tree.insert("",2,text="line1" ,values=("1","2","3"))
     #tree.insert("",3,text="line1" ,values=("1","2","3"))
      
     #tree.pack(expand=1,fill=BOTH)
     class Timer:
        
        def __init__(self, parent):
            tree.pack(expand=1,fill=BOTH)
            # start the timer
            tree.after(1000, self.refresh_data)
        def refresh_data(self):
            """ refresh the content of the label every second """
            data=[]
            datas2=[]
            resp21={}

            def get_datas(datas2):
                nonlocal data
                #import datetime
                #global starttime
                #starttime = datetime.datetime.now()
                #no
                if len(shopidlist)==0:
                    print("len",len(shopidlist))
                    pass
                else:
                    i=0
                    for shopid in shopidlist:
                        orderlist=[]
                        client = pyshopee.Client( int(shopid), partnerid, API_key )
                        resp21=READY_TO_SHIP(client)
                        for k in range(len(resp21['orders'])):
                            orderlist.append(resp21['orders'][k]['ordersn'])
                            print(resp21['orders'][k]['ordersn'])
                        j=0
                        respd = client.order.get_order_detail(ordersn_list=orderlist,timeout=20)
                        if(len(respd['orders'])>0):
                         for order in orderlist:
                            
                            orderdata=[]
                            #print(j)
                            
                            tmp=respd['orders'][j]
                            orderdata.append(urls[i])
                            orderdata.append('No.'+'{:02}'.format(j+1))
                            orderdata.append(tmp['recipient_address']['country']+tmp['recipient_address']['city'])
                            orderdata.append(order)
                            orderdata.append('待完善')
                            items_sku=[]
                            items=tmp['items']
                            for item in items:
                                items_sku.append(item['item_sku'])
                            orderdata.append(str(items_sku))#sku
                            orderdata.append(tmp['currency']+tmp['total_amount'])#订单金额
                            orderdata.append(len(tmp['items']))#数量
                            items_variation=[]
                            for item in items:
                                items_variation.append(item['variation_name'])
                            orderdata.append(str(items_variation))#属性
                            timeStamp=tmp['create_time']                            
                            dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                            otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
                            orderdata.append(otherStyleTime)
                            beizhu=tmp['message_to_seller']+tmp['note']
                            beizhu=beizhu.encode("utf-8")
                            '''
                            try:
                                beizhu = unicode(beizhu,"utf-8")
                            except TypeError as e:
                                pass
                                highpoints = re.compile(u'[\U00010000-\U0010ffff]')
                            
                                beizhu=highpoints.sub(u'',beizhu)
                            '''

                            #print(beizhu)
                            orderdata.append(beizhu)#备注
                            
                            #tmp=client.public.get_shops_by_partner(partnerid=partnerid)
                            #print("\n",i,'\n')
                            url=urls[i]
                            connectlock=1
                            data.append(orderdata)
                            j+=1
                        i=i+1
                        datas2.append(data)
                        
                        data=[]
                
                    #global endtime
                    #endtime = datetime.datetime.now()
                    #print (endtime - starttime)
                    return datas2
            datas2=get_datas(datas2)
            x=tree.get_children()
            i=0
            count=0
            if(len(x)>0):
               for i in range(len(datas2)):
                j=0
                #tree.insert("",i,values=(i,5,5))
                for j in range(len(datas2[i])):
                    if(count<len(x)):
                        item=x[count]
                        count+=1
                        tree.item(item,values=datas2[i][j])
                    else:
                        tree.insert('','end', values=(datas2[i][j]))

               
                    #tree.item(item, text="blub", values=datas[i])
               
                tree.pack(expand=1,fill=BOTH)
                        # request tkinter to call self.refresh after 1s (the delay is given in ms)            if(shopidlist==[]):
                tree.after(60000, self.refresh_data)
            
            else:
                global insert_lock2
                if insert_lock2==0:
                    for i in range(len(shopidlist)):
                    #tree.insert("",i,values=(i,5,5))
                        #p=Image.open("i\\fei.jpg")
                        #p = ImageTk.PhotoImage(p)
                        for j in range(len(datas2[i])):
                            #tree.insert("",i,values=(i,5,5))
                            tree.insert('','end', values=(datas2[i][j]))                      
                        insert_lock2=1
                #tree.item(item, text="blub", values=datas[i])
               
                        tree.pack(expand=1,fill=BOTH)
               
                
                tree.after(60000, self.refresh_data)
        #一分钟更新一次数据
     
     timer = Timer(win)
     win.mainloop()


def function3(names,passwords,urls,shopidlist):
     win=Tk() 
     win.title('店铺财务数据明细')
     tree=ttk.Treeview(win,show='headings')#表格
     tree["columns"]=("1","2","3","4","5","6","7","8",'9','10','11','12','13','14','15','16')
     tree.column("1",width=80)   #表示列,不显示
     tree.column("2",width=100)
     tree.column("3",width=80)
     tree.column("4",width=80)   #表示列,不显示
     tree.column("5",width=100)
     tree.column("6",width=100)   #表示列,不显示
     tree.column("7",width=100)
     tree.column("8",width=80)
     tree.column("9",width=80)   #表示列,不显示
     tree.column("10",width=100)
     tree.column("11",width=100)
     tree.column("12",width=100)   #表示列,不显示
     tree.column("13",width=80)
     tree.column("14",width=80)
     tree.column("15",width=80)#表示列,不显示
     tree.column("16",width=80)
    
     
     tree.heading("1",text="站点")  #显示表头
     tree.heading("2",text="订单编码")
     tree.heading("3",text="订单分区")
     tree.heading("4",text="订单号")
     tree.heading("5",text="首图")
     tree.heading("6",text="产品编码【SKU】")  #显示表头
     tree.heading("7",text="订单金额")
     tree.heading("8",text="买家实际支付")
     tree.heading("9",text="物流费用")
     tree.heading("10",text="优惠券及回扣")
     tree.heading("11",text="佣金及交易费")
     tree.heading("12",text="订单实际收入")
     tree.heading("13",text="产品采购成本")
     tree.heading("14",text="订单利润")
     tree.heading("15",text="本币结算")
     tree.heading("16",text="实时汇率")
     
     tree.pack(expand=1,fill=BOTH)
     class Timer:
        
        def __init__(self, parent):
            tree.pack(expand=1,fill=BOTH)
            # start the timer
            tree.after(1000, self.refresh_data)
        def refresh_data(self):
            """ refresh the content of the label every second """
            data=[]

            datas2=[]
            resp21={}

            def get_datas(datas2):
                nonlocal data
                #import datetime
                #global starttime
                #starttime = datetime.datetime.now()
                #no
                if len(shopidlist)==0:
                    pass
                else:
                    i=0
                    from forex_python.converter import CurrencyRates
                    c = CurrencyRates()
                    huilvs=c.get_rates('CNY')#1元人民可换这么多货币
                    for shopid in shopidlist:
                        orderlist=[]
                        client = pyshopee.Client(int(shopid), partnerid, API_key )
                        resp31= client.order.get_order_by_status (order_status='ALL')
                        tmp=resp31['orders']
                        if len(tmp)>0:
                            for k in range(len(tmp)):
                                if(tmp[k]['order_status']=='SHIPPED'):
                                    orderlist.append(tmp[k]['ordersn'])                      
                        j=0
                        if(len(orderlist)>0):
                         respd3 = client.order.get_order_detail(ordersn_list=orderlist,timeout=20)
                        
                        if(len(respd3['orders'])>0):
                            for order in orderlist:
                                tmp=respd3['orders'][j]
                                orderdata=[]
                                #print(j)
                                
                                orderdata.append(urls[i])
                                orderdata.append('OR.'+'{:02}'.format(j+1))
                                
                                orderdata.append(tmp['recipient_address']['country']+'\t'+tmp['recipient_address']['state'])#订单分区
                                orderdata.append(order)#订单号
                        
                                orderdata.append('待完善')#首图
                                items_sku=[]
                                items=tmp['items']
                                for item in items:
                                    items_sku.append(item['item_sku'])
                                orderdata.append(str(items_sku))#sku
                     
                                orderdata.append(tmp['currency']+tmp['total_amount'])#订单金额
                           
                               
                                buyerpay=tmp['total_amount']#商品金额+买家支付运费-Shopee Voucher-Shopee币折抵	
                                orderdata.append(buyerpay)
                                respd2=client.order.get_order_escrow_detail(ordersn=order,timeout=20)
                                tmp1=respd2['order']['income_details']
                                orderdata.append(tmp1['actual_shipping_cost'])#物流费用	
                                orderdata.append(str(tmp1['voucher']+tmp1['voucher_seller']))#优惠券及回扣	
                                orderdata.append(str(tmp1['commission_fee']+tmp1['credit_card_transaction_fee']))#佣金及交易费	
                                shijishouru=tmp1['escrow_amount']
                                orderdata.append(shijishouru)#订单实际收入	
                                caigoucost=0
                                orderdata.append(caigoucost)#产品采购成本【自动转换成外币】	
                                lirun=float(shijishouru)-caigoucost
                                orderdata.append(lirun)#订单利润
                                def get_huilv(a):
                                    nonlocal huilvs
                                    huilv=huilvs[a]
                                    return huilv
                                    pass
                                huilv=get_huilv(tmp1['local_currency'])
                                lirun_rmb=lirun/huilv
                                orderdata.append(lirun_rmb)#本币结算【RMB】
                                orderdata.append(huilv)#实时汇率

                                connectlock=1
                                data.append(orderdata)
                                j+=1
                        i=i+1
                        datas2.append(data)
                        
                        data=[]
                
                #global endtime
                #endtime = datetime.datetime.now()
                #print (endtime - starttime)
                return datas2
            datas2=get_datas(datas2)
            x=tree.get_children()
            i=0
            count=0
            if(len(x)>0):
               for i in range(len(datas2)):
                j=0
                #tree.insert("",i,values=(i,5,5))
                for j in range(len(datas2[i])):
                    if(count<len(x)):
                        item=x[count]
                        count+=1
                        tree.item(item,values=datas2[i][j])
                    else:
                        tree.insert('','end', values=(datas2[i][j]))
            
                        tree.pack(expand=1,fill=BOTH)

                    tree.after(60000, self.refresh_data)
            else:
                global insert_lock4
                if insert_lock4==0:
                    for i in range(len(shopidlist)):
                    #tree.insert("",i,values=(i,5,5))
                        #p=Image.open("i\\fei.jpg")
                        #p = ImageTk.PhotoImage(p)
                        for j in range(len(datas2[i])):
                            #tree.insert("",i,values=(i,5,5))
                            tree.insert('','end', values=(datas2[i][j]))                      
                        insert_lock4=1
                #tree.item(item, text="blub", values=datas[i])
               
                    tree.pack(expand=1,fill=BOTH)
                
                tree.after(60000, self.refresh_data)
        
     timer = Timer(win)
     win.mainloop()
     
def function4(names,passwords,urls,shopidlist):
     win=Tk() 
     win.title('采购及配货汇总')
     tree=ttk.Treeview(win,show='headings')#表格
     tree["columns"]=("1","2","3","4","5","6","7","8",'9','10')
     tree.column("1",width=80)   #表示列,不显示
     tree.column("2",width=100)
     tree.column("3",width=80)
     tree.column("4",width=80)   #表示列,不显示
     tree.column("5",width=100)
     tree.column("6",width=100)   #表示列,不显示
     tree.column("7",width=100)
     tree.column("8",width=80)
     tree.column("9",width=80)   #表示列,不显示
     tree.column("10",width=100)
    
     
     tree.heading("1",text="站点")  #显示表头
     tree.heading("2",text="订单编码")
     tree.heading("3",text="订单分区")
     tree.heading("4",text="订单号")
     tree.heading("7",text="下单时间")
     tree.heading("5",text="首图")
     tree.heading("6",text="产品编码【SKU】")  #显示表头
     tree.heading("8",text="属性")
     tree.heading("9",text="颜色及数量")
     tree.heading("10",text="备注")

     
     """
     zhan = ['马来-01','马来-01','马来-02']
     num= ['OR-001','OR-001','OR-001']
     qu=['A','A','a']
     for i in range(len(num)):# 写入数
         tree.insert('', i, values=(zhan[i], num[i],qu[i]))
     """
     tree.pack(expand=1,fill=BOTH)
     win.mainloop()
def loadaccount():
    getshopid()
def function5(names,passwords,urls,shopidlist):
     win5=Tk() 
     win5.title('店铺基本数据')
     tree=ttk.Treeview(win5,show='headings')#表格
     tree["columns"]=("1","2","3","4","5","6","7","8",'9','10','11','12','13','14','15','16','17','18','19','20','21','22')
     tree.column("1",width=60)   #表示列,不显示
     tree.column("2",width=30)
     tree.column("3",width=50)
     tree.column("4",width=50)   #表示列,不显示
     tree.column("5",width=60)
     tree.column("6",width=60)   #表示列,不显示
     tree.column("7",width=60)
     tree.column("8",width=60)
     tree.column("9",width=60)   #表示列,不显示
     tree.column("10",width=60)

     tree.column("11",width=60)   #表示列,不显示
     tree.column("12",width=60)
     tree.column("13",width=60)
     tree.column("14",width=60)   #表示列,不显示
     tree.column("15",width=60)
     tree.column("16",width=60)   #表示列,不显示
     tree.column("17",width=60)
     tree.column("18",width=80)
     tree.column("19",width=60)   #表示列,不显示
     tree.column("20",width=60)

     tree.column("21",width=80)   #表示列,不显示
     tree.column("22",width=80)
    
     
     tree.heading("1",text="国家/地区")  #显示表头
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
     tree.heading("12",text="账户金额")
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

     dict={}
     seq={"国家/地区","No.","站点","用户名","密码","站点网址【前台】","登录状态","店铺ID","产品数量","粉丝数量","关注数量","店铺名","账户余额","店铺评价","惩罚计分","浏览量","访客量","订单量","已下单金额","客单价","转化率","数据开始时间",	"数据截止时间"}
     dict=dict.fromkeys(seq)
     regions=[]
     nos=[]
     websites=[]
     usrname=[]
     password=[]
     urls=[]
     login_status=[]
     shopids=[]
     zhan = ['zg-01','zg-01','zh-02']
     num= ['01','01','01']
     usr_name=['A','A','a']
     for i in range(len(num)):# 写入数
         tree.insert('', i, values=(zhan[i], num[i],usr_name[i]))
     for i in range(len(num)):
         try:
            shopid=int(shopidlist[i])
            client = pyshopee.Client( shopid, partnerid, API_key )
            #tmp=client.public.get_shops_by_partner(partnerid=partnerid)
            #print("\n",i,'\n')
            usr_name=names[i]
            url=urls[i]
           
            
            resp1 = client.order.get_order_by_status (order_status='ALL')
            resp=READY_TO_SHIP(client)
            #1566287712=datetime.datetime.strptime('Aug 20, 2019 03:55:12 PM', '%b %d, %Y %I:%M:%S %p').timestamp()
            resp = client.order.get_order_list(create_time_from=1566287712,create_time_to=timestamp(),partner_id=partnerid,shopid=shopid,timestamp=timestamp())
            print("resp",resp)
            respd = client.order.get_order_detail(ordersn_list=ordersn_list,timeout=20)
            print("detail",respd)
         except:
             pass
     
     tree.pack(expand=1,fill=BOTH)
     '''
     def refresh_data(win):
        for i in range(len(names)):
         try:
            print("\n",i,'\n')
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
         except:
             pass
        zhan = ['zg-01','zg-01','zh-02']
        num= ['01','01','01']
        usr_name=['A','A','a']
        
     '''
     class Timer:
            def __init__(self, parent):
                # variable storing time
                self.seconds = 0
                # label displaying time
                #self.label = tk.Label(parent, text="0 s", font="Arial 30", width=10)
                #self.label.pack(expand=1,fill=BOTH)
                zhan = ['zg-01','zg-01','zh-02']
                num= ['01','01','01']
                usr_name=['A','A','a']
                
                tree.pack(expand=1,fill=BOTH)
                # start the timer
                tree.after(1000, self.refresh_data)

            def refresh_data(self):
                """ refresh the content of the label every second """
                i=0
                x=tree.get_children()
                datas=[]
                data=[]
                #names,passwords,urls,shopidlist=getshopid()
                pass
                for shopid in shopidlist:
                    #data.append()
                    #data.append()
                    datas.append(data)
                for item in x:
                    #tree.insert("",i,values=(i,5,5))
                    tree.item(item, text="blub", values=datas[i])
                    i+=1
                #tree.insert('', i, values=(i, 2,2))        
                tree.pack(expand=1,fill=BOTH)
                # request tkinter to call self.refresh after 1s (the delay is given in ms)
                tree.after(60000, self.refresh_data)
                #一分钟更新一次数据
     timer = Timer(win5)
     win5.mainloop()

def function6(names,passwords,urls,shopidlist):
     win=Tk() 
     win.title('运送中订单')
     #window_width = screen_width * 0.8
     #window_height = screen_height *0.8
     #win.geometry("%dx%d" % (window_width, window_height))
     '''
     def c1():
          win1=Tk()
          win1.title('明细')
          tree=ttk.Treeview(win1,show='headings')#表格
          tree["columns"]=("1","2","3","4","5")
          tree.column("1",width=100)   #表示列,不显示
          tree.column("2",width=100)
          tree.column("3",width=120)
          tree.column("4",width=120)   #表示列,不显示
          tree.column("5",width=120)
          
          tree.heading("1",text="商品金额")  #显示表头
          tree.heading("2",text="卖家支付运费")
          tree.heading("3",text="Shopee Voucher")
          tree.heading("4",text="Shopee币折抵")
          tree.heading("5",text="买家实际支付")
          
          tree.pack(expand=1,fill=BOTH)
          win1.mainloop()
     
          
     def c2():
          win2=Tk()
          win2.title('明细')
          tree=ttk.Treeview(win2,show='headings')#表格
          tree["columns"]=("1","2","3","4","5","6","7","8",'9','10','11')
          tree.column("1",width=80)   #表示列,不显示
          tree.column("2",width=80)
          tree.column("3",width=80)
          tree.column("4",width=80)   #表示列,不显示
          tree.column("5",width=100)
          tree.column("6",width=100)   #表示列,不显示
          tree.column("7",width=100)
          tree.column("8",width=100)
          tree.column("9",width=100)   #表示列,不显示
          tree.column("10",width=120)
          tree.column("11",width=120)
          
          tree.heading("1",text="商品金额")  #显示表头
          tree.heading("2",text="卖家支付运费总额")
          tree.heading("3",text="买家支付运费金额")
          tree.heading("4",text="实际运费")
          tree.heading("5",text="店铺优惠券")
          tree.heading("6",text="shopee运费回扣")
          tree.heading("7",text="佣金")
          tree.heading("8",text="交易手续费")  #显示表头
          tree.heading("9",text="运费总额")
          tree.heading("10",text="优惠券及回扣")
          tree.heading("11",text="佣金及交易手续费")
          tree.pack(expand=1,fill=BOTH)
          win2.mainloop()
     
               
     '''
     tree=ttk.Treeview(win,show='headings')#表格
     tree["columns"]=("1","2","3","4","5","6","7","8",'9','10','11')
     tree.column("1")   #表示列,不显示
     tree.column("2")
     tree.column("3")
     tree.column("4")   #表示列,不显示
     tree.column("5")
     tree.column("6")   #表示列,不显示
     tree.column("7")
     tree.column("8")
     tree.column("9")   #表示列,不显示
     tree.column("10")
     tree.column("11")   #表示列,不显示
     
     
    
     
     tree.heading("1",text="站点")  #显示表头
     tree.heading("2",text="No.")
     tree.heading("3",text="下单时间")
     tree.heading("4",text="订单分区")
     tree.heading("5",text="订单号")
     tree.heading("6",text="首图")
     tree.heading("7",text="产品编码【SKU】")  #显示表头
     tree.heading("8",text="物流跟踪号")
     tree.heading("9",text="订单金额")
     tree.heading("10",text="买家实际支付金额",#command=c1
                  )
     tree.heading("11",text="卖家实际支付金额",#command=c2
                  )
     



     
     tree.pack(expand=1,fill=BOTH)
     class Timer:
        
        def __init__(self, parent):
            tree.pack(expand=1,fill=BOTH)
            # start the timer
            tree.after(1000, self.refresh_data)
        def refresh_data(self):
            """ refresh the content of the label every second """
            data=[]

            datas2=[]
            resp21={}

            def get_datas(datas2):
                nonlocal data
                #import datetime
                #global starttime
                #starttime = datetime.datetime.now()
                #no
                if len(shopidlist)==0:
                    pass
                else:
                    i=0
                    for shopid in shopidlist:
                        orderlist=[]
                        client = pyshopee.Client(int(shopid), partnerid, API_key )
                        resp31= client.order.get_order_by_status (order_status='ALL')
                        tmp=resp31['orders']
                        if len(tmp)>0:
                            for k in range(len(tmp)):
                                if(tmp[k]['order_status']=='SHIPPED'):
                                    orderlist.append(tmp[k]['ordersn'])                      
                        j=0
                        if(len(orderlist)>0):
                         respd3 = client.order.get_order_detail(ordersn_list=orderlist,timeout=20)
                        
                        if(len(respd3['orders'])>0):
                            for order in orderlist:
                                #print(j)
                                tmp=respd3['orders'][j]
                                orderdata=[]
                                
                                
                                orderdata.append(urls[i])
                                orderdata.append('OR.'+'{:02}'.format(j+1))
                                timeStamp=tmp['create_time']                            
                                dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                                otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
                                orderdata.append( otherStyleTime)#订单创建时间
                                orderdata.append(tmp['recipient_address']['country']+''+tmp['recipient_address']['state'])#订单分区
                                orderdata.append(orderlist[j])
                                orderdata.append('待完get_datas善')#首图
                                items_sku=[]
                                items=tmp['items']
                                for item in items:
                                    items_sku.append(item['item_sku'])
                                orderdata.append(str(items_sku))#sku
                                orderdata.append(tmp['tracking_no'])#物流跟踪号
                                orderdata.append(tmp['currency']+tmp['total_amount'])#订单金额
                           
                                
                                buyerpay=tmp['total_amount']#商品金额+买家支付运费-Shopee Voucher-Shopee币折抵	

                                orderdata.append(buyerpay)#买家实际支付金额
                                res=client.order.get_order_escrow_detail(ordersn=order,timeout=20)
                                tmp=res['order']['income_details']
                                sellerpay=float(tmp['actual_shipping_cost'])+float(tmp['commission_fee'])#卖家支付运费总额+佣金及交易手续费-优惠券与回扣
                                orderdata.append(sellerpay)
                                #卖家实际支付金额
                                #tmp=client.public.get_shops_by_partner(partnerid=partnerid)
                                #print("\n",i,'\n')
                                url=urls[i]
                                connectlock=1
                                data.append(orderdata)
                                j+=1
                        i=i+1
                        datas2.append(data)
                        
                        data=[]
                
                #global endtime
                #endtime = datetime.datetime.now()
                #print (endtime - starttime)
                    return datas2
            datas2=get_datas(datas2)
            x=tree.get_children()
            i=0
            count=0
            if(len(x)>0):
               for i in range(len(datas2)):
                j=0
                #tree.insert("",i,values=(i,5,5))
                for j in range(len(datas2[i])):
                    if(count<len(x)):
                        item=x[count]
                        count+=1
                        tree.item(item,values=datas2[i][j])
                    else:
                        tree.insert('','end', values=(datas2[i][j]))
            
                        tree.pack(expand=1,fill=BOTH)

                    tree.after(60000, self.refresh_data)
            else:
                global insert_lock3
                if insert_lock3==0:
                    for i in range(len(shopidlist)):
                    #tree.insert("",i,values=(i,5,5))
                        #p=Image.open("i\\fei.jpg")
                        #p = ImageTk.PhotoImage(p)
                        for j in range(len(datas2[i])):
                            #tree.insert("",i,values=(i,5,5))
                            tree.insert('','end', values=(datas2[i][j]))                      
                        insert_lock3=1
                #tree.item(item, text="blub", values=datas[i])
               
                        tree.pack(expand=1,fill=BOTH)
                
                tree.after(60000, self.refresh_data)
        #一分钟更新一次数据
     timer = Timer(win)
     win.mainloop()


     


    



 


