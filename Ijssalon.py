def PapiGelato():
    print ('Welkom bij Papi Gelato.')
    Gelatomarkt = input('Bent u particulier of zakelijk?')
    if Gelatomarkt == 'particulier':
        particulierbolletjes()
    if Gelatomarkt == 'zakelijk':
        zakelijkLiter()
    
slagroom = 0  
sprinkels = 0
CaramelsausHoorntje = 0
Caramelsausbakje = 0

#----------ParticulierIjs----------
def particulierbolletjes():
    bolletjes = int(input('Hoeveel bolletjes wilt u? \n'))  
    if bolletjes > 8:
        print ('Sorry, zulke grote bakken hebben we niet.')
        particulierbolletjes()
    elif bolletjes  <= 3:
        print ('Dus,' , bolletjes , 'bolletjes.')
    elif bolletjes > 3:
        print ('Dan krijgt u van mij een bakje met' , bolletjes , 'bolletjes')

    particuliersmaak(bolletjes)
    return bolletjes

#----------smaak----------
def particuliersmaak(bolletjes):
    if  (bolletjes > 3) or (bolletjes <= 3) == True:
        Smaakbol = bolletjes   
        while Smaakbol > 0:
            Smaakbol = Smaakbol - 1
            smaak = input(print('Welke smaak wilt u voor bolletje nummer', Smaakbol ,'?',' Aardbei, Chocolade of Vanille? \n'))

        if smaak == 'Aardbei' or smaak == 'Chocolade' or  smaak == 'Vanille':
            print ('bolletje{s}.', bolletjes, 'heeft het smaak,' , smaak)

        else:
            print ('Sorry dat is geen optie die we aanbieden...')
            particuliersmaak(bolletjes)
    hoorn(bolletjes)

#----------hOORN----------
def hoorn(bolletjes):
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
    topping(bolletjes,hoorntjebakje,hoorntje,bakje)

#----------TOPPINGS----------
def topping(bolletjes,hoorntjebakje,hoorntje,bakje):
    toppings = input('Wat voor topping wilt u: Slagroom,  Sprinkels of  CaramelSaus?')
    if toppings == 'Slagroom':
        slagroom == 0.50
        print ('Dat wordt Slagroom op je Bolletjes.')
    if toppings == 'Sprinkels':
        sprinkels == 0.30
        print ('Dat worden Sprinkles op je Bolletjes.')
    if toppings == 'CaramelSaus' and hoorntje == 1:
        CaramelsausHoorntje == 0.60
        print ('Dat wordt CaramelSaus met je Hoorntje.')
    if toppings == 'CaramelSaus' and bakje == 1:
        Caramelsausbakje == 0.90
        print ('Dat wordt CaramelSaus met je Bakje.')

    particulierresultaat(toppings,bolletjes,hoorntje,bakje,slagroom,sprinkels,CaramelsausHoorntje,Caramelsausbakje)

    


#----------RESULTAAT----------
def particulierresultaat(toppings,bolletjes,hoorntje,bakje,slagroom,sprinkels,CaramelsausHoorntje,Caramelsausbakje):
        verder = input(print('Dus dat wordt een  Hoorntje/bakje met' , bolletjes ,'bolletjes.','Wilt u nog meer bestellen? (Y/N)'))
        if verder == 'N':
            

            totaalTopping = slagroom + sprinkels + CaramelsausHoorntje + Caramelsausbakje
            totaal = (bolletjes*0.95) + (hoorntje*1.25) + (bakje*0.75) + totaalTopping

            print ("---------[Papi Gelato]---------")
            print ('Bolletjes'  , bolletjes , 'x 0.95  = ', (bolletjes*0.95))
            print ('Horrentje'  , hoorntje , 'x 1.25  = ', hoorntje*1.25)
            print ('Bakje'       , bakje ,   'x 0.75  = ',   bakje*0.75)
            
            print ('Toppings'       , toppings,   'x 0.75  = ',  (totaalTopping))
            print ("-------------------------------")
            print ('Totaal                               ='   ,     (totaal))

            print ('Bedankt en tot ziens!')
            quit()

        elif verder == 'Y':
            print ('Laten dan snel weer terug gaan.')
            return PapiGelato()
        else:
            ('Sorry dat is geen optie die we aanbieden...')

#----------zakelijkijs----------
def zakelijkLiter():
    Liter = int(input('Hoeveel Liter wilt u? \n'))
    zakelijksmaak(Liter)


#----------zakelijksmaak----------
def zakelijksmaak(Liter):
    smaakAardbei = int(input('Hoeveel Liter Aardbei wilt u? \n'))
    Totaalliter = Liter - smaakAardbei 
    print(Totaalliter)
    if Totaalliter > 0:
        smaakChocolade = int(input('Hoeveel Liter Chocolade wilt u? \n'))
        Totaalliter = Totaalliter - smaakChocolade
        print(Totaalliter)
    if Totaalliter > 0:
        smaakVanille = int(input('Hoeveel Vanille Chocolade wilt u? \n'))
        Totaalliter = Totaalliter - smaakVanille
        print(Totaalliter)

    zakelijkresultaat(Liter)




def zakelijkresultaat(Liter):
    print ("---------[Papi Gelato]---------")
    print ('Liter'  , Liter , 'x 9.80  = ', Liter*9.80)
    print ("-------------------------------")
    print ('Totaal                         = ', Liter*9.80 )
    print ('BTW(9%)                        = ', (Liter*9.80) / 100 * 6)

PapiGelato()
