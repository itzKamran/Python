#Contact Management system

contacts = {}

def add_contact():
    name = input("Enter Your Name :")
    try:
        phone_no = int(input("Enter a phone number :"))
        contacts[name] = phone_no
        print(f"Customer Added Successfully")
    except ValueError:
        print("Add phone number in digits(0-9)")
def search_contact():
    name = input("Search Name :")
    if name in contacts:
      phone = contacts[name]
      print("\n---Search Name Contacts---")
      print(f"Name : {name} : Contacts Number : {phone}")
    else:
      print(f"\n Erro {name} Name Not Found !")

def view_contact():
    if not contacts:
      print("\n No Contacts Found !")
      return
    print("\n--------All Customer Data -----")
    for name , phone in contacts.items():
       print(f"Name : {name} :Phone Number: {phone}")

def delete_contact():
   name = input("Delete Contact")

   if name in contacts:
      delete_phone = contacts.pop(name , "Name Not Found !")

      print(f"{name} Name has Deleted In Contacts !")

while True:
   print("\n1.Add Contacts")
   print("2.Search Contacts")
   print("3.View Contacts")
   print("4.Deleted Contacts")
   print("5.Exists")
   try:
      choices = int(input("Enter A Choice (1-5) :"))
   except ValueError:
       print("Enter a Valid Number Between (1-5)  ")
   if choices == 1:
       add_contact()
   elif choices == 2:
        search_contact()
   elif choices == 3:
        view_contact()
   elif choices == 4:
        delete_contact()
   elif choices == 5:
       print("Thank You For Using Application")
       break
   else :
       print("invlid choices")
   
   





                
      


