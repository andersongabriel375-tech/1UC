nome = input("Nome: ")
idade = int(input("Idade: "))
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2) / 2

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "reprovado"
print("|||||||SITUAÇÃO NOTA||||||")
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"Média: {media}")
print(f"Situação: {situacao}")