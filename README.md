# trab_della
Trabalho Autômatos
No âmbito deste projeto,foi desenvolvito um autômato AFNE-e   utilizando  a linguagem de programação  python  autômato   tem como expressão regular (a+b+c)*abc (a+b+c)*;

Em outras palavras, este autômato aceita qualquer palavra que tiver  a subpalavra abc no inicio ,meio ou final da sequência;

#Funcionamento do código

1-Inicialmente o main.py recebe o arquivo data.json contendo os estados, e as transições,estado inical e final;

2-Segundamente a acontece um  calculo de transições vazias que considera todas as  transições vazias  para determinar até onde estado consegue chegar através delas;

3- Depois a ferramenta lê cada linha do arquivo test_input.csv que contêm  as sequências e escreve no arquivo test_output.csv da seguinta forma a sequencia lida,se aceita ou e o tempo de execução em cada linha;

Obs:Lembre de utilizar o prombt de comando para funcionamento correto do programa;


#Exemplo de resultado 

arquivo test_input_csv

palavra de entrada;resultadoesperado

aacbb;1

ccaa;0

bca;0

acba;1

prombt de comando

python main.py data.json test_input.csv test_output.csv

arquivo test_output.csv

Palavra de Entrada;Resultado Esperado;Resultado Obtido;Tempo de Execução

aacbb;1;aceito;0.0

ccaa;0;nao_aceito;0.0

bca;0;nao_aceito;0.0

acba;1;aceito;0.0









