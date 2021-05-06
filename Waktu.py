from time import time, ctime


prev_time = ""
the_time = ctime(time())
if prev_time != the_time:
    print 'Waktu Sekarang: ' ,ctime(time())
    prev_time = the_time
