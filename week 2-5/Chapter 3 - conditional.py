#x = 5
#if x < 10:
#    print ('Smaller')

#if x >= 10:
#    print ('Bigger')
#else:
#    print ('else was used')


#if x < 5:
#    print ('x<5')
#elif x < 10:
#    print ('x<10')
#elif x < 20:
#    print ('x<20')
#else:
#    print ('something else')

#astr = 'vega'
#try:
#    istr = int(astr)
#except:
#    istr = -1
#print ('printing',istr)

#working hours conditional
#hours = input('Enter working hours amount:')
#try:
#    hours = int(hours)
#except:
#    print ('numbers only!!!')

#rate = input ('Enter rate:')
#try:
#    rate = int(rate)
#except:
#    print ('numbers only!!!')

#if hours <= 40:
#    pay = hours * rate
#else:
#    pay = hours * 1.5 * rate
#print ('To pay:',pay)


#hrs = input("Enter Hours:")
#h = float(hrs)
#allh = h
#rte = input("Enter Rate:")
#r = float(rte)

#if h > 40.0:
#    addh = h - 40.0
#    h = h - addh

#print('normal hours:',h)
#print('additional hours:',addh)

#if allh <= 40.0:
#    pay = h * r
#else:
#    pay = (h * r) + (addh * r * 1.5)

#print (pay)





score = input("Enter Score: ")
score = float(score)

if score > 0 and score <= 1.0:
    if score >= 0.9:
        print ('A')
    elif score >= 0.8:
        print ('B')
    elif score >= 0.7:
        print ('C')
    elif score >= 0.6:
        print ('D')
    elif score < 0.6:
        print ('F')
else:
    print('The entered score is out of range!')