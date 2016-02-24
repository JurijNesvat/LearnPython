#finding the largest value

lsf = -1
print ('Before',lsf)

for i in [9,41,12,3,74,15]:
    if i > lsf:
        lsf = i
    print (lsf,i)

print ("After",lsf)



#finding the smallest value

ssf = 100
print ('Before',ssf)

for i in [9,41,12,3,74,15]:
    if i < ssf:
        ssf = i
    print (ssf,i)

print ("After",ssf)