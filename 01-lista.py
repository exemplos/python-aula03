usuarios = ["Maria", "Jose", "Carlos"]

print(usuarios)

print(usuarios[2])
print(len(usuarios))

nome = input("Digite um novo usuario:")
usuarios.append(nome)

print(usuarios)
print(usuarios[2])
print(len(usuarios))

procurarPor = input("Procurar por:")
idx = usuarios.index(procurarPor)
print("A posicao de {} é {}".format(procurarPor, idx))

usuarios.sort()
print(usuarios)
usuarios.sort(reverse=True)
print(usuarios)