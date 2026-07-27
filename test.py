from datetime import datetime, timedelta  
import requests
import pandas as pd
from logger import logger

def check_output_f3_3():
    logger.info("三分厂硫化产量检查")
    url='http://10.3.10.64:18080/Weblhscjl/Frm_iQuery'

    body={

#   "sczl": 0,
#   "bzzl": 0,
#   "lhzsj": 0,


#   "lhTime": 0,
#     "sl": 0,


      "lhlx": "0",
  "startDate": "2026-07-25 14:00:00",
  "endDate": "2026-07-25 14:59:59",

  "isbhtm": "1",

}


    



    res=requests.post(url,json=body)
    logger.info(res.status_code)
    result=res.json().get("Object")
    account=len(result)
    print(result[0])

    return account

if __name__=="__main__":
    a=check_output_f3_3()
    print(a)