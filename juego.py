import random 

class Juego:
    
    def __init__(self):
        pass
    
    def think(self):
        self.num = random.randint(1,100)
        
    def guess(self):
        while True:
            try:
                n = int(input('Dime un número del 1 al 100: '))
                if isinstance(n, int) and n>0 and n<101:
                    break
            except:
                pass

        return n    
    
    def jugar(self):
    
        self.think()
        while True:
            n = self.guess()
            if self.num == n:
                print('Has acertado!')
                break
            elif self.num > n:
                print('Mi número es mayor')
            else:
                print('Mi número es menor')
                
                
def main():
    while True:
        partida = Juego()
        partida.jugar()
        
        seguir = input('Quieres seguir jugando S/N? ')
        if seguir != 'S':
            break
            
if __name__ == '__main__':
    main()
