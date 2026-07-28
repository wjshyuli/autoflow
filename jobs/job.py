from jobs.check_mes import check_output_f3_1,check_output_f3_2,check_output_f3_3,check_mold,check_mold_f4
from jobs.sent_ding import sent_ding_f3,sent_ding_mold,sent_ding_mold_f4

#三分厂推送产量任务，计算当前一个小时的硫化成型产量和胎胚库存
def job1():
    try:
        a=check_output_f3_1()
        b,machine_list,avg=check_output_f3_2()
        print(machine_list)
        c=check_output_f3_3()
        sent_ding_f3(b,a,c,machine_list,avg)
    except Exception as e:
        logger.exception(e)


def job2():
    try:
        a=check_mold()
        sent_ding_mold(a)
        b=check_mold_f4()
        sent_ding_mold_f4(b)
    except Exception as e:
        logger.exception(e)

if __name__=="__main__":
    job1()