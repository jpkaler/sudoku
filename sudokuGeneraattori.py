# Sudoku Generaattori
# Luo valmiin sääntöjenmukaisen sudokun
import random
import time

# Luo gridi
nollasudoku = [
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

numberList = [1,2,3,4,5,6,7,8,9]

# Täytettävän position rivi, sarake sekä neliö listoina -> palauttaa bool sekä sarakkeessa ja neliössä jäljellä olevat numerot
def oikeaNumero(ypositio, xpositio, num, sudoku):
    rivi = sudoku[ypositio]
    sarake = [y[xpositio] for y in sudoku]
    nelio = []
    nelioxstart = xpositio // 3 * 3
    nelioystart = ypositio // 3 * 3

    for y in range((nelioystart), (nelioystart + 3)):
        nelio += sudoku[y][nelioxstart:(nelioxstart + 3)]

    sarakeJaljella = [x for x in numberList if x not in sarake]
    nelioJaljella = [x for x in numberList if x not in nelio]
    
    return (num not in rivi and num not in sarake and num not in nelio, sarakeJaljella, nelioJaljella)

# Täytä numeroita gridiin
def taytaSudoku(sudoku):
    random.shuffle(numberList)
    y = 0
    x = 0
    laskuri = 0
    laskuri2 = 0
    
    while y < 9:
        x = 0
        while x < 9:
            if not sudoku[y][x]:
                for num in numberList:
                    # Passaako numero kyseiseen kohtaan ruudukossa
                    if oikeaNumero(y,x,num, sudoku)[0]:
                        # Lisätään numero koordinaattien osoittamaan kohtaan
                        sudoku[y][x] = num
                        random.shuffle(numberList)
                        # Piirrä ruudukko
                        x += 1
                        """ for z in sudoku:
                            print(z)
                        time.sleep(0.5)
                        print() """
                        break

                    # Jos mikään numero ei passaa
                    elif numberList[8] == num:
                        # Jos ohjelma on jumittanut yli 20 kertaa samalla rivillä -> poistaa numerot samalta riviltä sekä edelliseltä riviltä
                        if laskuri2 > 20:
                            sudoku[y] = [0,0,0,0,0,0,0,0,0]
                            sudoku[(y - 1)] = [0,0,0,0,0,0,0,0,0]
                            y -= 1
                            laskuri2 = 0
                        # Jos ohjelma on jumittanut yli 10 kertaa samalla rivillä -> poistaa kaikki numerot samalta riviltä
                        elif laskuri > 10:
                            sudoku[y] = [0,0,0,0,0,0,0,0,0]
                            laskuri = 0
                        # Poistaa sarakkeeseen / neliöön passaavat numerot riviltä
                        else:
                            for xKoordinaatti in range(9):
                                if sudoku[y][xKoordinaatti] in oikeaNumero(y,x,num, sudoku)[(random.randint(1,2))]:
                                    sudoku[y][xKoordinaatti] = 0
                        laskuri += 1
                        laskuri2 += 1
                        x = 0
                        # Piirrä ruudukko
                        """ for z in sudoku:
                            print(z)
                        time.sleep(0.1)
                        print() """
            else:
                x += 1
        y += 1
        laskuri = 0
        laskuri2 = 0   
    return sudoku 

taytaSudoku(nollasudoku)

""" monta = 1000
before = time.time()
for i in range(monta):
    sudoku = [
    [0,0,0,0,0,0,0,0,0], # sudoku[0]
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]
    taytaSudoku(sudoku)

after = time.time()

print(f"{monta} sudokua luotiin ajassa: {after - before} sekuntia") """
