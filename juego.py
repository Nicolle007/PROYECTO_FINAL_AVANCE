import random
class mesa:
    def __init__(self,Usuario,rondas,cartas,apuesta,marcador,saldo):
        self.usuario=Usuario
        self.rondas=rondas
        self.cartas=cartas
        self.apuesta=int(apuesta)
        self.marcador=marcador
        self.saldo=int(saldo)
        
    def generar_cartas(self):
        c=0
        self.saldo=self.saldo-self.apuesta
        while c!=3:
            carta_creada=random.randint(1,13)
            carta=Carta(carta_creada)
            self.cartas.append(carta)
            c=c+1
            
    def comparar_valores_c1(self,valor_boton):
        carta=self.cartas[0]    
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+2
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13:
            if valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1:
            if valor_boton ==13:
                self.marcador = self.marcador+1
                
            
    def comparar_valores_c2(self,valor_boton):
        carta=self.cartas[1]
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+2
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13:
            if valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1:
            if valor_boton ==13:
                self.marcador = self.marcador+1
                
            
    def comparar_valores_c3(self,valor_boton):
        carta=self.cartas[2]
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+2
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13:
            if valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1:
            if valor_boton ==13:
                self.marcador = self.marcador+1
                
            
    def pagar(self):
        if self.marcador>=3:
            self.saldo=self.saldo+(self.apuesta*2)+self.apuesta
            return True
        elif self.marcador==2:
            self.saldo=self.saldo+(self.apuesta*0.5)+self.apuesta
        elif self.marcador==1:
            self.saldo=self.saldo
        else:
            self.saldo=self.saldo-self.apuesta+self.apuesta
            return False
            
    def revelar_cartas(self):
        valores_cartas=[]
        for i in self.cartas:
            valores_cartas.append(i.valor)
        print("Los valores de las cartas eran:")
        print(f"Carta 1: {valores_cartas[0]}")
        print(f"Carta 2: {valores_cartas[1]}")
        print(f"Carta 3: {valores_cartas[2]}")
            
          
class Carta:
    def __init__(self,valor):
        self.valor=int(valor)
    
    
class Usuario:
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.saldo=saldo
        
class Saldo:
    def __init__(self,valor):
        self.valor=int(valor)
        
        
class Rondas:
    def __init__(self,cantidad, orden):
        self.cantidad=cantidad
        self.orden=orden
        
class Apuesta:
    def __init__(self,valor):
        self.valor=int(valor)
    
class Marcador:
    def __init__(self,valor):
        self.valor=int(valor)
            

print("Bienvenido")
Usuario1=Usuario(input("Escribe tu nombre: "),2000)
print(f"{Usuario1.nombre} recuerda que tu saldo inicial es de 2000")
print("Se generaran 3 cartas aleatorias debes adivinar sus valores")
print("Si adivinas el numero exacto se te suman 2 puntos")
print("Si adivinas un numero 1 unidad cerca, Ej: el valor de la carta es 9 y tu respuesta es 8 o 10 se suma 1 punto")
print("Si logras hacer minimo 3 puntos se te pagara el doble de lo que apostaste")
print("Si logras hacer 2 puntos se te paga la mitad de lo que apostaste")
print("si logras hacer 1 punto se te devuelve el valor que apostaste")
apuesta1=Apuesta(input("Escribe el valor que deseas apostar "))
marcador1=Marcador(0)
saldo1=Saldo(2000)
mesa1=mesa(Usuario1.nombre,1,[],apuesta1.valor,marcador1.valor,saldo1.valor)
if mesa1.apuesta>mesa1.saldo:
    print("No puedes apostar mas de lo que tienes")
    print("TRAMPA")
else:
    print(" Se ha iniciado la mesa")
    print(f" El marcador está en {mesa1.marcador}")
    mesa1.generar_cartas()
    print(f"el saldo es de {mesa1.saldo}")
    for i in mesa1.cartas:print(i.valor)
    print("Se han genarado las cartas")
    carta1=(int(input("Ingresa el valor de la primera carta")))
    mesa1.comparar_valores_c1(carta1)
    print(f" El marcador está en {mesa1.marcador}")
    carta2=(int(input("Ingresa el valor de la segunda carta")))
    mesa1.comparar_valores_c2(carta2)
    print(f" El marcador está en {mesa1.marcador}")
    carta3=(int(input("Ingresa el valor de la tercera carta")))
    mesa1.comparar_valores_c3(carta3)
    print(f" El marcador final es: {mesa1.marcador}")
    print("Es hora de revelar el valor de las cartas ")
    mesa1.revelar_cartas()
    paga=mesa1.pagar()
    if paga ==True:
        print(f"Felicidades, ahora tu saldo es {mesa1.saldo} ")
    else:
        print(f"Mas suerte para la proxima! tu saldo es {mesa1.saldo}")
        
    while True:
        seguir=input("Desea seguir jugando?(s/n): ")
        if seguir== "s":
            if mesa1.saldo==0:
                print("Te quedaste sin dinero, no puedes apostar mas")
                break
            else:
                mesa1.marcador=0
                mesa1.cartas=[]
                print(f"{mesa1.usuario} tu saldo es de {mesa1.saldo}")
                apuesta1=Apuesta(input("Escribe el valor que deseas apostar "))
                if apuesta1.valor>mesa1.saldo:
                    print("No puedes apostar mas de lo que tienes")
                    print("TRAMPA")
                    break
                else: 
                    mesa1.apuesta=apuesta1.valor
                    print(" Se ha iniciado la mesa")
                    print(f" El marcador está en {mesa1.marcador}")
                    mesa1.generar_cartas()
                    print("Se han genarado las cartas")
                    carta1=(int(input("Ingresa el valor de la primera carta")))
                    mesa1.comparar_valores_c1(carta1)
                    print(f" El marcador está en {mesa1.marcador}")
                    carta2=(int(input("Ingresa el valor de la segunda carta")))
                    mesa1.comparar_valores_c2(carta2)
                    print(f" El marcador está en {mesa1.marcador}")
                    carta3=(int(input("Ingresa el valor de la tercera carta")))
                    mesa1.comparar_valores_c3(carta3)
                    print(f" El marcador final es: {mesa1.marcador}")
                    print("Es hora de revelar el valor de las cartas ")
                    mesa1.revelar_cartas()
                    paga=mesa1.pagar()
                    if paga ==True:
                        print(f"Felicidades, ahora tu saldo es {mesa1.saldo} ")
                    else:
                        print(f"Mas suerte para la proxima! tu saldo es {mesa1.saldo}")
        else:
            print("gracias por jugar ")
            break








        
    