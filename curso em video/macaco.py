class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    
tv = televisao()
tv_sala = televisao()

tv_sala.canal = 6

print(tv.ligada, tv.canal)
print(tv_sala.canal)