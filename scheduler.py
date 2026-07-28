from apscheduler.schedulers.background import BackgroundScheduler
from jobs.job import job1,job2



scheduler = BackgroundScheduler()

# ===== 调度入口 =====

def start():

    scheduler.add_job(
        job1,
        "cron",
        minute="0",
        id="job1",
        name="三分厂产量推送任务"
    )

    scheduler.add_job(
        job2,
        "cron",
        # minute="*/15",
        minute="0",
        id="job2",
        name="模具中新推送任务"
    )

    scheduler.start()



