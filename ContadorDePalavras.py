def contar_palavras(texto):
    # Converter o texto para minúsculas
    texto = texto.lower()
    
    # Remover pontuação e números
    texto = ''.join(e for e in texto if e.isalnum() or e.isspace())
    
    # Dividir o texto em palavras
    palavras = texto.split()
    
    # Criar um dicionário para armazenar a contagem de palavras
    contagem = {}
    
    # Contar as palavras
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem

# Exemplo de uso
texto = "Este é um exemplo de texto para contar palavras."
contagem = contar_palavras(texto)

print("Contagem de palavras:")
for palavra, count in contagem.items():
    print(f"{palavra}: {count}")