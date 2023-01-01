import Ferme.utile as tp2
import TP1.tp1 as tp1
def welcom():
    choiseTp = input("""
    Bonjour ce tp a ete realiser par Mouad Boussaid et Baba Nabe et Mohamed Omrane
    selectionner le tp : 
    1.TP1
    2.La Ferme
    votre choix : """)
    if(choiseTp.isdecimal()):
        if choiseTp=="1":
           tp1.creatFille()
           tp1.menu()
        elif choiseTp=="2":
            tp2.menu()
        else:
            welcom()
    else:
        welcom()    
        
welcom()