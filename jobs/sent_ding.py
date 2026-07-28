from logger import logger
import requests
from datetime import datetime, timedelta


webhooktest="https://oapi.dingtalk.com/robot/send?access_token=43fbdf590a9c441e4372f0fc6bc2efddf7262a034c2590dcdba7bc180c5502f0"
# 三分厂产量推送群
webhook1='https://oapi.dingtalk.com/robot/send?access_token=bd74aace201c4817a74793cc5ef4b92e9e89e4b509b7aee829ae72141fe80591'

#一到四分厂模具推送群
webhook2="https://oapi.dingtalk.com/robot/send?access_token=ad26e1b22dcfcf6497dd2f3c899ed955b2d6c69e79d3c65fea5993fd7d2d5535"
webhook3="https://oapi.dingtalk.com/robot/send?access_token=069d1e2eb088d85359547601fad37cce36e77b606696317f3b0d133786c75a14"
webhook4="https://oapi.dingtalk.com/robot/send?access_token=f7e0f06c81adc2193504dd7a14fc816ab1be7c752bcb56e29eafba66a07a0854"
webhook5="https://oapi.dingtalk.com/robot/send?access_token=b83741df7b04f56feaef6ccb86d65c9cfee44fe3312710e2804c2d5bb358b5a4"
webhook6="https://oapi.dingtalk.com/robot/send?access_token=f6e43029c381bf2335055c18515162fd970e8c124680db06ee0dab037e81605b"




def sent_ding(url,text):
    logger.info('发送钉钉消息')
    body={
        "msgtype": "actionCard",
        "actionCard": {
            "title": "消息推送", 
            "text": text,
        },
    }
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url=url, json=body, headers=headers)
    logger.info(f"钉钉消息响应：{resp.json()}")


def sent_ding_f3(num1,num2,num3,machine_list,avg):
    now = datetime .now().replace(microsecond=0,second=0)
    today=now.date()
    hour2=now.hour
    hour1=(now-timedelta(hours=1)).hour
    str1=""
    for item in machine_list:
        str1+=f'\n\n {item}'

    text=f"### {now} 产量推送：\n\n 时间范围：{hour1}到{hour2}点  \n\n 成型产量：{num1}  \n\n 胎胚库存：{num2} \n\n 硫化产量：{num3}\n\n ---\n\n---\n\n成型产量\n\n {str1}\n\n合计：{num1}\n\n平均:{avg}\n\n"
    
    sent_ding(url=webhooktest,text=text)


def sent_ding_mold(text_list):
    now = datetime.now().replace(microsecond=0,second=0)
    text=f"### {now}\n\n 换模机台提醒：\n\n---\n\n"
    #一分厂
    text1=text_list[0]
    text11=text
    for item in text1:
        text11=text11+f'\n\n 机台{item[0]}{item[1]}：计划剩余数：{item[2]}'
    sent_ding(url=webhook2,text=text11)
    #二分厂
    text2=text_list[1]
    text22=text
    for item in text2:
        text22=text22+f'\n\n 机台{item[0]}{item[1]}：计划剩余数：{item[2]}'
    sent_ding(url=webhook3,text=text22)
    #三分厂
    text3=text_list[2]
    text33=text
    for item in text3:
        text33=text33+f'\n\n 机台{item[0]}{item[1]}：计划剩余数：{item[2]}'
    sent_ding(url=webhook4,text=text33)

    text4=text_list[3]
    text44=text
    for item in text4:
        text44=text44+f'\n\n 机台{item[0]}{item[1]}：计划剩余数：{item[2]}'
    sent_ding(url=webhook5,text=text44)

def sent_ding_mold_f4(text):
    sent_ding(url=webhook6,text=text)




if __name__=="__main__":
    sent_ding_f3(1,2,3)
    