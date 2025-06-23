📦 Processador de Dados de Códigos de Barras
Este projeto é um aplicativo web simples construído com Streamlit que permite processar arquivos de texto contendo códigos de barras e suas respectivas quantidades. Ele adiciona a data e hora do processamento a cada registro e organiza os dados resultantes por quantidade, facilitando a análise e o gerenciamento de inventário ou contagens.

✨ Funcionalidades
Upload de Arquivo TXT: Permite o envio de arquivos de texto (.txt) contendo dados de códigos de barras.
Processamento de Dados: Lê cada linha do arquivo no formato CÓDIGO,QUANTIDADE.
Inclusão de Data e Hora: Adiciona a data e hora do processamento a cada registro.
Organização por Quantidade: Ordena os resultados finais com base na quantidade do item (do menor para o maior).
Tratamento de Erros: Identifica e reporta linhas com formato inválido ou quantidades não numéricas no arquivo de entrada.
Visualização e Download: Exibe os dados processados em uma área de texto e permite o download do resultado formatado em um novo arquivo .txt.
🚀 Como Usar
1. Preparar o Arquivo de Entrada
Seu arquivo de texto (.txt) deve ter o seguinte formato, com um código e sua quantidade separados por uma vírgula em cada linha:

CODIGO_EXEMPLO1,10
OUTRO_CODIGO,5
CODIGO_ALEATORIO,25
Exemplo de meus_dados.txt:

EAN1234567890123,50
EAN9876543210987,10
EAN1122334455667,25
CODIGO001,5
CODIGOXYZ,100
2. Rodar o Aplicativo Localmente
Clone este repositório (ou salve o código):
Se você salvou o código em um arquivo local, pule para o próximo passo. Caso contrário, se for um repositório Git:

Bash

git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_SEU_DIRETORIO>
Instale o Streamlit:
Se você ainda não tem o Streamlit instalado, execute:

Bash

pip install streamlit
Execute o aplicativo:
Navegue até o diretório onde o arquivo app.py (ou como você o nomeou) está salvo e execute o comando:

Bash

streamlit run app.py
(Substitua app.py pelo nome do seu arquivo Python, se for diferente).

Acesse o Aplicativo:
Seu navegador web abrirá automaticamente uma nova aba com o aplicativo em execução. Se não abrir, verifique o terminal para o endereço local (geralmente http://localhost:8501).

3. Utilizar a Interface
No aplicativo, clique em "Envie um arquivo .txt (formato: CODIGO,QUANTIDADE por linha)".
Selecione seu arquivo .txt preparado.
O aplicativo processará os dados e exibirá o "Resultado formatado" em uma caixa de texto.
Você pode inspecionar os dados ou clicar no botão "Baixar resultado formatado" para salvar o arquivo processado.
🛠️ Tecnologias Utilizadas
Python
Streamlit (para a interface web)
👨‍💻 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests se tiver sugestões de melhoria ou encontrar algum bug.
