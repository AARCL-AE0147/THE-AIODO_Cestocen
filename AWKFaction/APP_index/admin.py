import AIODO93

retuper=AIODO93.AWKFaction.return_request
HTML_load=AIODO93.AWKFaction.HTML
data_encode=AIODO93.AWKFaction.return_encode

def admin_return(request):

    PP=HTML_load("./HTML/CES.html")
    
    return retuper.return200(PP)

def the404(request):
    return request

def admin_return2(request):
    PP=HTML_load("./HTML/CES2.html")

    return retuper.return200(PP)

def admin_return3(request):
    return retuper.return302("/admin.html")

def setcookie(request):
    PP=HTML_load("./HTML/CES3.html")
    PA=retuper.setcookie200(PP,{"USER":"ARELUSS","PASSWD":"13820354138"},2000)
    return PA

def setcookie_of_new(request):
    print(request)
    PA=retuper.setcookie_new({"USER":"AE0147","PASSWD":"1929"},2300)
    return PA

def cookie_del(request):
    try:
        PODO=request["Cookie"]
        UA=PODO["PASSWD"]
        UA2=PODO["USER"]
        if len(UA2)==0:
            
            return retuper.return302("admin")
        return retuper.delcookie(COOKIE=["PASSWD","USER"])

    except Exception as O:
        return retuper.return302("/")