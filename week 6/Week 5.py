def Hello():
    print ("Hello World!")
    print ("hehe")

def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hi"

print greet("es")



def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,4)
print x
