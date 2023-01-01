from Ferme.classes import Ferme
animaux = Ferme.Ferme()
# get data from user and put it in dic         
def setData():
    nom = input("enter un nom: ")
    age = input("enter l age: ")
    return {"nom":nom,"age":age}
    
# add animal 
def ajouterAnimal():
    typeanimal = input("""
    selectionner le type d’animal a creer : 
    1.Chat
    2.Chien
    votre choix : """)
    if(typeanimal.isnumeric):
        if typeanimal == "1":
            data = setData()
            myanimal =Ferme.Chat(data["nom"],data["age"])
            animaux.ajouter_animal(myanimal)
            print ("le Chat",data["nom"],"est ne")
        elif typeanimal=="2":
            data = setData()
            myanimal = Ferme.Chien(data["nom"],data["age"])
            animaux.ajouter_animal(myanimal)
            print ("le chien",data["nom"],"est ne")
#check animal if exist in list 
def checkExistData(myData):
    if myData:    
        data = animaux
        for item in data.animaux:
            if item.nom == myData["nom"]:
                return {"exist":True,"data":item,"err":False}
        return {"exist":False,"data":"","err":False}
    return {"exist":False,"data":"","err":True}
# delete data from list
def deleteElement(myData):
    dataTest=animaux
    if dataTest:
        for i in dataTest.animaux:
            if i.nom == myData.nom:
                recovery= i
                dataTest.animaux.remove(i)
    return recovery  
#delete animal from list
def deleteData():
    nom = input("ecrire un nom : ")
    if nom.isalpha():
        result = checkExistData({'nom':nom})
        if(result["exist"]):
            res = deleteElement(result["data"])
            print ("le",res.__class__.__name__,res.nom,"est mort")
            showMenu()
        else :
            print(" animal not exist")
            showMenu()
    else:
        print ("error ")
        deleteData()
        
# get number of animal in the farm 
def lenAnimal(myData):
    if(myData):
        return print ("Ma ferme a",len(myData.animaux),"animaux")
    else: 
        return print("err in data")  
    
# show second menu   
def showMenu():
    x = input("back to menu Y/N : ")
    if(x.isalpha()):
        x = x.capitalize()
        if x=="Y":
           menu()
        elif x=="N":
            exit()
        else:
            showMenu()
    else:
        showMenu()
# show first menu          
def menu():
    print("""
      Bienvenu à la ferme
    1.Ajouter un animal
    2.Lancer le cri de tous les animaux de la ferme 
    3.Tuer un animal 
    4.Nombre d'animaux
    5.Exite
    """)
    choix = input("ecrire votre choix: ")
    if choix=="1":
        ajouterAnimal()
        showMenu()
    elif choix=="2":
        animaux.crier()
        showMenu()
    elif choix=="3":
         deleteData()
         showMenu()
    elif choix=="4":
        lenAnimal(animaux)
        showMenu()
    elif choix=="5":
        print("Goodbye") 
        exit()
    else:
        print("\n Not Valid Choice Try again")

