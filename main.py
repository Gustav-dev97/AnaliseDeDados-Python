#pip install pandas
#pip install numpy
#pip install openpyxl
#pip install plotly

import pandas as pd

#Graficos
import plotly.express as px


#Passo 1: Importar a Base de Dados
tabela = pd.read_csv("telecom_users.csv")

#Passo 2: visualizar a Base de Dados
#Entender as informacoes que voce tem disponivel
#Para voce corrigir as redundâncias do banco de dados (em analise de dados informacao o que nao te ajuda te atrapalha)

#Nao afeta o arquivo original
#axis = 0 -> Linha, axis = 1 ->coluna
#tabela = tabela.drop (nome,eixo)
#tabela = tabela.drop (["Unnamed: 0", "IDCliente", "Genero"], axis=1)
#print(tabela)
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)

#Passo 3: Tratamento de Dados
#ver/ajustar qualquer valor que tá sendo reconhecido de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#valores vazios
#axis = 0 -> linhas, axis = 1 -> colunas

#colunas vazias -> excluir
#tabela = tabela.dropna (how=,axis=)
tabela = tabela.dropna(how="all", axis=1)

#linhas com algum valor vazio -> excluir
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

#Passo 4: Análise Simples -> entender como estão acontecendo os cancelamentos
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#passo 5: Análise mais completa -> entender a causa dos cancelamentos/possiveis solucoes

#Cria o Gráfico
#Para cada coluna da nossa base de dados, criar 1 gráfico

for coluna in tabela.columns:
    print(coluna)

    # x = coluna da base de dados , Churn = Sim ou não (cancelou ou não)
    #grafico = px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequence=["green", "red"])
    grafico = px.histogram(tabela, x=coluna, color="Churn")


    #Exibe o gráfico
    grafico.show()

#Conclusoes:

# Familias maiores potendem a cancelar menos
    # - Podemos oferecer um 2º numero de graça, ou um plano família

# Quanto maior tempo como cliente, menor a chance de cancelar
    # - Ação de bonificar o cliente nos primeiros 12 meses
    # - Nos primeiros meses os clientes estão cancelando muito
        # - Podemos estar com um problema no inicio do periodo do cliente
        # - Podemos estar fazzendo alguma ação de marketing muito ruim

# -Temos algum problema na fibra, os clientes estão cancelando MUITO
    # - Olhar mais a fundo a causa do cancelamento das fibras

# -Quantos menos serviços a pessoa tem, maior a chance dele cancelar
    # - Podemos oferecer um serviço extra e graça

# -Podemos incentivar pagamento no débito automático ou no cartão, taxas de cancelamento muito menores

# -Podemos oferecer incentivos para contrato anual
