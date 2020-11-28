import os
ListeSolution = []
os.chdir(r"C:\Users\Utilisateur\Desktop\Python Temp\NSI-TP\Exercice Parcours en Largeur")
root = os.getcwd()


def Parcours():
    f = os.listdir()
    while len(f)>0:
        print(len(f))
        s = f.pop(0)
        if "text.txt" in s:
            print("Trouvé text")
            with open(s,"r") as file:
                print("Text ouvert")
                data = file.read()
                ListeSolution.append(data)
        elif os.path.isdir(s):
            os.chdir(s)
            for i in os.listdir():
                if os.path.isdir(i): # n'ajoute à la file que les dossiers. Ajouter un truc pour lire le texte (mais faire attentions à la profondeur de lecture.
                    os.chdir(i)
                    temp_path = os.getcwd()
                    f.append(temp_path)
                    os.chdir("..")
                else:
                    temp_path = os.path.join(os.getcwd(),i)
                    f.append(temp_path)
            os.chdir("..")
        else:
            print(s)

