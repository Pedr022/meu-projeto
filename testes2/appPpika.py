import tkinter as tk

janela = tk.Tk()
janela.title('Gráficos 2D Nativos')

area_desenho = tk.Canvas(janela, width=400, height=550, bg='grey')
area_desenho.pack()

area_desenho.create_rectangle(180, 250, 260, 440, fill='brown')
area_desenho.create_oval(220, 400, 300, 480, fill='brown')
area_desenho.create_oval(140, 400, 220, 480, fill='brown')
area_desenho.create_oval(165, 180, 275, 270, fill='pink')
area_desenho.create_line(220, 200, 220, 180, fill='black', width='5')
area_desenho.create_line(220, 90, 220, 150, fill='white', width='10')
area_desenho.create_line(220, 50, 220, 75, fill='white', width='10')
area_desenho.create_line(265, 110, 235, 160, fill='white', width='10')
area_desenho.create_line(170, 110, 200, 160, fill='white', width='10')

janela.mainloop()