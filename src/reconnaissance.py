from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    liste_modele = ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    resultat = []
    for k in range (len(liste_modele)):
        image.binarisation(image,S)
        image.localisation(image)
        image.resize(image, image.H, image.W)
        image.similitude(image, liste_modele[k])
        resultat.append(image.similitude(image, liste_modele[k]))
    result = 0
    for i in range (len(resultat)):
        if resultat[i] > resultat[0]:
            result = i
    return result
            
    
        

