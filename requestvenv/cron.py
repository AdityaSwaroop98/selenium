from crontab import CronTab
cron = CronTab(user='root')
job = cron.new(command='sudo python3 index.py')
job.minute.every(1)
cron.write()