class ContactManager:

    def __init__(self, contacts: dict[str, list[str]] = {}):
        
        self.contacts = contacts

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:

        """
        Questa funzione crea un contatto...
        """

        if name not in self.contacts:
            self.contacts[name] = phone_numbers

        else: 
            raise ValueError("Errore: Questo contatto è già esistente.")
        
        return {name: phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
            
            if phone_number in self.contacts[contact_name]:
                raise ValueError("Errore, il numero di telefono esiste già.")
                
            if contact_name not in self.contacts:
                raise ValueError("Errore, il contatto non esiste.")

            self.contacts[contact_name].append(phone_number)

            return {contact_name: self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

            if phone_number not in self.contacts[contact_name]:
                raise ValueError("Errore, il numero non è presente.")

            elif contact_name not in self.contacts:
                raise ValueError("Errore, il contatto non è presente.")

            self.contacts[contact_name].remove(phone_number)

            return {contact_name: self.contacts[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:
         
        if contact_name not in self.contacts:
             raise ValueError("Errore, il contatto non esiste.")
        
        if old_phone_number not in self.contacts[contact_name]:
             raise ValueError("Errore, il numero non è presente")
        
        index = self.contacts[contact_name].index(new_phone_number)

        self.contacts[contact_name][index] = new_phone_number

        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self) -> list[str]:
         
         return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str) -> list[str]:
         
         if contact_name not in self.contacts:
              raise ValueError("Errore, il contatto non esiste.")
         
         return self.contacts[contact_name]
    
    def search_contact_by_phone_numbers(self, phone_number: str) -> list[str]:
         
         contact_list: list[str] = []

         for contacts, list_contacts in self.contacts.items():
              
              if phone_number in list_contacts:
                   
                   contact_list.append(contacts)


              if contact_list == []:
                   
                   raise Exception("Nessun contatto trovato con questo numero di telefono!")
              
              
              return contact_list