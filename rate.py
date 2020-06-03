hrs = input('Enter hours')
h = float(hrs)
rate = input('Enter rate')
r = float(rate)
if h <= 40 :
    rate = h * r
else :
    rate = (40 * r) + ( (h-40) * r * 1.5)

print (rate)
