import csv 
import os
# header de fichier .csv
header = ['nom', 'prenom', 'age', 'ville']
#initialise le ficher avec header
def creatFille():
    with open(os.path.abspath(os.curdir)+"\myfiel.csv", 'w',newline='') as f:
        # create the csv writer
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        # write a row to the csv file
        #writer.writerow(header)
# add list of data to file  
def setListOfDataToFille(myData):
    with open(os.path.abspath(os.curdir)+"\myfiel.csv", 'w',newline='') as f:
        # create the csv writer
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        # write a row to the csv file
        for element in myData:
            writer.writerow(element)
# add one data to file
def setDataToFille(myData):
    with open(os.path.abspath(os.curdir)+"\myfiel.csv", 'a',newline='') as f:
        # create the csv writer
        writer = csv.DictWriter(f, fieldnames=header)
        # write a row to the csv file
        writer.writerow(myData)
# get data form file 
def getData():
    mydata=[]
    with open(os.path.abspath(os.curdir)+"\myfiel.csv", 'r') as f:
        reader = csv.DictReader(f,delimiter=',', quotechar='"')
        for d in reader:
            mydata.append(d)
    return mydata
# show list of data
def showList():
    mydata=getData()
    for i in mydata:
        print(i)
              
# check if string contains number  
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False
# check if data exist in file .csv
def checkExistData(myData):
    if myData:    
        data = getData()
        for i,item in enumerate(data):
            if item["nom"] == myData["nom"]:
                return {"exist":True,"data":item,"index":i,"err":False}
        return {"exist":False,"data":"","err":False}
    return {"exist":False,"data":"","err":True}
# delete element from list 
def deleteElement(myData):
    dataTest=getData()
    if dataTest:
       for i in dataTest:
        if i["nom"] == myData["nom"]:
            dataTest.remove(i)
    return dataTest  
# delete data form file
def deleteData():
    nom = input("ecrire un nom : ")
    if nom.isalpha():
        result = checkExistData({'nom':nom})
        if(result["exist"]):
            res = deleteElement(result["data"])
            setListOfDataToFille(res)
            print ("operation succed")
        else :
            print(" nom not exist")
            errMenu("delete")
    else:
        print ("error ")
        deleteData()
        
# update data in the file 
def updateData():
    data=[]
    nom = input("ecrire votre nom : ")
    element = checkExistData({'nom':nom})
    if nom and element["exist"] :
       print ("your data is exist")
       data = setData()  
       dataTest=getData()
       if element["exist"]:
          dataTest[element["index"]]=data
          setListOfDataToFille(dataTest)
    else:
        print ("your data doesn't exist")
# get data from user and add in dic       
def setData():
    myData=[]
    age=0
    nom = input("ecrire votre nom : ")
    prenom = input("ecrire votre prenom : ")
    ville = input("ecrire votre ville : ")
    try :
        age = int(input("ecrire votre age : "))
    except ValueError as e:
        print("errurs valeur not.")
    if age==0:
        return print("age not correct")
    if nom=="" or prenom=="" or ville=="" :
        return print("you can send data empty") 
    else:
        if containsNumber(nom) or containsNumber(prenom) or containsNumber(ville) :
            return print("you can'nt add digit in nom or prenom or ville")
        myData={'nom':nom,'prenom':prenom,'age':age,'ville':ville}
        return myData
      
# add data to file .csv
def addData():
    myData= setData()
    if checkExistData(myData)["exist"] : 
        print ("data exist")
    elif not checkExistData(myData)["err"] :
        setDataToFille(myData)
        print(" your saving data is succed")
    else:
        print ("err in input")
# show menu
def menu():
    print("""
        Bienvenu à dataBase TP
    1.Afficher la liste de toutes les personnes enregistrées
    2.Ajouter une nouvelle personne 
    3.Modifier les informations d'une personne 
    4.Supprimer une personne
    5.Exite
    """)
    choix = input("ecrire votre choix: ")
    if choix=="1":
      showList()
      showMenu()
    elif choix=="2":
      addData()
      showMenu()
    elif choix=="3":
      updateData()
      showMenu()
    elif choix=="4":
     deleteData()
     showMenu()
    elif choix=="5":
      print("Goodbye") 
      exit()
    else:
       print("\n Not Valid Choice Try again")
       menu()
 
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
    
 
# show err menu   
def errMenu(var):
    x = input("vous voulez recommencer Y/N: ")
    if(x.isalpha()):
        x = x.capitalize()
        if x=="Y":
            print("\n recommence")
            if var == "delete":
                deleteData()
        elif x=="N":
            menu()
        else:
            errMenu(var) 
    else:
        errMenu()
            
              
