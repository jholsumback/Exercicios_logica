nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2
print("Sua media é:", media)

if media >= 70:
    print("APROVADO")
elif media >= 50 and media <= 70:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
