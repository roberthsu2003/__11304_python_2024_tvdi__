from crontab import CronTab
import os
cron = CronTab(user=True)
path = os.path.abspath("./lesson2.py")
job = cron.new(command=f"/opt/miniconda3/envs/venv1/bin/python '{path}'")
job.minute.every(10)
job.set_comment("Output hello world")
cron.write()