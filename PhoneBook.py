####################################################################################################################
###                                    Algorithms for Bioinformatics
###                                 ***  class Phone Book              ***    
###
### Test number: 4      Class Number: 3         Date:   17 to 21 February 2020
###
### Group
### Student: Nuno Guilherme Balatrejo Pereira Nunes     Number:201606441
### Student: Tiago da Silva Coelho                      Number:201604170
### Student: Vasco Fernando Coelho Soares               Number:201604364
### 
####################################################################################################################
### Complete the code below for the object PhoneBook
### In main give example on how to create, update, insert and use object PhoneBook
### Explain in comments how the data will be organized

class PhoneBook:
    ''' Implements a Phone Book '''
    
    def __init__(self):
        ''' initializes phone book with appropriate data structure '''
        # complete
        # ...
        contactos = {}


        
    def add_phone(self,name, number):
        # complete
        # ...
        contactos[name] = number

    # add the remaining methods here

    def search_name(self,name):
        return contactos[name]

    def search_phone(self,number):
        for key,value in contactos.items():
            if(value == number): return key

    def print_book(self):
        for key,value in contactos.items():
            print("Nome: " + key + "Numero: " + value)

    def tester(self):
        self.add_phone("Nuno Nunes",938155275)
        self.add_phone("Tiago Coelho",917773333)
        self.add_phone("Vasco Soares",938155285)
        print("Search Name: " + self.search_name("Nuno Nunes"))
        print("Search Phone: "+ self.search_phone(938155275))
        print("copy: " + self.copy())
        self.print_book()

    def copy(self):
        copy.copy(contactos)
        
    
if __name__ == "__main__":
    ''' test code here '''
    # complete
    # ...

    p1 = PhoneBook("John")

    print(PhoneBook.name)
    print(PhoneBook.self)



    ##criamos um dicionario chamado contactos onde ira ser adicionado por ordem de insercao cada um dos contactos