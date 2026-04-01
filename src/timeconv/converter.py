def second_to_minute(second):
    if second >= 60:
        minutes, seconds = divmod(second, 60)
        print(f"{int(minutes)} minute(s) : {round(seconds, 2)} second(s)")
    else:
        print(f"{round(second, 2)} second(s)")

def second_to_hour(second):
    if second >= 86400:
        days, remainder = divmod(second, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{int(days)} day(s) : {int(hours)} hour(s) : {int(minutes)} minute(s) : {round(seconds, 2)} second(s)")
        
    elif second >= 3600:
        hours, remainder = divmod(second, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{int(hours)} hour(s) : {int(minutes)} minute(s) : {round(seconds, 2)} second(s)")
        
    elif second >= 60:
        minutes, seconds = divmod(second, 60)
        print(f"{int(minutes)} minute(s) : {round(seconds, 2)} second(s)")
        
    else:
        print(f"{round(second, 2)} second(s)")

def minute_to_hour(minute):
    if minute >= 1440: 
        days, remainder = divmod(minute, 1440)
        hours, mins = divmod(remainder, 60)
        print(f"{int(days)} day(s) : {int(hours)} hour(s) : {int(mins)} minute(s)")
    elif minute >= 60:
        hours, mins = divmod(minute, 60)
        print(f"{int(hours)} hour(s) : {int(mins)} minute(s)")
    else:
        print(f"{round(minute, 2)} minute(s)")

def minute_to_second(minute):
    print(f"{round(minute*60, 5)} second(s).")

def hour_to_minute(hour):
    print(f"{round(hour*60, 5)} minute(s).")

def hour_to_second(hour):
    print(f"{round(hour*3600, 5)} second(s).")
