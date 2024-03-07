compras = []
resp = "s"
while resp !="n":
    compras.append(input("digite o item da lista:") )
    resp = input("Deseja continuar? - s para Sim ou n para Não:")
for x in compras:
    if x == "banana":
        print("Encontrei a banana!")
    else:
        print("não encontrei a banana :( ")