def ijs():
    print ('Welkom bij Papi Gelato.')
    bolletjes = int(input('Hoeveel bolletjes wilt u? \n'))
    if bolletjes > 8:
        print ('Sorry, zulke grote bakken hebben we niet.')
        ijs()
    elif bolletjes  <= 3:
        print ('Dus,' , bolletjes , 'bolletjes.')
    elif bolletjes > 3:
        print ('Dan krijgt u van mij een bakje met' , bolletjes , 'bolletjes')
    return bolletjes 
    
     
def smaak(bolletjes):
    if  (bolletjes > 3) or (bolletjes <= 3) == True:
        Smaakbol = bolletjes   
        while Smaakbol > 0:
            Smaakbol = Smaakbol - 1
            smaak = input(print('Welke smaak wilt u voor bolletje nummer', Smaakbol ,'?',' Aardbei, Chocolade, Munt of Vanille? \n'))

            if smaak == 'Aardbei' or smaak == 'Chocolade' or smaak == 'Munt' or smaak == 'Vanille':
                print ('bolletje{s}.', bolletjes, 'heeft het smaak,' , smaak)

            else:
                print ('Sorry dat snap ik niet...')
                Smaakbol = Smaakbol + 1

    Aardbei = 'Aardbei' and 0
    Chocolade = 'Chocolade' and 0 
    Munt = 'Munt' and 0 
    Vanille = 'Vanille' and 0 

    if Smaakbol <= 0:
        
        print ("---------[Smaken]---------") 
        print (int(Smaakbol) , "X" , smaak ) 
        print (int(Smaakbol) , "X" , smaak )
        print (int(Smaakbol) , "X" , smaak ) 
        print (int(Smaakbol) , "X" , smaak )                
        print ("--------------------------") 


def hoorn():
    hoorntjebakje = input('Wilt u deze bolletje(s). in een hoorntje of een bakje? \n')
    hoorntje = 'hoorntje' and 0
    bakje = 'bakje' and 0

    if hoorntjebakje == 'bakje':
        bakje = 1
        print ('Dat wordt 1 Bakje.')
    elif hoorntjebakje == 'hoorntje':
        hoorntje = 1
        print ('Dat wordt 1 Hoorntje.')
    else:
        hoorn()

        

def topping(hoorntjebakje,hoorntje,bakje):
    if hoorntjebakje == True:
        toppings = input('Wat voor topping wilt u:  Geen,  Slagroom,  Sprinkels of  CaramelSaus?')
        if toppings == 'Slagroom':
            slagroom = 0.50
            print ('Dat wordt 1 Slagroom.')
        if toppings == 'Sprinkels':
            sprinkels = 0.30
            print ('Dat wordt 1 Sprinkles.')
        if toppings == 'CaramelSaus' and hoorntje == 1:
            CaramelsausHoorntje = 0.60
            print ('Dat wordt 1 CaramelSaus Hoorntje.')
        if toppings == 'CaramelSaus' and bakje == 1:
            Caramelsausbakje = 0.90
            print ('Dat wordt 1 CaramelSaus Bakje.')
        if (toppings == 'Slagroom') and (toppings == 'Sprinkels') and (toppings == 'CaramelSaus' and hoorntje == 1) and (toppings == 'CaramelSaus' and bakje == 1):
            print ('Sorry, dat snap ik niet...')


def resultaat(toppings,bolletjes,hoorntje,bakje,slagroom,sprinkels,CaramelsausHoorntje,Caramelsausbakje):
    if (toppings == 'Slagroom') and (toppings == 'Sprinkels') and (toppings == 'CaramelSaus' and hoorntje == 1) and (toppings == 'CaramelSaus' and bakje == 1):
        verder = input(print('Dus dat wordt een  Hoorntje/bakje met' , bolletjes , 'bolletjes en', toppings ,'Wilt u nog meer bestellen? (Y/N)'))
        if verder == 'N':
            
            totaalBolletjes = bolletjes*1.10
            totaalHoorntje  =  hoorntje*1.25
            totaalBakje     =  bakje*0.75
            totaalTopping = slagroom + sprinkels + CaramelsausHoorntje + Caramelsausbakje
            totaal = totaalBolletjes + totaalHoorntje + totaalBakje + totaalTopping

            print ("---------[Papi Gelato]---------")
            print('Bolletjes'  , bolletjes , 'x 1.10  = ', totaalBolletjes)
            print('Horrentje'  , hoorntje , 'x 1.25  = ', totaalHoorntje)
            print('Bakje'       , bakje ,   'x 0.75  = ',  totaalBakje)
            
            print('Toppings'       , toppings ,   'x 0.75  = ',  totaalTopping)
            print ("-------------------------------")
            print ('Totaal                               ='   ,     totaal)

            print ('Bedankt en tot ziens!')
            quit()

        elif verder == 'Y':
            print ('Laten dan snel weer terug gaan.')
            return ijs()
        else:
            ('Sorry, dat snap ik niet...')

bol = ijs()
smaak(bol)
top = hoorn()
topping(top)
resultaat()