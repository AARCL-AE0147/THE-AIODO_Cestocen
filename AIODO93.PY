#Copyright 2020 AIODO93
# NO License
#Author:ARELUSS
#在python任何开发中的综合框架

#初始化
if True:
    ADMIN=[]

    try:

        import base64

    except Exception:

        ADMIN.append("base64")

    try:

        import re

    except Exception:

        ADMIN.append("re")

    try:

        from urllib import request,parse

        import urllib.parse

        import urllib.request 

    except Exception:

        ADMIN.append("urllib")

    try:

        import time

    except Exception:

        ADMIN.append("time")

    try:

        import jwt

    except Exception:

        ADMIN.append("PyJwt")

    try:

        import pymysql

    except Exception:

        ADMIN.append("Pymysql")

    try:

        import threading

        N=threading.Lock()

    except Exception:

        ADMIN.append("threading")

    try:

        import time

    except Exception:

        ADMIN.append("time")

    try:

        import random

    except Exception:

        ADMIN.append('random')

    try:

        import pandas as pds

        import numpy as np

    except Exception:

        ADMIN.append("pandas")
        ADMIN.append("numpy")

    try:

        from sklearn.model_selection import train_test_split

        from sklearn.preprocessing import StandardScaler

        from sklearn.feature_extraction import DictVectorizer

        from sklearn.neighbors import KNeighborsClassifier

        from sklearn.externals import joblib

        from sklearn.linear_model import LogisticRegression

        from sklearn.tree import DecisionTreeClassifier,export_graphviz

    except Exception:

        ADMIN.append("scikit_learn")
    
    try:

        import jieba

    except Exception:

        ADMIN.append("jieba")

    try:

        import socket
    
    except Exception:

        ADMIN.append("socket")


    if len(ADMIN)>0:

        print("缺少模块"+str(ADMIN),"一些功能将被限制")
    
    print('''------------------------------------------------
        Welcome to the AIODO93 framework 
        if it shows that you have finished loading
        Developers:AARCL 

        THE AIODO93 - 0.77
------------------------------------------------- ''')

#字符串处理
class string(object):

    def search_to(KILLER,DATA):
        #search_to用来搜索字符 找到就返回True 没有就返回Flase 
        #KILLER 是搜索的字符 也可以写列表 如果列表中的一样不存在那么都会返回Flase
        #DATA 是搜素的文本 
        try:

            for i in KILLER:
                try:

                    OS=re.search(i,DATA).group()

                except Exception:

                    OS=None
                    break

            if OS==None:

                return False

            else:

                return True

        except Exception:

            print("object ERROR")
    
    def search_one(DATA,dirty_stuff=["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(",")","%","!","@","[","]","`","{","}"],ADD=None,FIT=None):
        #search_one用来过滤字符 过滤后会返回一个列表 有2个内容 第一个内容是过滤后的字符串 下标是0 第二个内容是 如果过滤了字符 就是False 如果没有过滤字符 就是True
        #DATA代表需要进行过滤的字符 ADD代表在默认过滤字符添加的字符必须为列表形式 FIT代表自定义过滤集也是需要列表
        try:

            if type(ADD)==list:
                for i in ADD:

                    dirty_stuff.append(i)

            if type(FIT)==list:

                dirty_stuff=FIT

            lens=len(DATA)
            sql=DATA

            for stuff in dirty_stuff:

                sql = sql.replace(stuff, "")

            if len(sql)-lens==0:

                return [sql,"True"]

            if len(sql)-lens!=0:

                return [sql,"False"]

        except Exception:

            print("object ERROR")

    #判断字符是否存在 replace方法
    def search_to_replace(KILLER=None,DATA=None):
        OS=len(DATA)
        OOS=DATA.replace(KILLER,"")
        OPS=len(OOS)

        if OS==OPS:
            return False
        else:
            return True


#文件提取
class data_open():

    def code_open(path,debug=False):
        try:
            f=open(path,"rb")
            AS=f.read().decode()
        except Exception as o:
            AS=None
            if debug==True:print(o)
        return AS


#字符串加密
class string_no_see(object):

    #CHAR加密
    def CHR(DATA):

        text = "hello kali"
        output = ""

        for i in range(len(text)):

            output +="CHR(%s)" % ord(text[i])

            if i<len(text)-1:

                output +="."

        return output


#列表处理
class AIODO93_list(object):
    
    #分页器
    def BOOK(book_key=1,book_num=20,book_open=None):
        #这是一个分页器 book_key页数 book_num代表一页的内容 book_open代表需要进行分页的表
        #最后的返回的结果是页数对应的内容和最大分页数
        #book_open除以book_num 如果有余数就+1 没有余数就直接返回 这是最大分页数的原理
        DATA=[]
        DATA2=[]
        DATA3=[]
        DATA4=[]
        SAVE=0
        OPENS=book_key*book_num

        if book_num>1:

            for i in range(OPENS):

                DATA.append(i)

            for i in range(book_num):

                i=i-(i+i)
                DATA2.append(DATA[i])

            DATA2.remove(DATA2[0])
            DATA2.append(DATA2[-1]-1)

            for i in range(len(DATA2)):

                i=i-(i+i)
                DATA3.append(DATA2[i])

            ADD=DATA3[0]
            DATA3.remove(DATA3[0])
            DATA3.append(ADD)

            try:

                for i in DATA3:

                    DATA4.append(book_open[i])

            except Exception:
                
                pass

            OS=int(len(book_open)/book_num)
            UN=len(book_open)%book_num

            if UN != 0:

                OS=OS+1

            return [DATA4,OS]
            
        try:

            return [book_open[book_key*book_num-1],len(book_open)]

        except Exception:

            return [None,len(book_open)]

    #二维列表多下标搜查 模糊
    def Dlist(DATA=None,IS=None,search=None):
        #data必须是[[]] IS是列表下标必须传入一个列表 search是查找字符串
        #这函数的作用是将大列表中所有的列表 所对应的指定下标 是否出现search查找字符串 只要出现就会加入返回列表 只出现一次即可

        SOT=[]

        for i in IS:
            for o in DATA:

                try:

                    BB=string.search_to(KILLER=[search],DATA=o[i])

                    if BB==True:

                        SOT.append(o)

                except Exception:

                    pass

        SOT=set(SOT)

        return SOT

    #二维列表多下标搜查 强制
    def Dlist_one(DATA=None,IS=None,search=None):
        #如上 只不过 IS中的下标只有都有search搜查字符串才能加入返回列表

        SAC=[]

        for o in DATA:

            AS=[]

            for i in IS:

                try:

                    BB=string.search_to(KILLER=[search],DATA=o[i])

                    if BB==True:

                        AS.append("TRUE")

                    if len(AS)==len(IS):

                        SAC.append(o)

                except Exception:
                    pass
        
        return SAC

    #获取一个列表中最大的值 以及它的下标
    def list_max(DATA):

        IOP=DATA[0];index=0;KILL=0;target=0

        for i in DATA:

            if i==IOP:pass
            if i>IOP:KILL=i;target=index
            if i<IOP:pass
            index=index+1

        return [KILL,target]

    #获取一个列表中最小的值 以及它的下标
    def list_min(DATA):

        IOP=DATA[0];index=0;KILL="s";target=0

        for i in DATA:
            if i==IOP:pass
            if i<IOP:KILL=i;target=index
            if i>IOP:pass
            index=index+1

        if KILL=="s":
            
            return[IOP,target]

        return [KILL,target]

    #将一个列表中的所有整型转换成浮点数
    def listOFfloat(DATA):

        APP=[]

        for i in DATA:

            if type(i)==float:APP.append(i)
            else:APP.append(float(i))

        return APP

    #将一个列表中所有的数字转换成整型
    def listOFnum(DATA):

        APP=[]

        for i in DATA:
            APP.append(int(i))

        return APP

    #计算列表数字平均值
    def listmean(DATA):

        O=0

        for i in DATA:

            O=O+i

        return O/len(DATA)

    #指定一个列表中对应下标的值更换你所传的值
    def listreplace(DATA,X,YOU):

        index=0

        for i in X:

            DATA[index]=YOU[index]
            index=index+1

        return DATA


#文件后缀处理
class file_end(object):
    def end(DATA,END):
        if DATA.endswith(".html"):
            return True
        else:
            return False


#web框架搭建
class SOCKET_WEB:
    def web_bulid(port=None,humen=None):
        if port==None:port=8239
        if humen==None:humen=1000000

        tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        tcp_server.bind(("",port))
        tcp_server.listen(128)

        return tcp_server


#网络爬虫            
class web(object):
    #发生get 分别是链接 头 get请求文件 代理
    def get(URL,HAND=None,GETDATA=None,DAILI=None):
        #数据爬取-GET
        #URL填链接 HAND填头 GETDATA填get文件请求
        if DAILI==None:
            if GETDATA==None:
                if HAND==None:

                    req=request.Request(url=URL,method='GET')
                    reop=request.urlopen(req)

                    return reop.read().decode('utf-8')

                else:

                    req=request.Request(url=URL,method='GET',headers=HAND)
                    reop=request.urlopen(req)

                    return reop.read().decode('utf-8')

            else:
                if HAND==None:

                    parser=urllib.parse.urlencode(GETDATA)

                    URL=URL+"?"+parser

                    req=request.Request(url=URL,method="GET")
                    reop=request.urlopen(req)

                    return reop.read().decode('utf-8')

                else:

                    parser=urllib.parse.urlencode(GETDATA)

                    URL=URL+"?"+parser

                    req=request.Request(url=URL,method="GET",headers=HAND)
                    reop=request.urlopen(req)

                    return reop.read().decode('utf-8')

        else:
            if GETDATA==None:
                if HAND==None:

                    VPN=urllib.request.ProxyHandler(DAILI)
                    RVPN=urllib.request.build_opener(VPN)
                    parser=urllib.parse.urlencode(GETDATA)

                    URL=URL+"?"+parser

                    req=request.Request(url=URL,method='GET')
                    VPNP=RVPN.open(req)

                    return VPNP.read().decode('utf-8')

                else:

                    VPN=urllib.request.ProxyHandler(DAILI)
                    RVPN=urllib.request.build_opener(VPN)
                    parser=urllib.parse.urlencode(GETDATA)

                    URL=URL+"?"+parser

                    req=request.Request(url=URL,method='GET',headers=HAND)
                    VPNP=RVPN.open(req)

                    return VPNP.read().decode('utf-8')

            else:
                if HAND==None:

                    parser=urllib.parse.urlencode(GETDATA)

                    URL=URL+"?"+parser

                    VPN=urllib.request.ProxyHandler(DAILI)
                    RVPN=urllib.request.build_opener(VPN)
                    req=request.Request(url=URL,method="GET")
                    VPNP=RVPN.open(req)

                    return VPNP.read().decode('utf-8')
                    
                else:

                    parser=urllib.parse.urlencode(GETDATA)

                    URL=URL+"?"+parser

                    VPN=urllib.request.ProxyHandler(DAILI)
                    RVPN=urllib.request.build_opener(VPN)
                    req=request.Request(url=URL,method="GET",headers=HAND)
                    VPNP=RVPN.open(req)

                    return VPNP.read().decode('utf-8')
        
    #发送post 分别是链接 请求头 data    
    def post(URL,HAND=None,DATA=None):
        #如上
        if DATA==None:
            if HAND==None:

                req=request.Request(url=URL,method="POST")
                reop=request.urlopen(req)

                return reop.read().decode('utf-8')

            else:

                req=request.Request(url=URL,method="POST",headers=HAND)
                reop=request.urlopen(req)

                return reop.read().decode('utf-8')

        else:
            if HAND==None:

                data=urllib.parse.urlencode(DATA)
                data=data.encode("utf-8")
                req=request.Request(url=URL,method='POST',data=data)
                reop=request.urlopen(req)

                return reop.read().decode('utf-8')

            else:

                PARSER=urllib.parse.urlencode(DATA)
                PARSER=PARSER.encode("UTF-8")
                req=request.Request(url=URL,method='POST',data=PARSER,headers=HAND)
                reop=request.urlopen(req)

                return reop.read().decode('utf-8')


#AWKFaction框架
class AWKFaction(object):

    #网络请求处理-
    class web_request(object):


        #分割请求
        def request_split(DATA):
            request_open={}
            request_POST={}

            #获取请求头 与地址
            def state1():
                DATAIO=DATA.split(" ",999999)
                IOS=DATAIO[1]

                AD=IOS.split("?",1)

                try:
                    del AD[1]
                except Exception:
                    pass
                request_open.update({"url":AD[0]})
                request_open.update({"request":DATAIO[0]})

            #获取post请求文件
            def state2():
                if request_open["request"]=="POST":

                    DATAIO=DATA.split("\n",999999)
                    
                    DASS=DATAIO[-1]
                    THE=urllib.request.unquote(DASS)

                    THE=THE.split("&",9999999)
                    try:
                        for i in THE:
                            AUIODO=i.split("=",1)
                            request_POST.update({AUIODO[0]:AUIODO[1]})

                        request_open.update({"postdata":request_POST})
                    except Exception:
                        request_open.update({"postdata":None})
            
            #获取其余请求头
            def state3():

                DATAIO=DATA.split("\n",9999999)

                del DATAIO[0]
                del DATAIO[-1]

                OAP=[]
                for i in DATAIO:
                    IAO=i.split(":",1)
                    OAP.append(IAO)

                ZAP=[]
                PASZ=[]
                for i in OAP:
                    ZAP=[]
                    for o in i:
                        AS=o.replace("\r","")
                        ZAP.append(AS)
                    PASZ.append(ZAP)
                
                index=0
                for i in PASZ:
                    if len(i)==2:
                        index=index+1
                    else:
                        del PASZ[index]
                        index=index+1

                for i in PASZ:
                    request_open.update({i[0]:i[1]})  
            
            #获取get请求文件
            def state4():
                DATAIO=DATA.split(" ",999999)

                OPASS=DATAIO[1]

                try:
                    if string.search_to_replace(DATA=OPASS,KILLER="?")==True:

                        GETDATA=OPASS.split("?",1)

                        THE=urllib.request.unquote(GETDATA[1])

                        THE=THE.split("&",9999999)

                        try:
                            for i in THE:
                                AUIODO=i.split("=",1)
                                request_POST.update({AUIODO[0]:AUIODO[1]})

                            request_open.update({"GETDATA":request_POST})

                        except Exception:
                            request_open.update({"GETDATA":None})
                    else:
                        request_open.update({"GETDATA":None})

                except Exception:
                    request_open.update({"GETDATA":None})

            #分割请求地址
            def state5():
                print("----")
                PAR=request_open["url"]
                print(request_open)
                AODP=PAR.split("?",1)
                print(AODP)
                try:
                    del AODP[1]
                    request_open["url"]=AODP[0]
                except Exception:
                    request_open["url"]=AOOP[0]
            
            #获取cookie参数
            def state6():
                PPD={}
                OAP=request_open["Cookie"]
                kak=OAP.split(";",99999999)
                for i in kak:
                    AD=i.split("=",1)
                    A=AD[0]
                    P=A[1:len(A)]
                    PPD.update({P:AD[1]})
                    
                request_open["Cookie"]=PPD

            state1()
            state2()
            state3()
            state4()
            state6()
            return request_open


        #设置跨度key
        def url_of_HTML(DATA,PAF):
            DOGO=DATA["url"]
            if DOGO=="/":
                return DATA

            OAP=file_end.end(DOGO,".html")
            if OAP==True:
                return DATA
            else:
                DATA.update({PAF:"True"})
            return DATA


        #清除跨度key
        def del_url_of_HTML(DATA,RAF,debug=False):
            try:
                del DATA[RAF]
                if debug==True:print("检测到用户自带跨度key已清除")
                return DATA
            except Exception:
                if debug==True:print("用户没有携带跨度key")
                return DATA
        
    #网络回复请求处理
    class return_request(object):

        def return200(DATA):
            return{"web":200,"DATA":DATA}

        def return200OFDATA(DATA):
            return{"web":"DATA200","DATA":DATA}

        def return302(GOTO):
            return{"web":"302","goto":GOTO}

        def setcookie200(DATA,COOKIE,TIME):
            return{"web":"S200","DATA":DATA,"COOKIE":COOKIE,"TIME":TIME}

        def setcookie_new(COOKIE,TIME):
            return{"web":"news200","COOKIE":COOKIE,"TIME":TIME}

        def delcookie(COOKIE):
            return{"web":"delc","COOKIE":COOKIE}
    
    #网络请求编码处理
    class return_encode(object):
        #处理HTML
        def R200(DATA):
            TOAD=REPON.reponr(200)
            WEBECHO_header=[("Server","AWKFaction/1.1"),("AD","ARELUSS")]
            CCA=REPON.headers(WEBECHO_header)
            PPA=REPON.END(TOAD,CCA,DATA["DATA"])
            return PPA

        #处理静态文件
        def RD200(DATA):
            TOAD=REPON.reponr(200)
            WEBECHO_header=[("Server","AWKFaction/1.1"),("AD","ARELUSS")]
            CCA=REPON.headers(WEBECHO_header)
            PPA=REPON.END(TOAD,CCA,DATA["DATA"])
            return PPA

        #重定向
        def R302(DATA):
            TOAD=REPON.R302()
            WEBECHO_hearder=[("Location",DATA["goto"])]
            CCA=REPON.headers(WEBECHO_hearder)
            PPA=REPON.END(TOAD,CCA,"THENOFS")
            print(PPA)
            return PPA

        #返回页面的cookie设置
        def R200_SETCOOKIE(DATA):
            TOAD=REPON.reponr(200)
            COOKIE_header=REPON.open_cookie(DATA["COOKIE"],DATA["TIME"])
            WEB_header=REPON.headers([("Server","AIODO93")])
            print("------")
            PPA=REPON.END_OF_COOKIE(TOAD,WEB_header,COOKIE_header,DATA["DATA"])
            return PPA
        
        def NEW_COOKIE(DATA):
            TOAD=REPON.reponr(200)
            COOKIE_header=REPON.open_cookie(DATA["COOKIE"],DATA["TIME"])
            WEB_header=REPON.headers([("Server","AIODO93")])
            return REPON.COOKIE(TOAD,COOKIE_header,WEB_header)

        def del_COOKIE(DATA):
            TOAD=REPON.reponr(200)
            COOKIE=REPON.COOKIE_DEL(DATA["COOKIE"])
            WEB_header=REPON.headers([("Server","AIODO93")])
            return REPON.COOKIE(TOAD,COOKIE,WEB_header)

    #HTML文件提取
    def HTML(path,debug=False):
        try:
            f=open(path,"rb")
            AS=f.read().decode()
        except Exception as o:
            AS=None
            if debug==True:print(o)
        return AS

    #静态文件提取
    def DATA(path,debug=False):
        try:
            if path[0]=="/":
                path="."+path
            f=open(path,"rb")
            AS=f.read()
            return AS
        except Exception:
            return 404

    #结局404
    def ENDOF404(path):
        APS=data_open.code_open(path)
        PP1,PP2=REPON.the404()

        ENDSS=REPON.END(PP1,PP2,APS)
        return ENDSS


#统一回应头头构造HTTP /1.1
class REPON(object):

    #头构造
    def reponr(num):
        num=f"{num} ok"
        return "HTTP/1.1 %s\r\n"%num
    
    #headers构造
    def headers(DATA):
        PAND=""
        for WEB in DATA:
            PAND=PAND+"%s: %s\r\n"%WEB
        return PAND

    #最终请求构造
    def END(HTTPSP,header,data):
        try:
            ESS=HTTPSP+header+"\r\n"+data
            return ESS.encode("utf-8")
        except Exception:
            return (HTTPSP+header+"\r\n").encode("utf-8")+data
    
    #404请求构造
    def the404():
        webecho_line="HTTP/1.1 404 Not Found\r\n"
        webecho_header="Server:PWS/1.0\r\n"

        return webecho_line,webecho_header

    #302重定向头构造
    def R302():
        OS="HTTP/1.1 302 Found\r\n"
        return OS

    #cookie信息取出并生成请求头
    def open_cookie(DATA,time):
        PANDSA=""
        for i in DATA:
            PANDSA=PANDSA+f"Set-Cookie: {i}={DATA[i]}; expires=Tue; Max-Age={time}\r\n"
        return PANDSA

    #带有cookie信息的页面返回
    def END_OF_COOKIE(STATUS,HEADERS,COOKIE_HEADERS,DATA):
        bha=STATUS+HEADERS+COOKIE_HEADERS+"\r\n"+DATA
        return bha.encode("utf-8")

    #设置cookie
    def COOKIE(STATUS,HEADERS,COOKIE):
        BHA=STATUS+HEADERS+COOKIE+"\r\n"
        return BHA.encode("UTF-8")

    #删除cookie
    def COOKIE_DEL(DATA):
        PANDSA=""
        for i in DATA:
            PANDSA=PANDSA+f"Set-Cookie: {i}=""; expires=Tue; \r\n"
        return PANDSA


#时间处理
class new_time(object):
    #返回列表形式的时间 直接调用即可

    def times(DATA=None):

        TIMES=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        if DATA==None:

            DATA=[]
            DATA.append(TIMES[0:4])
            DATA.append(TIMES[5:7])
            DATA.append(TIMES[8:10])
            DATA.append(TIMES[11:13])
            DATA.append(TIMES[14:16])
            DATA.append(TIMES[17:19])

            return DATA

        else:

            return TIMES


#HTMLbase64数据解码
class HTML_base64(object):
    #对HTML传来的base64进行解码 data是base64字符串 会返回文件后缀和解码后的数据
    def UP_File(data):
        #HTML文件解码器 data用来填要解码的文件
        #会返回2个结果 第一个结果是base64自带文件前缀
        #第二个是解码后的数据 （如果是文本你只需要decode一下）

        OS=data.split(",",1)
        PI=base64.b64decode(OS[1])

        return [OS[0],PI]


#TOKEN生成
class token(object):

    #对字符串进行加密 OS是加密厚度(相当于key) ARELUSS研发 会返回加密字符串
    def encode_token(data,OS):
        import base64
        SS=data

        for i in range(OS):

            SS=SS.encode("utf-8")
            OSA=base64.b16encode(SS)
            SS=base64.b64encode(SS)
            SS=SS.decode("utf-8")
            OSA=OSA.decode("utf-8")
            SS=SS+OSA[0:2]

        return SS
    
    #对加密字符串进行解密 OS是加密厚度 ARELUSS研发 会返回解密字符
    def decode_token(data,OS):
        import base64
        SS=data

        for i in range(OS):

            SS=SS[0:len(SS)-2]
            SS=base64.b64decode(SS)
            SS=SS.decode("utf-8")

        return SS

    #一键生成jwt tokeen data是字典 key是jwtkey time是时间 会返回JWT
    def jwt_encode(data,key,time=None):
        import jwt
        if time==None:

            try:

                OS=jwt.encode(data,key,algorithm="HS256")
                OS=OS.decode("utf-8")

                return OS

            except Exception:

                return False

        else:

            datas={'exp':time}
            data.update(datas)

            try:

                OS=jwt.encode(data,key,algorithm="HS256")

            except Exception:

                return False

            OS=OS.decode("utf-8")
            return OS
    
    #对jwt进行解码 data是JWT key是密匙 会返回解码的JWT
    def jwt_decode(data,key):
        import jwt
        try:
            OS=jwt.decode(data,key,algorithms="HS256")

            return OS

        except Exception as O:

            print(O)

            return False


#字典处理
class dicts(object):

    #直接获取字典中key所对应的一项  dicts必须为二维列表中的字典 data为key 返回key的value
    def dict_value(dicts=None,data=None):

        for item in dicts:
            for values in item:
                if values==data:
                    return item[values]

        return None

    #生成socketio dict data必须为字典 返回socketio会话字典
    def socketio_dict(data=None):

        IS={
            "msg":data,
            "timestamp":round(time.time()*1000)
        }

        return IS

    #将列表每一个值转换为列表 DATA=为列表 KEY=列表对应的key 这也是列表
    def listofdict(DATA,KEY):

        OA={}

        for i in range(len(KEY)):

            OA.update({KEY[i]:DATA[i]})

        return OA


#MYSQL处理
class MYSQL(object):
    #LOGIN为字典 字典key必须出现 host user port passwd 
    #database代表数据库名字
    #search代表查询字符串
    #FITS代表是过滤
    def database_all(LOGIN=None,database=None,search=None,FITS=None):

        N=threading.Lock()
        N.acquire()

        SQLDB=pymysql.connect(
            host=LOGIN["host"],port=LOGIN["port"],
            user=LOGIN["user"],passwd=LOGIN["passwd"],
            database=database,charset="utf8"
        )
        SQLDATA=SQLDB.cursor()

        SQL="show tables"

        SQLDATA.execute(SQL)
        OPENS=SQLDATA.fetchall()

        DATA=[]
        DATABASE=[]
        DATAOS=[]
        
        for i in OPENS:

            DATA.append(i[0])
        
        if FITS==None:

            OS=string.search_one(DATA=search)
            OS=OS[0]

        else:

            OS=string.search_one(DATA=search,FIT=FITS)
            OS=OS[0]

        for i in DATA:

            SQL="select * from %s"%i
            SQLDATA.execute(SQL)
            DATABASE.append(SQLDATA.fetchall())

        for i in DATABASE:
            for o in i:

                DATAOS.append(o)
        
        DATA=[]

        for i in DATAOS:
            for o in i:

                BB=string.search_to(KILLER=[search],DATA=o)

                if BB==True:
                    DATA.append(i)

        DATA=set(DATA)
        DATABASE=[]

        for i in DATA:

            DATABASE.append(i)

        N.release()

        return DATABASE


#验证码生成
class TO_HUMEN(object):

    def state(num=4,strings=True,nums=True):
        if strings==True:PP=1
        if nums==True:PP=2
        if nums==True and strings==True:PP=3

        IAO=""
        if PP==1:
            for i in range(num):

                IAO=IAO+random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")

        if PP==2:
            for i in range(num):

                IAO=IAO+random.choice("1234567890")

        if PP==3:
            for i in range(num):

                IAO=IAO+random.choice("QWERTYUIOPASDFGHJKLZXCVBNM1234567890")

        return IAO


#UUID生成
class TO_ONE(object):
    #直接调用即可生成一个UUID
    def TIME_ONE_FOR():

        IS=""
        SA=new_time.times()
        OS=""

        for i in range(len(SA)):

            OS=OS+SA[i]

        for i in range(8):

            IS=IS+random.choice("QWERTYUIOPASDFGHJKLZXCVBNM1234567890")

        SA=OS+"-"+IS;print(SA)

        return SA


#PANDAS模块铺助
class PANDAS(object):
    #自动缺值填补
    def ISNULL(DATA=None):

        UPDATE=[]

        for i in DATA.columns:
            if np.all(pds.notnull(DATA[i]))==False:

                UPDATE.append(i)
                DATA[i].fillna(DATA[i].mean(),inplace=True)

            if len(DATA)>0:

                OA=True

            else:

                OA=False

        return (DATA,UPDATE,OA)


#SKLEARN模块铺租
class SKLEARN(object):
    #自动进行测试集与特征集拆分 SP为拆分比例

    def SPLIT(DATA=None,SP=0.2):

        PP1,PP2,PP3,PP4=train_test_split(DATA.data,DATA.target,test_size=SP)
        OS=StandardScaler()
        PP1=OS.fit_transform(PP1)
        PP2=OS.fit_transform(PP2)

        return PP1,PP2,PP3,PP4 
    

    #一键进行分词
    class Dict_T(object):

        def Dict_open(DATA=None):

            OS=DictVectorizer(sparse=False)
            
            return [OS.fit_transform(DATA),OS.get_feature_names(),OS]
    

    #一键打印模型预测属性
    class AI(object):

        def mod_print(DATA):

            print("------模型系数-----\n",DATA.coef_)
            print("------模型偏差-----\n",DATA.intercept_)

            return [DATA.coef_,DATA.intercept_]


    #利用pairwise计算用户相似用户
    def USER_and_USER(DATA,isrange=None):

        TODE=[];AIO=DATA;AIO2=[]

        for i in DATA.index:

             AIO2.append(i)

        PAO=AIODO93_NUM.DATA(DATA=AIO)
        index=0

        for i in PAO:

            index=0

            for o in i:

                if int(o)==1:

                    PAO[index][index]=0

                index=index+1

        ISA=PAO

        def STATE(PAO=ISA):

            IA=[];TA=[];index=0

            for i in PAO:

                PP=AIODO93_list.listOFfloat(i)
                AO=AIODO93_list.list_max(PP)
                PAO[index][AO[1]]=0
                IA.append(AO[1])
                index=index+1

            for i in range(len(IA)):

                TA.append([AIO2[i],[AIO2[IA[i]]]])

            return [TA,PAO]

        AA1=STATE()[0]
        AA2=STATE()[1]
        
        def RESTATE(RE=None,RELIST=None):

            IA=[];TA=[];index=0

            for i in RE:

                PP=AIODO93_list.listOFfloat(i)
                AO=AIODO93_list.list_max(PP)

                RE[index][AO[1]]=0
                ASA=AO[1]
                RELIST[index][1].append(AIO2[AO[1]])
                index=index+1

            return [RELIST,RE]

        if isrange==None:

            return RESTATE(AA2,AA1)[0]

        index=0

        for i in range(isrange):
            if index==0:

                AA=RESTATE(AA2,AA1)
                BB=RESTATE(AA[1],AA[0])
                index=index+1

            else:

                BB=RESTATE(BB[1],BB[0])

        if index==1:

            return AA[0]

        else:

            try:

                return BB[0]

            except Exception:

                return AA[0]
    
    #预测用户对一个物品的指数 THE为原pandas USER_AND_USER为用户相近用户列表 UNKOWN为用户需要预测的object
    #请把函数 USERandUSER函数的结果给USERANDUSER
    #BIG是最大分数
    def USER_and_UNKOWN(THE=None,USER_AND_USER=None,UNKOWN=None,BIG=None,debug=False):
        PP=THE.columns;IS=[];
        
        #后期重要值
        IS_CAT=[];data=[];samedata=[];endsamedata=[]

        for i in PP:
            IS.append(i)

        for i in UNKOWN:
            IS_CAT.append(i)

        for i in IS_CAT:
            data.append(IS[i])

        for i in USER_AND_USER[1]:
            samedata=[]

            for o in data:
                if THE[o][i]==0:

                    samedata.append(1)

                else:

                    samedata.append(THE[o][i])
                
            endsamedata.append(samedata)

        if debug==True:print(f"你预测的用户是 {USER_AND_USER[0]} 对对象{data}的指数预测 他的相应用户分别对这{len(data)}个对象的映像是{endsamedata}")

        def STATE():

            if debug==True:print("STATE")

            OA=[];END=[];EEND=0;ENDS=[];SATA=0

            for i in range(len(data)):

                END=[];EEND=0;

                for o in range(len(endsamedata)):

                    END.append(endsamedata[o][i])

                for o in END:

                    EEND=EEND+o

                for o in PP:

                    OA=THE[o][USER_AND_USER[0]]
                    SATA=SATA+OA

                ENDS.append((EEND/len(USER_AND_USER[1]))-0.1*(SATA/len(THE.columns)))

            return ENDS

        return STATE()


#中文处理
class CHINA(object):
    #多中文列表处理
    def one_list_jieba(data=None):

        LIST=[]

        for i in data:
            
            LIST.append(" ".join(list(jieba.cut(i))))

        return LIST


#测试集生成
class Ai_Data_Load():

    def Data_Load_1():

        features={'SepalLength':np.array([6.4,5.0]),
          'SepalWidth':np.array([6.4,5.0]),
          'PetalLength':np.array([2.2,1.0]),
          'Petalwidth':np.array([5.0,5.7]),
         }

        return features

    
#算法原型
class AIODO93_NUM(object):
    #PANDAS拆分成python列表
    def DATA(DATA,state=None,tagert=None):

            OPEN_DATA=[];OPEN_NAME=DATA.columns;OPEN_LIST=[]

            for i in OPEN_NAME:

                OPEN_LIST=[]

                for SATE in range(DATA.shape[0]):

                    OPEN_LIST.append(DATA[i][SATE])

                OPEN_DATA.append(OPEN_LIST)
                
            NEW_OPENDATA=[];SUPER_OPENDATA=[]

            for i in range(len(OPEN_DATA[0])):

                NEW_OPENDATA=[]

                for o in OPEN_DATA:

                    NEW_OPENDATA.append(o[i])

                SUPER_OPENDATA.append(NEW_OPENDATA)

            if state==None:return SUPER_OPENDATA

            STATE_OPEN=[];SUPER_STATE_OPEN=[]

            for o in SUPER_OPENDATA:

                STATE_OPEN=[]

                for i in state:

                    STATE_OPEN.append(o[i])

                SUPER_STATE_OPEN.append(STATE_OPEN)

            if tagert==None:return SUPER_STATE_OPEN

            APS=[];APP=[]

            for i in SUPER_OPENDATA:

                APS=[]

                for o in tagert:

                    APS.append(i[o])

                APP.append(APS)

            return {"data":SUPER_STATE_OPEN,"target":APP}
    
    #验证是否有差值
    def istrue(DATA=None):

        SUB=DATA["target"]
        SUA=DATA["data"]

        if len(SUB)==len(SUA):
            return True

    #ARELUSS 死亡算法 (已失败)
    class AIODO93_DIEGAME(object):

        def KILL_GAME(isdata=None,newdata=None,target=None,isrange=None):#此算法已失败 纪念品

            def IFISRANGE():

                if isrange == None:
                    IIS=0

                    for i in isdata:
                        IIS=IIS+i

                    IIS=IIS/len(isdata)
                    return IIS

                else:
                    return isrange

            def ABSTO():

                AAR=[];BBR=[]

                for o in newdata:
                    AA=0;BBR=[]
                    for i in isdata:
                        IO=abs(i-o[AA]);AA=AA+1
                        BBR.append(IO)
                    AAR.append(BBR)

                return AAR
            
            def LIVE(IAS=IFISRANGE()):

                THE_ABS=ABSTO();newisrange=IAS;ISOPEN={};ADD=[]
                DICT_NUM=0

                for data in THE_ABS:
                    ISKILL=0
                    for num in data:
                        if num > newisrange:
                            ISKILL=ISKILL+1

                    ISOPEN.update({DICT_NUM:[data,[ISKILL]]})
                    DICT_NUM=DICT_NUM+1

                return ISOPEN

            OA=LIVE();CCP=OA[0][1][0];IIA={}

            for i in range(len(OA)):
                SAO=OA[i]
                if SAO[1][0] > CCP:
                    pass
                if SAO[1][0] <= CCP:
                    CCP=SAO[1][0]
                    IIA.update({i:SAO})

            if len(IIA)==1:
                for key in IIA:
                    IA=key
                return target[IA]

            else:
                def RE(RELIST=None):

                    THE_DATA=[];ONE_DATA=[];OSS=0;ONE=0

                    for i in RELIST:
                        THE_DATA.append(i)

                    for i in THE_DATA:
                        ONE_DATA.append(newdata[i])

                    for i in ONE_DATA:
                        for num in i:
                            OSS=OSS+num
                            ONE=ONE+1

                    IOP=int(OSS/ONE)*int(OSS/ONE)

                    return IOP

                STATE=RE(RELIST=IIA)

                print(STATE,"THE ELSE1")

                def RE2(THE=None,ISRAN=None):

                    HUB=[];HUA=[]

                    for i in THE:
                        HUB=[]
                        for o in newdata[i]:
                            HUB.append(o)
                        HUA.append([HUB,[i]])

                    return HUA

                STATE2=RE2(THE=IIA)
                print(STATE2,"THE ELSE2")
                    
                def RE3(THE=None,ISRAN=None):

                    TODIE=[];STATE=[];UUAS={}

                    for i in THE:
                        KILLER=0
                        TODIE=[]
                        STATE=[]
                        for o in i[0]:
                            if o > ISRAN:
                                KILLER=KILLER+1
                            TODIE.append(o)
                        STATE.append(TODIE)
                        UUAS.update({i[1][0]:[STATE,[KILLER]]})

                    return UUAS

                STATE3=RE3(THE=STATE2,ISRAN=STATE)
                print("THE",STATE3)

                def RE_OPEN(RES=None):

                    II=RE(RES)
                    II2=RE2(RES)
                    II3=RE3(THE=II2,ISRAN=II)

                    return II3
                
                def APKK(DATA):

                    TODE=RE_OPEN(DATA)

                    if len(TODE)==len(STATE3):
                        return TODE
                    else:
                        APKK(DATA=TODE)
                        
                RESS=APKK(DATA=STATE3)
                print("THE2",RESS)

                def KILL_GAME_END(END=None):

                    OS=[];IA=0;IA2=1;OS2=[]

                    for i in END:OS.append(newdata[i]);OS2.append(i)
                    AFF_END=[];ENDS=[]

                    for o in OS:
                        AFF_END=[]
                        for i in range(len(isdata)):AFF_END.append(abs(o[i]-isdata[i]))
                        ENDS.append(AFF_END);

                    print("最终清洗结果:\n",ENDS);print("最终保留下标位:\n",OS2)
                    
                    while True:
                        XKILL=0;YKILL=0;OSAP=0

                        for o in range(len(ENDS[0])):
                            if ENDS[IA][o]<ENDS[IA2][o]:
                                YKILL=YKILL+1
                                THEII=1
                                PPW=ENDS[IA][o]

                                while True:
                                    if THEII*PPW<ENDS[IA2][o]:

                                        YKILL=YKILL+1;
                                        THEII=THEII+1;
                                        print(THEII*ENDS[IA2][o],PPW);
                                        PPW=PPW+int(ENDS[IA2][o])

                                    else:break

                                print("Y权重增加 目前值为:",YKILL)

                            if ENDS[IA][o]>ENDS[IA2][o]:
                                XKILL=XKILL+1
                                THEII=1
                                PPW=ENDS[IA2][o]

                                while True:
                                    if THEII*PPW<ENDS[IA][o]:

                                        XKILL=XKILL+1;
                                        THEII=THEII+1;
                                        print(THEII*ENDS[IA][o],PPW);
                                        PPW=PPW+int(ENDS[IA][o])

                                    else:break

                                XKILL=XKILL+1

                                print("X权重增加 目前值为:",XKILL)

                        OSAP=1+IA2

                        print("最终覆盖:",OSAP);print("最终长度为:",len(ENDS))

                        if OSAP<len(ENDS):
                            if XKILL>YKILL:

                                pass

                            else:

                                IA=IA2

                            IA2=IA2+1
                        if OSAP==len(ENDS):

                            print("进入预测值结果判断")
                            print("X偏重:",XKILL,"Y偏重:",YKILL)

                            if XKILL<YKILL:

                                print("返回预测值XKILL")
                                SUPEREND2SS=OS2[IA]
                                print("返回值是:",SUPEREND2SS)
                                return SUPEREND2SS

                                break

                            if XKILL>YKILL:

                                SUPEREND1SS=OS2[IA2]
                                return SUPEREND1SS

                                break

                            if XKILL==YKILL:

                                SUPEREND3SS=IA
                                return SUPEREND3SS

                                break

                THEEND=KILL_GAME_END(RESS)

                return target[THEEND]


    #ARELUSS 杀人游戏算法原型 (已成功)
    class AIODO93_KILLGAME(object):
        #传入 isdata就是预测的特征 newdata是已经有的特征 target是已经有的目标值 isrange代表范围 debug代表死否启动调试
        def KILL(isdata=None,newdata=None,target=None,isrange=None,debug=False):

            def ABS_NUM(OPEN=newdata,OPEN2=isdata):

                DATA=[];DATA2=[];index=0

                for i in OPEN:
                    DATA=[]
                    try:
                        for o in range(len(OPEN)):
                            AIODO=isdata[o]-i[o]
                            DATA.append(abs(AIODO))
                    except Exception:
                        pass

                    DATA2.append([DATA,[index]])
                    index=index+1

                return DATA2

            def D_value(DATA=None,distance=None):

                DICTS=[];DICTS2=[];DICTS3=[];KILLER=0;DICT4=[];OPEN=0

                for i in range(len(DATA)):
                    DICTS.append(DATA[i][1][0])
                    DICTS2.append(DATA[i][0])

                for i in DICTS2:
                    DICRS3=[];KILLER=0
                    for o in i:
                        if o > distance:
                            KILLER=KILLER+1
                        DICRS3.append(o)
                    DICT4.append([DICRS3,[KILLER],[DICTS[OPEN]]]);OPEN=OPEN+1

                return DICT4
 
            def distance(DATA=None):

                OS=0

                for i in isdata:
                    OS=OS+i
                OS=OS/len(isdata)

                return OS

            def Delete_value(DATA=None):

                STATE=int(DATA[0][1][0]);ONE_STATE=[]

                for i in range(len(DATA)):
                    THE=int(DATA[i][1][0])

                    if debug==True:print("判断",DATA[i])

                    try:
                        if THE > STATE:
                            if debug==True:
                                print("已抹除",DATA[i])
                        if THE < STATE:STATE=THE;ONE_STATE.append(DATA[i])
                        if THE == STATE:ONE_STATE.append(DATA[i])
                    except Exception:
                        pass

                return ONE_STATE
 
            def Delete_value_2(DATA=None):

                PP=0;DD=0;KK=[]

                for i in range(len(DATA)):
                    DD=0
                    THE=DATA[i][0]
                    for o in THE:
                        DD=o+DD
                    KK.append([DD,DATA[i][2]])

                return KK
  
            def end(DATA=None):

                index=0;IS=DATA[0][0]
                END="S"

                for i in range(len(DATA)):

                    THE=DATA[i][0];
                    if IS==THE:pass
                    if IS>THE:IS=THE;END=DATA[i];
                    if IS<THE:pass

                if END=="S":
                    return DATA[0]

                return END
  
            def return_value(DATA):

                if len(DATA)==2:
                    OO=DATA[1][0]
                    return target[OO]
                else:
                    try:
                        OO=DATA[0][1][0]
                        return target[OO]
                    except Exception:
                        return None

            if debug==True:print("开始计算绝对值")
            ABS_NUMS=ABS_NUM(OPEN=newdata,OPEN2=isdata)
            if debug==True:print("绝对差值通过")


            if debug==True and isrange==None:print("没有指定范围范围自动等于平均值")
            if isrange==None:isrange=int(distance(DATA=isdata))


            if debug==True:print("权重判断开始")
            D_values=D_value(DATA=ABS_NUMS,distance=isrange)
            if debug==True:print("判断完毕 获取值如下:\n",D_values)


            if debug==True:print("清洗开始")
            Delete_Values=Delete_value(DATA=D_values)
            if debug==True:print("清洗结束 获取值如下:\n",Delete_Values)


            if debug==True:print("开始获取总和")
            Delete_Values2=Delete_value_2(DATA=Delete_Values)
            if debug==True:print("获取值如下:\n",Delete_Values2)


            if debug==True:print("第二轮清洗开始")
            ENDS=end(DATA=Delete_Values2)
            if debug==True:print("获取值如下\n",ENDS)


            if debug==True:print("最终清洗开始")
            OEND=return_value(DATA=ENDS)
            if debug==True:print("最终清洗结束")

            return [OEND]


#AIODO93人工智能原型   
class AIODO93_Count(object):

    #新增额外参数 Count 计算次数 默认1
    def KILLGAME(isdata=None,newdata=None,target=None,isrange=None,debug=False,Count=None):

        if Count==None:
            Count=1
        IOAP=[]

        AAR=isdata;NNR=newdata;PPR=target;IIR=isrange

        if IIR==None:
            P=0
            for i in isdata:
                P=P+i
            IIR=int(P/len(isdata))

        if debug == False:
            OOR=False
        else:
            OOR=True

        for i in range(Count):
            END=AIODO93_NUM.AIODO93_KILLGAME.KILL(isdata=AAR,newdata=NNR,target=PPR,isrange=IIR,debug=OOR)
            IOAP.append(END)
            IIR=IIR+IIR
            if debug==True:print("AI搜捕距离",IIR)

        if debug==True:print(IOAP)

        AOS=[];AO=0

        for i in target:
            AO=0
            if debug==True:print("搜索维度",i)
            for o in IOAP:
                if o[0]==i:
                    AO=AO+1
            AOS.append(AO)

        if debug==True:print(AOS)

        index=0
        OPS=[AOS[0],0];KALI="s"

        for i in AOS:

            if debug==True:print("编号投票",index,i)
            if i==OPS[0]:pass
            if i>OPS[0]:KALI=[i,index]
            if i<OPS[0]:pass
            index=index+1

        if debug==True:print("结果",KALI,OPS)

        if KALI=="s":
            OAA=OPS[1]
        else:
            OAA=KALI[1]
        
        return [target[OAA]]


#人工智能原型 
class AI(object):

    #人工智能模型启动
    def state(data=None,mod=None,debug=False):

        DDS=[];DDS2=[]

        for i in mod:
            AI=joblib.load(i)
            END=AI.predict(data)
            DDS.append(END)
        
        for i in DDS:
            DDS2.append(i[0])

        IA=set(DDS2)
        OAP=[]

        for i in IA:
            OAP.append(i)

        TTE=[]
        OA=[]

        for o in range(len(OAP)):
            for i in DDS2:
                if i==OAP[o]:
                    try:
                        TTE[o]=TTE[o]+1
                    except Exception:
                        TTE.append(0)
                        TTE[o]=TTE[o]+1

        SAT=AIODO93_list.list_max(TTE)

        if debug==True:print(DDS2)

        return [OAP[SAT[1]]]
        
    #Count All
    class ALUENA_ALL():

        #学习 data=为学习的资料 target为学习资料对应的答案 path为学习经验存储路径文件夹 modname为模型名字
        def create_model(data=None,target=None,path=None,modname=None):

            modlist=[]

            def KNN():

                the_path=path+modname+"1"+".pkl"
                modlist.append(the_path)
                AI1=KNeighborsClassifier(n_neighbors=1)
                AI1.fit(data,target)
                joblib.dump(AI1,the_path)

            def IO_ECHO():

                the_path=path+modname+"2"+".pkl"
                modlist.append(the_path)
                AI2=LogisticRegression()
                AI2.fit(data,target)
                joblib.dump(AI2,the_path)

            def IO_TREE():

                the_path=path+modname+"3"+".pkl"
                modlist.append(the_path)
                AI3=DecisionTreeClassifier()
                AI3.fit(data,target)
                joblib.dump(AI3,the_path)


            KNN()

            IO_ECHO()

            IO_TREE()

            return modlist


    #KNN
    class ALUENA_KNN():

        #KNN 算法
        def create_model(data=None,target=None,path=None,modname=None):

            modlist=[]

            def KNN():

                the_path=path+modname+"1"+".pkl"
                modlist.append(the_path)
                AI1=KNeighborsClassifier(n_neighbors=1)
                AI1.fit(data,target)
                joblib.dump(AI1,the_path)
            

            KNN()

            return modlist


#PYTHON常用小实例
class PYTHON(object):

    def CF99(num=10):
        
        for i in range(num):
            print("")
            for j in range(i):
                print(f"{j+1}*{i}={(j+1)*i}",end="\t")

                