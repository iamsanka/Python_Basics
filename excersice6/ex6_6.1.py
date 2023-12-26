#create the function time to converts seconds in to time format

def time(secs):
    #convert to sections
    hours=int(secs/3600)
    secs=secs%3600
    minutes=int(secs/60)
    secs=secs%60

    #get theh string value
    hours=str(hours)
    minutes=str(minutes)
    secs=str(secs)

    #set for 2 digit value
    if(2 > len(hours)) :
        hours="0"+hours

    if(2 > len(minutes)) :
        minutes="0"+minutes

    if(2 > len(secs)) :
        secs="0"+secs

    print(hours+":"+minutes+":"+secs)

    return hours,minutes,secs

time(10021)