# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

#print('1' + 1) # O python não consegue somar uma string com um inteiro.
print(int('1') + 1) # é necessário converter a string em inteiro.
print(type(float('1') + 1))
print(bool(' ')) # converte em boolean. 
print(str(11) + 'b') # converte o numero 11 em string e concatena com a string 'b'.

