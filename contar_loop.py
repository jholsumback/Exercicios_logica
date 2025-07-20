valor =  int(input("Quer contar ate quanto?"))
salto = int(input("Qual será o salto pra contar?"))

contador = 0

while contador <= valor:
    print(contador)
    contador += salto
    

print("Terminei de contar")