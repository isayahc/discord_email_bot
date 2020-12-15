from src.bot import send_message
from src.email_read import wsb

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone, timedelta
from time import sleep
import os
import logging
from logging.config import fileConfig

def get_utc_time() ->datetime.time:
    now_utc_date = datetime.now(timezone.utc)
    now_utc_time = now_utc_date.time() # coverts datetime into time object
    return now_utc_time

def utc_to_nyc():
    nyc_time = get_utc_time() - timedelta(hours=5)
    return nyc_time

def wait_for_publishing(wait_minutes:int):
    #inital time is 6.am nyc or 11 utc
    while not wsb():
        sleep(60*wait_minutes)



def main():
    data = wait_for_publishing(5)
    hook_url = os.environ.get('discord_link')
    send_message(data, hook_url)

#wsb usually publishes around 6am
#start conquence then
#while not wsb
##wait x=15 mins
#else send_message(wsb())



if __name__=='__main__':
    #logger data
    logger = logging.getLogger()
    fileConfig('logging_config.ini')

    logging.debug("I'm a message for debugging purposes.")
    logging.debug(get_utc_time())
    current_time = get_utc_time()

    sched = BlockingScheduler()
    sched.add_job(
        main, 
        'cron', 
        minute =current_time.minute+5,
        hour=current_time.hour
    )
    sched.start()
