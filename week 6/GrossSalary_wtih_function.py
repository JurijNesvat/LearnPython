#def GrossSalary(hrs,rte):
#print('normal hours:',h)
#print('additional hours:',addh)

 #   if hrs <= 40.0:
  #      pay = hrs * rte
#    else:
#        pay = (40.0 * rte) + (15 * (hrs - 40.0))

#    return pay

#print (GrossSalary(45,10))


def computepay(h,r):
    if h <= 40.0:
        pay = h * r
    else:
        pay = (40.0 * r) + (1.5 * r * (h - 40.0))
    return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rte = raw_input("Enter Rate:")
r = float(rte)

p = computepay(h,r)
print (p)