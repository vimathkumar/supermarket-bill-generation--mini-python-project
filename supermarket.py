from datetime import datetime
date = datetime.now()
date1 = date.strftime("%d-%m-%y %H:%M:%S")

welcome = """
===========Welcome to KVK Store============
"""
print(welcome)
name = input("enter your name : ")
print("\tWelcome {}".format(name.upper()))
grocerries = """
============================
         KVK STORE
============================
ITEM            PRICE
----------------------------
Rice            Rs 45/kg
Sugar           Rs 40/kg
Salt            Rs 15/kg
Oil             Rs 180/litre
Panner          Rs 150/kg
Maggie          Rs 60/each
Boost           Rs 190/each
Colgate         Rs 80/each
============================
"""
items = {"rice": 45,"sugar": 40,"salt": 15,"oil":180,"panner":150,"maggie":60,"boost":190,"colgate":80}
total_price = 0
ilist = []
qlist = []
plist = []
inp1 = int(input("For list of items press 1 : "))
if inp1 ==1:
    print(grocerries)
    for i in range(len(items)):
        inp2 = int(input("If you want to buy press 1 or 2 for exit : "))
        if inp2==1:
            item = input("Enter your item : ")
            quantity = int(input("Enter the quantity : "))
            if item.lower() in items:
                price = items[item.lower()] * quantity
                total_price+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
            else:
                print("Sorry, your entered item is not available.")
        elif inp2 == 2:
            break 
        else:
            print("you entered wrong number...")
    if len(ilist)>0:
        inp3 = input("Can i prepare the bill? say yes or no : ")
        if inp3 == 'yes':
            if total_price!=0:
                print()
                print(17*"-","KVK MARKET",17*"-")
                print(19*" ","Laveru  ")
                print("Name :",name,8*" ","Date:",date1)
                print(20*"-","Bill",20*"-")
                print("Sno         item         quantity        price")
                for i in range(len(ilist)):
                    print(i+1,9*" ",ilist[i],9*" ",qlist[i],12*" ",plist[i])
                print("Total price :                            ",total_price)
                print(46*"-")
                gst = total_price*0.05
                print("GST :                                    ",gst)
                print(46*"-")
                print("Final Price :                           ",gst+total_price)
                print(46*"-")
                print("THANK YOU FOR VISITING \"KVK\" STORE.")
                print("Visit again {}...Have a great day :)".format(name.upper()))
                print(46*"-")
    else :
        print("THANK YOU FOR VISITING \"KVK\" STORE")
else :
    print("THANK YOU FOR VISITING KVK STORE")
