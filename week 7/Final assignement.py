largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    try:
        n = int(num)
    except:
        print ("Invalid input")
    if largest is None:
        largest = n
    elif largest < n:
        largest = n

    if smallest is None:
        smallest = n
    elif smallest > n:
        smallest = n

    print largest,smallest
    if num == "done" :
        break

print "Maximum", largest
print "Minimum", smallest