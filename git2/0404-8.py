a=int(input("성적?:"))

if a>=60:
    if a>=70:
        if a>=80:
            if a>=90:
                print ("A")
            else: print ("B")
        else: print ("C")
    else: print ("D")
else: print ("F")

print ("학점입니다.^^")

if a<90:
    if a<80:
        if a<70:
            if a<60:
                print ("F")
            else:
                print ("D")
        else:
            print ("C")
    else:
        print ("B")
else:
    print ("A")

print ("----------")
