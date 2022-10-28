#The Python Game 


from tkinter import * 
import random 





#Primero declarar constantes

JUEGO_ANCHO = 800
JUEGO_LARGO = 800 
VELOCIDAD = 50
TAM_VEN = 60
TAMAÑO_SERPIENTE = 3 
COLOR_PYTHON = "BLUE"
COLOR_FONDO = "GREEN" 
COLOR_COMIDA = "RED" 

class Python:   #Se definen la primer clase 

    def __init__(self): 
        self.tamaño_serp = TAMAÑO_SERPIENTE 
        self.coordinates = [] 
        self.cuadrados = [] 

        for i in range(0, TAMAÑO_SERPIENTE) : 
            self.coordinates.append([0,0]) 
        
        for x, y in self.coordinates: 
            cuadrado = canvas.create_rectangle(x, y, x + TAM_VEN, y + TAM_VEN, fill= COLOR_PYTHON)  
            self.cuadrados.append(cuadrado)



 

class Comida: 

    def __init__(self) -> None:
        x = random.randint(0, (JUEGO_ANCHO / TAM_VEN)- 1) * TAM_VEN 
        y = random.randint(0, (JUEGO_LARGO / TAM_VEN)- 1) * TAM_VEN 
        self.coordinates = [x, y]   

        canvas.create_oval(x, y, x + TAM_VEN, y + TAM_VEN, fill=COLOR_COMIDA) 

        


def vuelta(serp, comida): 
    
    x, y = serp.coordinates[0]

    if mov == "up": 
        y -= TAM_VEN 
    elif mov == "down": 
        y += TAM_VEN 
    elif mov == "right": 
        x += TAM_VEN 
    elif mov == "left":  
        x -= TAM_VEN  

    serp.coordinates.insert(0, (x, y))  

    cuadrado = canvas.create_rectangle(x, y, x + TAM_VEN, y + TAM_VEN, fill= "YELLOW" ) 

    serp.cuadrados.insert(0, cuadrado)

    if x == comida.coordinates[0] and y == comida.coordinates[1]: 

        
        global puntaje 

        puntaje += 1 

        label.config(text= 'Puntaje: {}'. format(puntaje)) 

        canvas.delete('comida') 

        comida = Comida() 


    else: 
        del serp.coordinates[-1]
        canvas.delete(serp.cuadrados[-1])
        del serp.cuadrados[-1] 

    if choque(serp): 
        juego_terminado() 

    else: 
        window.after(VELOCIDAD, vuelta, serp, comida)




def mov_serp(new_mov):  

    global mov 


    if new_mov == 'left':
        if mov != 'right':
            mov = new_mov
    elif new_mov == 'right':
        if mov != 'left':
            mov = new_mov
    elif new_mov == 'up':
        if mov != 'down':
            mov = new_mov
    elif new_mov == 'down':
        if mov != 'up':
            mov = new_mov

        

def choque(serp): 
    x, y = serp.coordinates[0] 

    if x < 0 or x >= JUEGO_ANCHO: 
        return True 
    elif y < 0 or y  >= JUEGO_LARGO: 
        return True 

    for tam_serp in serp.coordinates[1:]: 
        if x == tam_serp[0] and y == tam_serp[1]: 
            return True
    
    return False

    

def juego_terminado():   
    canvas.delete(ALL) 
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('new york times', 60), text= 'Really? Is just a Snake game', fill='blue')

      


window = Tk()  
window.title('The Python Game')  
window.resizable(False, False)


window.bind('<Left>', lambda event: mov_serp('left'))

window.bind('<Right>', lambda event: mov_serp('right'))

window.bind('<Up>', lambda event: mov_serp('up'))

window.bind('<Down>', lambda event: mov_serp('down'))

puntaje = 0 
mov = 'down' 

label = Label(window, text = 'Puntaje:{}'.format(puntaje)) 
label.pack() 


canvas = Canvas(window, bg = COLOR_FONDO, height=JUEGO_LARGO, width=JUEGO_ANCHO ) 
canvas.pack() 

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")




serp = Python()   

comida = Comida()     

vuelta(serp, comida)

window.mainloop() 


