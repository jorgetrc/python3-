"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na 
    palavra secreta; exiba a letra:
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = "python"
letras_acertadas = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apelas uma letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você ganhou!!! Parabéns')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas:', tentativas)
        letras_acertadas = ''
        tentativas = 0

