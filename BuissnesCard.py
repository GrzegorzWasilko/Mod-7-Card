
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s ', filename="logfile-wizytówka.log")
from faker import Faker
fake = Faker()

if __name__ == "__main__":
#_____________________________________Class_Begin_Here_____________________________________________________<<<<<<<<<<<<<<<
    class BuissnesCard :                                                 
        def __init__(self,name, phon, type_of_bussines):               #<--------------------------------------Konstruktor 
            self.name=name
            #self.sername=sername
            self.phon=phon
            self.type_of_bussines=type_of_bussines
            self._len_name =0                                 #<--@PROPERTY---Ćw 7.2__zmienna__dynamiczna_użyta w lini ...53

        def __str__(self):
            return f'(BuisnesCard of {self.name}, phon number{self.phon}, type_of_bussines {self.type_of_bussines})'
        def contact(self):                                               #<-------ćw 7.2 def_contact()----wywołanie linia 50
            return print (f"Kontaktuj się z  {self.name} pod numerem {self.phon}")
        @property
        def len_name(self):
            return self.len_name
        @len_name.setter
        def len_name(self,name):
            self._len_name=len(name)
#_____________________________________Class__END__HERE______________________________________________________<<<<<<<<<<<<<<

    new_card1=BuissnesCard(fake.name(),'1111','Spzoo')
    new_card2=BuissnesCard(fake.name(),'3333','SA')
    new_card3=BuissnesCard(fake.name(),'5555','KOMANDYTOWA')
    new_card4=BuissnesCard(fake.name(),'2222','BlackMarket')
    print(new_card1)
    logging.info(f"otworzono program")

#______________________________________ćw_mod_7.1__lambda, iterowanie po liscie z klasami , sortowanie__________
    card_list=[new_card1,new_card2,new_card3,new_card4]
    for new in card_list :
        print(new.name,new.phon,new.type_of_bussines,)
    sort=sorted(card_list,key=lambda card: card.name)
    for card in sort:
        print(card)#dla czego nie działa __str__?
    print('\n')
    sort_phon=sorted(card_list,key=lambda card: card.phon)
    for card in sort_phon:    
        print (card)
    print("zakonczenie mod 7.1 ponizej 7.2 \n\n")
#___________________________________ćw_mod_7.2_________________________________________________________________
new_card1.contact()
print (f'wypisanie  new_card.name to => {new_card1.name}')
print(f' typ zmiennej name to {type(new_card1.name)} ')          # name to string len powinno zadzałać
print(new_card1.len_name)     #!!!!!!!!!!!!!!!!!!!!!!!!!!#nie działa !!!!!!!!!!!!!!!!!!!!!!!!!!!

#_________________________________________THE_END_______________________________________________________________