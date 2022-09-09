import random
from tkinter import font
from sudokuGeneraattori import taytaSudoku
from tkinter import *

sudoku = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
] 


# Luodaan oikea vastausruudukko


# VÄRIT
otsikkotaustavari = "#613659" # 2. tummin
taustavari = "#D3B1C2" # vaalein
tekstivari = "#211522" # tummin
vari4 = "#C197D2"

# Valittu numero
numero = 0

root = Tk()

# Fontit
fontHeader = font.Font(family='Segoe Script', size=16, weight="bold")
fontNumbers = font.Font(family='Microsoft New Tai Lue', size=12, weight="bold")
fontText = font.Font(family='Helvetica', size=12, weight="bold")

# Täytetään ruudukko vaikeustason mukaisesti sovitulla määrällä numeroita
def taytaRuudukko(sudoku, frames, vaikeus, vastausFrame):
    global buttons
    buttons = []

    taytaSudoku(sudoku)

    luoVastausPainikkeet(vastausFrame)
    
    # Looppaa oikean vastausruudukon numerot ja lisää vastaavat napit pelilaudalle
    for i in range(9):
        for j in range(9):
            buttons.append(Button(frames[(i//3)*3+(j//3)], text=sudoku[i][j], width=3, height=2, borderwidth=1, relief="solid", background='black', foreground=tekstivari, font=fontNumbers, command=lambda i=((i*9)+j):buttonPress(i, buttons)))

    # Poistaa tietyn määrän nappeja näkyvistä vaikeustason mukaan
    vaikeustaso(buttons, vaikeus)

    # Näyttää napit ruudukolla
    for i in range(81):
        buttons[i].grid(row=i//9, column=i%9)

# Poistetaan ruudukosta vaikeustason mukaisesti numeroita
def vaikeustaso(numerot, vaikeus):
    for i in random.sample(range(81), k=(40+(vaikeus*8))):
        numerot[i]['text'] = ''
    for num in numerot:
        if num['text'] != '':
            num['state'] = 'disabled'
            

# Lisää alavalikosta valitun numeron pelilaudalta klikattuun paikkaan
def buttonPress(indeksi, buttons):
    if numero != 0:
        buttons[indeksi]['text'] = numero
        buttons[indeksi]['foreground'] = 'black'

    # Voittotesti - Lisää aina oikean numeron oikeaan kohtaan
    # buttons[indeksi]['text'] = sudoku[indeksi//9][indeksi%9]


# Aktivoi valitun numeron, jolloin sitä voidaan lisätä pelilaudalle
# Korostaa valitut numerot pelilaudalta
def activateNumber(num, numeronapit):
    global numero
    if numero != num:
        numero = num
        for nappi in numeronapit:
            nappi['background'] = taustavari
        numeronapit[num-1]['background'] = otsikkotaustavari
        for i in range(81):
            if buttons[i]['text'] == num:
                buttons[i]['background'] = otsikkotaustavari
            else:
                buttons[i]['background'] = taustavari
    else:
        numero = 0
        numeronapit[num-1]['background'] = taustavari
        for i in range(81):
            buttons[i]['background'] = taustavari
    

# Tarkistaa ovatko numerot oikeissa paikoissa ja ilmoittaa väärien vastausten määrän
def tarkistaVastaukset(frame):
    montaVaarin = 0
    voitto = True
    
    for i in range(81):
        if buttons[i]['text'] != sudoku[i//9][i%9] and buttons[i]['text'] != '':
            montaVaarin += 1
            buttons[i]['foreground'] = 'red'
        elif buttons[i]['text'] == '':
            voitto = False
    
    tarkistusTeksti = Label(frame, text=f"Sinulla on {montaVaarin} numeroa väärin.", background=vari4, foreground=tekstivari, font=fontText)
    tarkistusTeksti.grid(row=1, column=4, columnspan=5)

    if montaVaarin == 0 and voitto:
        voittoTeksti = Label(frame, text="Voitit pelin!", background=vari4, foreground=tekstivari, font=fontText)
        voittoTeksti.grid(row=2, column=2, columnspan=4)
        

# Luo 9 kehystä, joihin numerot laitetaan
def luoJaNaytaKehykset():
    frames = []

    for i in range(9):
        frames.append(Frame(root, height=130, width=130, borderwidth=3, relief='solid',background=taustavari))

    for i in range(9):
        frames[i].grid(row=(i//3)+1, column=(i%3)+1)

    return frames

# Luo numerot 1-9 alalaitaan, josta ne saa käyttöön painamalla
def luoVastausPainikkeet(frame):
    vastausButtons = []

    for i in range(9):
        vastausButtons.append(Button(frame, text=(i+1), height=1, width=2, borderwidth=1, relief="solid", background=taustavari, foreground=tekstivari, font=fontText, command= lambda i=i:activateNumber(i+1, vastausButtons)))

    for i in range(9):
        vastausButtons[i].grid(row=0, column=i, padx=2, pady=1)

def tyhjennaSudoku(sudoku):
    for rivi in sudoku:
        for i in range(9):
            rivi[i] = 0

def aloitaPeli(vaikeus):
    vastausFrame = Frame(root, height=150, width=300, background=taustavari)
    vastausFrame.grid(row=4, column=0, columnspan=4)
    
    tyhjennaSudoku(sudoku)

    taytaRuudukko(sudoku, luoJaNaytaKehykset(), vaikeus, vastausFrame)

    mainMenu = Button(vastausFrame, text="Päävalikko", background=taustavari, foreground=tekstivari, font=fontText, command=lambda: mainmenu(vastausFrame))
    mainMenu.grid(row=2, column=0, columnspan=3, sticky=W)
    

    tarkistusNappi = Button(vastausFrame, text="Tarkista vastaukset", background=taustavari, foreground=tekstivari, font=fontText, command=lambda: tarkistaVastaukset(vastausFrame))
    tarkistusNappi.grid(row=1, column=0, columnspan=4, sticky=W)

    
def mainmenu(vastausFrame):
    vastausFrame.grid_remove()

    frames = luoJaNaytaKehykset()
    
    vaikeus = Button(frames[1], text="Valitse \nvaikeustaso: ", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText)
    vaikeus.grid(row=0, column=0, rowspan=3, columnspan=2)

    helppo = Button(frames[3], text="Helppo", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText, command=lambda: aloitaPeli(0))
    helppo.grid(row=0, column=0, rowspan=3, columnspan=2)

    keskitaso = Button(frames[4], text="Keskitaso", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText, command=lambda: aloitaPeli(2))
    keskitaso.grid(row=0, column=0, rowspan=3, columnspan=2)

    vaikea = Button(frames[5], text="Vaikea", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText, command=lambda: aloitaPeli(3))
    vaikea.grid(row=0, column=0, rowspan=3, columnspan=2)
    

# Alkuruudun labelit sekä buttonit
otsikko = Label(root, text="SUDOKU", height=3, width=25, background=otsikkotaustavari, foreground=taustavari)
otsikko.configure(font=fontHeader)
otsikko.grid(row=0, column=0, columnspan=4)

frames = luoJaNaytaKehykset()

buttons = []
for i in range(9):
    for j in range(9):
        buttons.append(Button(frames[(i//3)*3+(j//3)], text='', width=3, height=2, borderwidth=1, relief="solid", background=taustavari, foreground=tekstivari, font=fontNumbers))
for i in range(81):
    buttons[i].grid(row=i//9, column=i%9)

frames = luoJaNaytaKehykset()
vaikeus = Button(frames[1], text="Valitse \nvaikeustaso: ", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText)
vaikeus.grid(row=0, column=0, rowspan=3, columnspan=2)

helppo = Button(frames[3], text="Helppo", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText, command=lambda: aloitaPeli(0))
helppo.grid(row=0, column=0, rowspan=3, columnspan=2)

keskitaso = Button(frames[4], text="Keskitaso", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText, command=lambda: aloitaPeli(2))
keskitaso.grid(row=0, column=0, rowspan=3, columnspan=2)

vaikea = Button(frames[5], text="Vaikea", height=6, width=12, background=taustavari, foreground=tekstivari, font=fontText, command=lambda: aloitaPeli(3))
vaikea.grid(row=0, column=0, rowspan=3, columnspan=2)

icon = PhotoImage(file="./sudoku/icon.png")
root.iconphoto(False, icon)
root.title("SUDOKU")

root.geometry("+600+200")
# MACOS
'''root.configure(background="white")'''
root.mainloop()