

def amplitude(lista):
  if not lista:
    print("A lista está vazia.")
    return

  maior = max(lista)
  menor = min(lista)
  resultado = maior - menor
  print(f"A amplitude é:{resultado}")

numeros = [4, 2 ,7, 23, 21, 68, 23, 1, 6]
amplitude(numeros)