def computepay(time,rate):
    if time>40:
        extra=time-40
        time=time-extra
        extra*=3/2
        extra*=rate
        time*=rate
        return (time+extra)
    else:return time*rate
hrs=float(input('enter the Time'))
rate=float(input('enter the rate'))
print("pay",computepay(hrs,rate))
        
           