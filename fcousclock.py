import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print("倒计时: {:02d}:{:02d}".format(*divmod(seconds, 60)))
        time.sleep(1)
        seconds -= 1
    print("时间到！")

focus_time = 25 # 以分钟为单位
focus_timer(focus_time)
