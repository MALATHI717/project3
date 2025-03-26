# myapp/crons.py
from django_cron import CronJobBase, Schedule
from myapp.models import MyModel
import datetime

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Run every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.my_cron_job' 

    def do(self):
        now = datetime.datetime.now()
        print(f"Running cron job at {now}")
        MyModel.objects.filter(expiry_date__lt=now).delete()
