import string

maiuscula = list(string.ascii_uppercase)
minuscula = list(string.ascii_lowercase)
digitos = list(string.digits)
criptografado = []


def cifraCesar(original, descriptografar=False, criptografado=None):
    if descriptografar == False:
        deslocamento = 3
    else: 
        deslocamento = -3

    if criptografado == None:
        criptografado = []

    # Caso Base
    if len(original) == 0:
        return ''.join(criptografado)
    
    # Para dígitos
    if original[0] in digitos:
        posicao = digitos.index(original[0])
        if (posicao + deslocamento) >= len(digitos):
            posicao = (posicao + deslocamento) - len(digitos)
            criptografado.append(digitos[posicao])
        else:
            criptografado.append(digitos[posicao + deslocamento])

    # Para letras maiúsculas
    elif original[0] in maiuscula:
        posicao = maiuscula.index(original[0])
        if (posicao + deslocamento) >= len(maiuscula):
            posicao = (posicao + 3) - len(maiuscula)
            criptografado.append(maiuscula[posicao])
        else:
            criptografado.append(maiuscula[posicao + deslocamento])

    # Para letras minúsculas
    elif original[0] in minuscula:
        posicao = minuscula.index(original[0])
        if (posicao + deslocamento) >= len(minuscula):
            posicao = (posicao + deslocamento) - len(minuscula)
            criptografado.append(minuscula[posicao])
        else:
            criptografado.append(minuscula[posicao + deslocamento])

    elif original[0] in (' ', '\n'):
        criptografado.append(original[0])
    
    else:
        criptografado.append(original[0])
    # Responsividade
    return cifraCesar(original[1:], descriptografar, criptografado)
    

def cripto_arquivo(original, descriptografar):
    with open(original, 'r', encoding='utf8') as arquivo:
        conteudo = arquivo.read()
        conteudo = cifraCesar(conteudo, descriptografar)
        with open('criptografado.txt', 'w') as arquivo:
            arquivo.writelines(conteudo)

def descriptografar_arquivo(criptografado):
    with open(criptografado, 'r') as arquivo:
        conteudo = arquivo.read()
        conteudo = cifraCesar(conteudo, True)
    return conteudo

# criptografar original
cripto_arquivo('secreto.txt', False)

# descriptografar criptografado
descriptografado = descriptografar_arquivo('criptografado.txt')
print(descriptografado)