from logger import logger
from datetime import datetime, timedelta
import requests
import pandas as pd


#-----三分厂产量机胎胚库存提醒
#胎胚库存
def check_output_f3_1():
    logger.info("三分厂胎胚库存检查")
    url='http://10.3.10.64:18080/WebCxTptj/Frm_iQuery'
    res=requests.post(url,json={})
    logger.info(res.status_code)
    result=res.json().get("Object")
    account=0
    for item in result:
        account+= item['slDecimal']
    return account
#查最近一小时的成型、硫化产量
def check_output_f3_2():
    logger.info("三分厂成型二段产量检查")
    url='http://10.3.10.64:18080/WebCxsctj/Frm_iQuery'
    now = datetime .now().replace(microsecond=0,second=0,minute=0)
    et=now-timedelta(seconds=1)
    st=now-timedelta(hours=1)
    body={
    "startDate":str(st),
    "endDate":str(et)
    }
    print(body)
    res=requests.post(url,json=body)
    logger.info(res.status_code)
    result=res.json().get("Object")
    account=0
    avg1=0
    machine_list=[]
    for item in result:
        if len(item['SbName'])==5:
            account+= item['Sl']
            avg1+=1
            machine_list.append(f"{item["SbName"]}:{item['Sl']}")
            # print(f"{item['SbName']}:{item['Sl']}")
        elif len(item['SbName'])==6 and item['SbName'][-1]=='2':
            account+= item['Sl']
            avg1+=1
            machine_list.append(f"{item["SbName"]}:{item['Sl']}")
            # print(f"{item['SbName']}:{item['Sl']}") 
    avg=account/avg1
    print(avg1)
    avg=round(avg)
    return account,machine_list,avg
    
def check_output_f3_3():
    logger.info("三分厂硫化产量检查")
    url='http://10.3.10.64:18080/Weblhscjl/Frm_iQuery'
    now = datetime .now().replace(microsecond=0,second=0,minute=0)
    et=now-timedelta(seconds=1)
    st=now-timedelta(hours=1)
    body={
        #   "sczl": 0,
        #   "bzzl": 0,
        #   "lhzsj": 0,
        #   "lhTime": 0,
        #     "sl": 0,   抓包的时候带的数据
        "startDate":str(st),
        "endDate":str(et),
        "lhlx": "0",       #补码，0不包含，1包含
        "isbhtm": "1",      #虚拟条码，0不包含，1包含

    }
    print(body)
    res=requests.post(url,json=body)
    logger.info(res.status_code)
    result=res.json().get("Object")
    account=len(result)

    return account
    
# 检查当日产量
def check_output_f3_4():
    logger.info("today三分厂成型二段产量检查")
    url='http://10.3.10.64:18080/WebCxsctj/Frm_iQuery'
    now = datetime .now()
    if now.hour<7:
        st=(now-timedelta(days=1)).replace(hour=7,minute=0,second=0,microsecond=0)
    else:
        st=now.replace(hour=7,minute=0,second=0,microsecond=0)
    et=(now+timedelta(hours=8)).replace(microsecond=0) # 防止有些机器时间不对
    body={
    "startDate":str(st),
    "endDate":str(et)
    }
    print(body)
    res=requests.post(url,json=body)
    logger.info(res.status_code)
    result=res.json().get("Object")
    account=0
    for item in result:
        if len(item['SbName'])==5:
            account+= item['Sl']
    
            
            
        elif len(item['SbName'])==6 and item['SbName'][-1]=='2':
            account+= item['Sl']

    return account

    
def check_output_f3_5():
    logger.info("当日三分厂硫化产量检查")
    url='http://10.3.10.64:18080/Weblhscjl/Frm_iQuery'
    now = datetime .now()
    if now.hour<7:
        st=(now-timedelta(days=1)).replace(hour=7,minute=0,second=0,microsecond=0)
    else:
        st=now.replace(hour=7,minute=0,second=0,microsecond=0)
    et=(now+timedelta(hours=8)).replace(microsecond=0) # 防止有些机器时间不对

    
    body={
        #   "sczl": 0,
        #   "bzzl": 0,
        #   "lhzsj": 0,
        #   "lhTime": 0,
        #     "sl": 0,   抓包的时候带的数据
        "startDate":str(st),
        "endDate":str(et),
        "lhlx": "0",       #补码，0不包含，1包含
        "isbhtm": "1",      #虚拟条码，0不包含，1包含

    }
    print(body)
    res=requests.post(url,json=body)
    logger.info(res.status_code)
    result=res.json().get("Object")
    account=len(result)

    return account

    


    
#-------mold------
url_map={
    1:"http://10.3.10.61:18080/WebJtggsz/Frm_iQuery",
    2:"http://10.3.10.62:18080/WebJtggsz/Frm_iQuery",
    3:"http://10.3.10.64:18080/WebJtggsz/Frm_iQuery",
    4:"http://10.3.10.64:18081/WebJtggsz/Frm_iQuery",
}
def check_mold_f(url):
    res=requests.post(url=url,json={})
    result=res.json().get("Object")
    df=pd.DataFrame(result)
    logger.info(res.status_code)
    df["ys"] = pd.to_numeric(
                df["ys"],
                errors="coerce"
                ).fillna(0).astype(int)

    df2 = df.loc[df["ys"] < 20, ["sbid","dso","ys"]]
    data=df2.values.tolist()
    print(data)
    return data


def check_mold():
    data_list=[]

    for k,v in url_map.items():
        data_list.append(check_mold_f(v))
    
    return data_list

def check_mold_f4():
    data_list=[]
    return data_list



if __name__=="__main__":
    print(check_output_f3_5())