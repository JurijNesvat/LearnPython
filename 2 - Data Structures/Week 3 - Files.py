#New line character
#stuff = "X\nY"
#print stuff

#Assignement1:

# Use words.txt as the file name
#try:
#    fname = raw_input("Enter file name: ")
#    fh = open(fname)
#    filenorm = fh.read()
#    filecap = filenorm.strip()
#    filecap = filecap.upper()
#    print filecap
#except:
#    print ("No such file found")
#    exit()

#Assignement 2:
fname = raw_input("Enter file name: ")
fh = open(fname)
lineamount = 0
summary = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    position = line.find("0")
    neededamount = line[position:position+6]
    neededamount = float(neededamount)
    lineamount = lineamount + 1
    summary = summary + neededamount

average = summary / lineamount
print "Average spam confidence:",average