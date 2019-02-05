print('Thank you for using our RoboAdvisory\n')
print('We offer an advanced service that will tell you how to allocate your wealth based on your age!\n\n')
choice = input("Would you like to begin?\n\t1 - Yes\n\t2 - No\n\n") #Get user input for whether to proceed or not
while (choice != "2"):                                            #While loop to keep user in program unless they choose to leave(2)
    if (choice == "1"):
        age = input("How old are you?\n\n")                         #Take user age, store as age variable

        if (int(age) >= 20 and int(age) <= 85):                   #If age is between 20 and 85, use dictionary below to choose proper stock allocation
             d = {'20':'95','21':'95','22':'94','23':'94','24':'93',
             '25':'92','26':'92','27':'92','28':'91','29':'91','30':'91',
             '31':'90','32':'90','33':'89','34':'89','35':'88',
             '36':'87','37':'86','38':'85',
             '39':'84','40':'83',
             '41':'82','42':'81',
             '43':'80','44':'79',
             '45':'78','46':'78',
             '47':'77','48':'76',
             '49':'75','50':'74',
             '51':'73','52':'72',
             '53':'70','54':'69',
             '55':'67','56':'66',
             '57':'64','58':'63',
             '59':'62','60':'60',
             '61':'57',
             '62':'54',
             '63':'51',
             '64':'48',
             '65':'45',
             '66':'44','67':'43','68':'42','69':'41','70':'40',
             '71':'39','72':'38','73':'37','74':'36','75':'36',
             '76':'35','77':'34','78':'33','79':'32','80':'32',
             '81':'31','82':'30','83':'29','84':'28','85':'27',
             }
             stock = d[age]                                     #Assign stock to value corresponding with age key in dictionary
             print('\nYou should be', stock, '% invested in stocks and', (100 - int(stock)), '% invested in bonds!\n')
             choice = input("Would you like to begin again?\n\t1 - Yes\n\t2 - No\n\n")        #Give user option to run through program again with new age choice
       
        elif (int(age) > 85):                                   #Created this to avoid needing to assign dictionary values up to highest possible age, as allocation does not change after 85
            print('\nYou should be 25 % invested in stocks and 75 % invested in bonds!\n')
            choice = input("Would you like to begin again?\n\t1 - Yes\n\t2 - No\n\n")
        
        elif (int(age) < 20):                                   #Given chart did not show allocation for users under 20, so just tell them they are too young to invest
            print('\nYou are too young to be investing!\n')
            choice = input("Would you like to begin again?\n\t1 - Yes\n\t2 - No\n\n")
        
        else:
            print('That was not a valid choice.\n')             #Prints if something besides an age is inputted, such as a word or letter
            choice = input("Would you like to begin again?\n\t1 - Yes\n\t2 - No\n\n")
    else:
        print("That is not a valid answer.")                    #Prints if user selects something other than 1 or 2 at main menu
        choice = input("Would you like to begin again?\n\t1 - Yes\n\t2 - No\n\n")

print("\nThank you and please come again!\n")                     #Prints when user chooses to quit the program