import sys
import ply.lex as lex

# Lista de palavras reservadas
reservadas = {
    'se'        : 'SE',
    'repita'    : 'REPITA',
    'fim'       : 'FIM',
    'leia'      : 'LEIA',
    'retorna'   : 'RETORNA',
    'escreva'   : 'ESCREVA',
    'inteiro'   : 'INTEIRO',
    'flutuante' : 'FLUTUANTE',
    'até'       : 'ATE',
    'senão'     : 'SENAO',
    'então'     : 'ENTAO'
}

# Lista de nomes de tokens com as palavras reservadas
tokens = ['MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVISAO', 'DOIS_PONTOS', 'VIRGULA', 'MENOR', 'MAIOR', 'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'E_LOGICO', 'OU_LOGICO', 'NEGACAO', 'ABRE_PARENTESE', 'FECHA_PARENTESE', 'ABRE_COLCHETE', 'FECHA_COLCHETE', 'ATRIBUICAO', 'NUM_INTEIRO', 'NUM_PONTO_FLUTUANTE', 'NUM_NOTACAO_CIENTIFICA', 'ID', 'COMENTARIO'] + list(reservadas.values())
 
# Expressões regulares para tokens simples
t_MAIS              = r'\+'
t_MENOS             = r'-'
t_MULTIPLICACAO     = r'\*'
t_DIVISAO           = r'/'
t_DOIS_PONTOS       = r':'
t_VIRGULA           = r','
t_MENOR             = r'<'
t_MAIOR             = r'>'
t_IGUAL             = r'=='
t_DIFERENTE         = r'!='
t_MENOR_IGUAL       = r'<='
t_MAIOR_IGUAL       = r'>='
t_E_LOGICO          = r'\&\&'
t_OU_LOGICO         = r'\|\|'
t_NEGACAO           = r'!'
t_ABRE_PARENTESE    = r'\('
t_FECHA_PARENTESE   = r'\)'
t_ABRE_COLCHETE     = r'\['
t_FECHA_COLCHETE    = r'\]'
t_ATRIBUICAO        = r'='
t_ignore            = ' \t'   # espacos e tabulacoes

# Expressão Regular para a palavra reservada 'senão'
def t_SENAO(t):
    r'senão'
    t.type = reservadas.get(t.value,'SENAO')
    return t

# Expressão Regular para a palavra reservada 'então'
def t_ENTAO(t):
    r'então'
    t.type = reservadas.get(t.value,'ENTAO')
    return t

# Expressão Regular para a palavra reservada 'até'
def t_ATE(t):
    r'até'
    t.type = reservadas.get(t.value,'ATE')
    return t

# Expressão regular para comentarios
def t_COMENTARIO(t):
    r'\{([\w\s]*)\}'
    t.type = reservadas.get(t.value,'COMENTARIO')
    return t
    
# Expressão regular para IDs
def t_ID(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'ID')
    return t

# Expressão regular para notacao cientifica
def t_NUM_NOTACAO_CIENTIFICA(t):
    r'([+-]?([0-9]+[.]([0-9]*)?|[.][0-9]+)|([0-9]+))([eE][-+]?\d+)'
    # t.value = float(t.value)    
    return t

# Expressão regular para numeros de ponto flutuante
def t_NUM_PONTO_FLUTUANTE(t):
    r'[+-]?([0-9]+[.]([0-9]*)?|[.][0-9]+)'
    # t.value = float(t.value)    
    return t
    
# Expressão regular para numero inteiro
def t_NUM_INTEIRO(t):
    r'[-\+]?[0-9]+'
    # t.value = int(t.value)    
    return t

# Expressão regular para quebra de linha
def t_NOVA_LINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# Erro
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 

def imprimeTokens(dados):
    # Construindo o lexer
    lexer = lex.lex()

    # Atribuindo os dados ao lexer
    lexer.input(dados)
    
    # Gerando tokens
    while True:
        tok = lexer.token()
        if not tok: 
            break
        print(tok.value, ":", tok.type)

def main():
    nome_arquivo = sys.argv[1]
    arquivo = open(nome_arquivo, "r")
    string_arquivo = arquivo.read()
    imprimeTokens(string_arquivo)

main()