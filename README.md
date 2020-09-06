# Análise Léxica (Trabalho - 1ª parte)

## Linguagem de programação T++

 ### BNF Comentada

|||
|-:|-|
|programa ::=|lista_declaracoes|
|lista_declaracoes ::= |lista_declaracoes declaracao \| declaracao
|declaracao ::= |declaracao_variaveis \| inicializacao_variaveis \| declaracao_funcao|
|declaracao_variaveis ::= |tipo DOIS_PONTOS lista_variaveis|
|inicializacao_variaveis ::= |atribuicao|
|lista_variaveis ::= |lista_variaveis VIRGULA var \| var|
|var ::= |ID \| ID indice|
|indice ::=| indice ABRE_COLCHETE expressao FECHA_COLCHETE \| ABRE_COLCHETE expressao FECHA_COLCHETE|
|tipo ::= |INTEIRO \| FLUTUANTE|
|declaracao_funcao ::= |tipo cabecalho \| cabecalho|
|cabecalho ::= |ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM|
|lista_parametros ::= |lista_parametros VIRGULA parametro \| parametro \| vazio|
|parametro ::= |tipo DOIS_PONTOS ID \| parametro ABRE_COLCHETE FECHA_COLCHETE|
|corpo ::= |corpo acao \| vazio|
|acao ::= |expressao \| declaracao_variaveis \| se \| repita \| leia \| escreva \| retorna \| erro|
|se ::= |SE \| expressao ENTAO corpo FIM \| SE expressao ENTAO corpo SENAO corpo FIM|
|repita ::= |REPITA corpo ATE expressao|
|atribuicao ::= |var ATRIBUICAO expressao|
|leia ::= |LEIA ABRE_PARENTESE var FECHA_PARENTESE|
|escreva ::= |ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE|
|retorna ::= |RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE|
|expressao ::= |expressao_logica \| atribuicao|
|expressao_logica ::= |expressao_simples \| expressao_logica operador_logico expressao_simples|
|expressao_simples ::= |expressao_aditiva \| expressao_simples operador_relacional expressao_aditiva|
|expressao_aditiva ::= |expressao_multiplicativa \| expressao_aditiva operador_soma expressao_multiplicativa|
|expressao_multiplicativa ::= |expressao_unaria \| expressao_multiplicativa operador_multiplicacao expressao_unaria|
|expressao_unaria ::= |fator \| operador_soma fator \| operador_negacao fator|
|operador_relacional ::= |MENOR \| MAIOR \| IGUAL \| DIFERENTE \| MENORIGUAL \| MAIORIGUAL|
|operador_soma ::= |MAIS \| MENOS|
|operador_logico ::= |ELOGICO \| OULOGICO|
|operador_negacao ::= |NEGACAO|
|operador_multiplicacao ::= |MULTIPLICACAO \| DIVISAO|
|fator ::= |ABRE_PARENTESE expressao FECHA_PARENTESE \| var \| chamada_funcao \| numero|
|numero ::= |NUM_INTEIRO \| NUM_PONTO_FLUTUANTE \| NUM_NOTACAO_CIENTIFICA|
|chamada_funcao ::= |ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE|
|lista_argumentos ::= |lista_argumentos VIRGULA expressao \| expressao \| vazio|

## Especificação formal dos autômatos para a formação de cada classe de token da linguagem
Explicar cada expressão regular, lista de palavras reservadas e lista de tokens

## Detalhes da implementação da varredura na LP e ferramenta (e/ou bibliotecas) escolhidas
Explicar como foi usada a biblioteca lex, e seu funcionamento

## Exemplos de saída do sistema de varredura (lista de tokens) para exemplos de entrada (código fonte)
Explicar como se executa o programa e dar um exemplo de uso, colocando um print da entrada e saída