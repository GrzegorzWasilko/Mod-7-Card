
import logging
from re import X
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s ', filename="logfile-wizytówka.log")
from faker import Faker
fake = Faker()

if __name__ == "__main__":
#_____________________________________BaseContact Class_Begin_Here__________________________________________<<<<<<<<<<<<<<<
    class BaseContact :                                                 
        def __init__(self,name, phon):                                 #<---------------------------------------Konstruktor 
            self.name=name
            self.phon=phon
            self.len_name = name                      

        def __str__(self):
            return (f'(BuisnesCard of {self.name},phon number:{self.phon})') #____, type_of_bussines {self.type_of_bussines}
        def contact(self):                                               #<-------Zad_1_Mod_7_contact()---wywołanie linia 59
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
        def contact(self):                                        #<-------Zad_1_Mod_7_contact()---wywołanie linia 60
                return print (f"Kontaktuj się z {self.name} pod numerem SŁUŻBOWYM : {self.business_phon}")


    #____________________________________Child_Class_End____________________________________________________

    logging.info(f"otworzono program")

#_______________________________________ZADANIE_1_MODUŁ 7________________________________________________________
Base_card= BaseContact(fake.name(),'111 111 111')
Biznes_card=BussnesCard('Kasjer','123 456 789','kiosk',fake.name(),'222 222 222')
#print(f' type_of_biznes obiektu BiznesCard to:{Biznes_card._type_of_business}, imie, nazwisko to:{Biznes_card.name}, telefon:{Biznes_card.phon}') #__sprawdzam poprawność wpisania zmiennych
print(Base_card)
print(Biznes_card)
Base_card.contact()                                                               #___funkcja contact() clasy bazowej.
Biznes_card.contact()                                                             #___funkcja contact() clasy potomnej.
print(f' zmienna dynamiczna clasy potomnej:{Base_card.len_name}, {Base_card.name}')
print(f' zmienna dynamiczna clasy potomnej:{Biznes_card.len_name}, {Biznes_card.name}')
#_________________________________________Generator_Wizytówek_________________________________________________
type=input('Dla Base wybierz: 0 dla Biznes wybierz: 1\n')
quantity=input('wpisz liczbę wizytówek do stworzenia\n')
card_list=[]
print(type,quantity)
i=0
def fcreate_contacts(_quantity,_type): 
    print("wszedłem do funkcji")   
    for i in range(int(_quantity)):
        if int(_type) == 0:
            x=BaseContact(fake.name(),fake.phone_number())
            card_list.append(x)
            print(card_list[i])
            
        if int(_type) == 1:
            card_list.append(i)
            card_list[i]=BussnesCard(fake.job(),fake.phone_number(),fake.bs(),fake.name(),fake.phone_number())
            print(card_list[i])
        i+=1
fcreate_contacts(quantity,type)    
for i in range (len(card_list)):
    print(f"koncowe wyswietlenie rezultatu zapisu do listy nr karty {i} w liście to : {card_list[i]}")      

#_________________________________________T__H__E__--__E__N__D__________________________________________          