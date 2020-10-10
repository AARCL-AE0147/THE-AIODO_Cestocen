import AIODO93

def request_split(DATA):
    return AIODO93.AWKFaction.web_request.request_split(DATA)

def HTML_IO(DATA):
    return AIODO93.AWKFaction.web_request.url_of_HTML(DATA,"ARELUSS_TO_FILE_IS")

def handers_IO_key(DATA):
    return AIODO93.AWKFaction.web_request.del_url_of_HTML(DATA,"ARELUSS_TO_FILE_IS")

def file_to(DATA):
    try:
        print(f"{DATA['Host']}->{DATA['request']}-->{DATA['url']}")
        PD=DATA["ARELUSS_TO_FILE_IS"]
        PER=AIODO93.AWKFaction.DATA(path=DATA["url"])
        
        PER=AIODO93.AWKFaction.return_request.return200OFDATA(PER)

        return PER
    except Exception:
        print("不存在key-跳过",file_to.__name__)
        return DATA