import tkinter as tk
import random as rd
from tkinter.constants import BOTTOM, CENTER, FLAT, NW

def generate():
    string = '';
    for i in range(4):
        string += selectchar(i);
    for i in range(12):
        string += selectchar(rd.randint(0,3));
    mdp.set(string);

#Création de la fenêtre root
r = tk.Tk();

#Les variables principales
mainbgcolor = '#25455f';
mainfgcolor = 'white';
mdp = tk.StringVar();
mdp.set('Your Password');

#Entry qui sert d'affichage pour le mdp
showmdp = tk.Entry(r,
                   textvariable = mdp,
                   bg = mainbgcolor,
                   fg = mainfgcolor,
                   font = 'Roboto 20 bold',
                   highlightthickness = 0,
                   justify = CENTER,
                   bd = 0
                   );
showmdp.pack(pady = 100, side = BOTTOM);

#Fonction qui choisit un caractère aléatoire 
def selectchar(num):
    # 0 -> lettres minuscules
    # 1 -> lettres majuscules
    # 2 -> nombres
    # 3 caractères spéciaux
    if(num == 0):
        return chr(rd.randint(97,122));
    elif(num == 1):
        return chr(rd.randint(65,90));
    elif(num == 2):
        return ascii(rd.randint(0,9));
    else:
        return chr(rd.randint(33,47));


# Parametrage de la fenêtre root
r.title('Password Generator');
r.iconbitmap('assets/icon.ico');
r.geometry('500x800');
r.resizable(False,False);
r.config(bg= mainbgcolor);

#logo
canvas = tk.Canvas(r,
                   bg = mainbgcolor,
                   bd = 0,
                   highlightthickness = 0,
                   width = 500,
                   height = 500);
canvas.pack();
#on assigne au canvas le logo
logo = tk.PhotoImage(file ='assets/mainlogo.png');
canvas.create_image(0,
                    0,
                    image = logo,
                    anchor = NW);

#Boutton qui appelle la fonction generate
btngenerate = tk.Button(r,
                        text = 'Generate',
                        width = 40,
                        height = 3,
                        bg = '#8f4ecf',
                        activebackground = '#541682',
                        activeforeground = '#5a585c',
                        fg = 'white',
                        bd = 0,
                        highlightthickness = 0,
                        relief = FLAT,
                        font = 'Roboto 10 bold',
                        cursor = 'exchange',
                        command = generate);
btngenerate.pack();

#Lance l'application
r.mainloop();
