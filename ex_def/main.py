def computepay(jam,rate):
    #print('in computepay', jam, rate)
    if jam > 40:
        reg = jam * rate
        otp = (jam - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = fh * fr
    print("pay : ",pay)
    return(pay)


sh = input("masukan Jam : ")
sr = input("masukan Rate: ")
fh = float(sh)
fr = float(sr)

computepay(fh,fr)


