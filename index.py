import string
from collections import Counter

# Solicita o texto do usuário
texto = input("Digite um texto qualquer: ")

# Remove pontuação e converte para minúsculas
texto_limpo = texto.lower().translate(str.maketrans("", "", string.punctuation))

# Separa em palavras
palavras = texto_limpo.split()

# Conta e ordena
frequencias = Counter(palavras)
ordenado = sorted(frequencias.items(), key=lambda x: x[1], reverse=True)

# Exibe o resultado
print("\nFrequência das palavras:")
for palavra, quantidade in ordenado:
    print(f"{palavra}: {quantidade}")
