'''
Money Exchange program
Takes in a currency and a value and changes it to a different currency
'''
currency = raw_input("What is your currency? (dollars/euros)")
money = input("Enter your amount: ") 

if currency == 'dollars':
    euros = money * 0.92
    print "Your", money, "dollars are", euros, "euros"
    
elif currency == 'euros':
    dollars = money * 1.09
    print "Your", money, "euros are", dollars, "dollars"
elif currency == 'won':
    won = money * 0.00090
    print "Your", money, "won are", won, "dollars."
else: 
    print"Sorry your currency is not supported for now"
