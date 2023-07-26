print("""
*****************************************
*               WELCOME                 *
*         We are Tour Persion.          *
*      We provide world wide tours.     *
*   And we only service too 154 people  *    
*****************************************

""")
CusTNum= int(input("How many peope will you be:"))
while True:
        
    if CusTNum > 154 :
        People =  CusTNum - 154
        print(f"Sorry we don't have this package for your group size. \nBecause {People} people left outside")
        break
    if CusTNum == 154 :
        print ("You can use our all busses. It takes 2 of 47 seat, 23 seat and VIP 7seat buss's!")
        break
    if CusTNum >= 103 and CusTNum < 154 :
        print ("You can use our one or two of 47 seat, 23 seat and VIP 7 seat buss's!")
        break
    else:
        print(""" 
        1) First package: 47 seat and slow travel
        2) Second package: 23 seat and avarage travel
        3) Third package VIP: 7 seat and fast travel

        """)
        package=int(input("You can choose package's(1, 2, or 3): "))

        
        if CusTNum> 47 and CusTNum<103:
            if package==1:
                print(" you canuse two first package buss and one second pakage buss  ")


        if CusTNum >23 and CusTNum <= 47:
            if package == 1 :
                print("Right desicion")
            if package == 2:
                leftPeople = CusTNum - 23
                if leftPeople > 23 :
                    print("you might want to choose fist pakage")
                
                if leftPeople > 7 and leftPeople <=23:
                    print(" We will offer one more Buss to your service.") 
                
                if leftPeople <=7:
                    print("You can Choose Third package with your package. ") 
            if package == 3:
                leftPeople = CusTNum - 7
                if leftPeople > 7 :
                    print("you might want to choose First pakage")
                
                if leftPeople > 0 and leftPeople <=7:
                    print(" We will offer one more Buss to your service.") 

        if CusTNum < 23 and CusTNum>7 :
            if package == 2 :
                print("Right desicion")
            if package == 1:
                leftPeople = CusTNum - 23
                if leftPeople > 23 :
                    print("you might want to choose fist pakage")
                
                if leftPeople > 7 and leftPeople <=23:
                    print(" We will offer one more Buss to your service.") 
                
                if leftPeople <=7:
                    print("You can Choose Third package with your package. ") 



