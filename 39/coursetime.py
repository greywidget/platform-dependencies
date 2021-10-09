from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
    Here is a snippet of the input file:

    Start  What is Practical JavaScript? (3:47)
    Start  The voice in your ear (4:41)
    Start  Is this course right for you? (1:21)
    ...

     Return a list of MM:SS timestamps
    """
    pattern = re.compile(r"\((\d+:\d+)\)")
    with open(COURSE_TIMES) as f:
        data = f.read()
    return re.findall(pattern, data)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
    and calculates the total duration as HH:MM:SS"""
    total_mins = 0
    total_secs = 0
    for item in timestamps:
        mins_secs = item.split(":")
        total_mins += int(mins_secs[0])
        total_secs += int(mins_secs[1])
    return str(timedelta(minutes=total_mins, seconds=total_secs))
