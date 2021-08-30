
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s ', filename="logfile-wizytówka.log")
from faker import Faker
fake = Faker()

if __name__ == "__main__":
#_____________________________________Class_Begin_Here_____________________________________________________<<<<<<<<<<<<<<<
    class BaseContact :                                                 
        def __init__(self,name, phon):                                 #<--------------------------------------Konstruktor 
            self.name=name
            self.phon=phon
            self.len_name = name                       #<--@PROPERTY---Ćw 7.2__zmienna__dynamiczna_użyta w lini ...53 i 54

        def __str__(self):
            return (f'(BuisnesCard of {self.name},phon number:{self.phon})') #____, type_of_bussines {self.type_of_bussines}
        def contact(self):                                               #<-------ćw 7.2 def_contact()----wywołanie linia 50
            return print (f"Kontaktuj się z  {self.name} pod numerem PRYWATNYM:{self.phon}")
        @property
        def len_name(self):
            return self._len_name
        @ len_name.setter
        def len_name(self,name):
            self._len_name=len(name)
#_____________________________________Class__END__HERE__________________________________________<<<<<<<<<<<<<<

#_____________________________________CHild_Class_Begin________________________________________________
    class BussnesCard(BaseContact):
        
        def __init__ (self,position,business_phon,type_of_business,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.osition=position
            self.business_phon=business_phon
            self._type_of_business=type_of_business
    #_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
        @property
        def _type_of_business(self):
            return self.type_of_business

        @_type_of_business.setter
        def _type_of_business(self,value):
            self.type_of_business=value +" Sp.z.o.o"
    #_ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ 
        def contact(self):                                               #<-------ćw 7.2 def_contact()----wywołanie linia 50
                return print (f"Kontaktuj się z {self.name} pod numerem SŁUŻBOWYM : {self.business_phon}")


    #____________________________________Child_Class_End____________________________________________________


    new_card1= BaseContact(fake.name(),'111 111 111')
    new_card2= BaseContact(fake.name(),'333 333 333')
    #new_card3= BaseCard(fake.name(),'5555','KOMANDYTOWA')
    #new_card4= BaseCard("Bodzio Bombik",'2222','BlackMarket')
    print(new_card1)
    logging.info(f"otworzono program")

#______________________________________ćw_mod_7.1__lambda, iterowanie po liscie z klasami , sortowanie__________
    '''
 card_list=[new_card1,new_card2,new_card3,new_card4]
      print(new.name,new.phon,new.type_of_bussines,)
    sort=sorted(card_list,key=lambda card: card.name)
    for card in sort:
        print(card)#dla czego nie działa __str__?
    print("\n")
    sort_phon=sorted(card_list,key=lambda card: card.phon)
    for card in sort_phon:    
        print (card)
    print("zakonczenie mod 7.1 ponizej 7.2 \n ")
'''
#___________________________________ćw_mod_7.2_________________________________________________________________
new_card1.contact()
    #print (f'wypisanie  new_card.name to => {new_card1.name}')
    #print(f' typ zmiennej name to {type(new_card1.name)} a długość to {print(len(new_card1.name))}') 
print(new_card1.len_name)                                                       #<----wywołanie property.setter
print(new_card2.len_name)                                                       #<----wywołanie property.setter

#___________________________________ZADANIE ! MODUŁ 7________________________________________________________
Base_card= BaseContact(fake.name(),'111 111 111')
print (f'\n Wyświetlam dane wizytówki z klasy bazowej \n najpierw funkcja contact : {Base_card.contact()}') #____funkcja contact() clasy bazowej
Biznes_card=BussnesCard('Kasjer','123 456 789','kiosk',fake.name(),'222 222 222')
print(f' type_of_biznes obietu BiznesCard to:{Biznes_card._type_of_business}, imie, nazwisko to:{Biznes_card.name}, telefon:{Biznes_card.phon}') #__sprawdzam poprawność wpisania zmiennych
print(Biznes_card)
Biznes_card.contact()                                                                               #___funkcja contact() clasy potomnej.
Base_card.contact()                                                                                 #___funkcja contact() clasy bazowej.
print(f' zmienna dynamiczna clasy potomnej:{Base_card.len_name} , {Base_card.name}')
print(f' zmienna dynamiczna clasy potomnej:{Biznes_card.len_name},{Biznes_card.name}')
#_________________________________________Generator_Wizytówek_________________________________________________
def fake_card_generator(number,type):
    pass