age = input("How old are you?\n\n")
stock = 0
if (int(age)>= 20 and int(age) <= 25):
    stock = 95
elif (int(age)>= 26 and int(age) <= 30):
    stock = 92
elif (int(age)>= 31 and int(age) <= 35):
    stock = 90
elif (int(age)>= 36 and int(age) <= 38):
    stock = 87
elif (int(age)>= 39 and int(age) <= 40):
    stock = 84
elif (int(age)>= 41 and int(age) <= 42):
    stock = 81
elif (int(age)>= 43 and int(age) <= 44):
    stock = 79
elif (int(age)>= 45 and int(age) <= 46):
    stock = 78
elif (int(age)>= 47 and int(age) <= 48):
    stock = 77
elif (int(age)>= 49 and int(age) <= 50):
    stock = 75
elif (int(age)>= 51 and int(age) <= 52):
    stock = 72
elif (int(age)>= 53 and int(age) <= 54):
    stock = 69
elif (int(age)>= 55 and int(age) <= 56):
    stock = 66
elif (int(age)>= 57 and int(age) <= 58):
    stock = 63
elif (int(age)>= 59 and int(age) <= 60):
    stock = 60
elif (int(age)== 61):
    stock = 57
elif (int(age)== 62):
    stock = 54
elif (int(age)== 63):
    stock = 51
elif (int(age)== 64):
    stock = 48
elif (int(age)== 65):
    stock = 45
elif (int(age)>= 66 and int(age) <= 70):
    stock = 40
elif (int(age)>= 71 and int(age) <= 75):
    stock = 36
elif (int(age)>= 76 and int(age) <= 80):
    stock = 32
elif (int(age)>= 81 and int(age) <= 85):
    stock = 28
elif (int(age)>= 86):
    stock = 25

if (int(age) < 20):
    print("\nYou are too young to be investing!\n")

else:
    print("\nYou should invest", stock, "% in stocks and", (100-stock), "% in fixed income.\n")


        
        
        
        
    
        