import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "ACcfc00505b8b1dbd6bd42d4c20fb362e1"
# Your Auth Token from twilio.com/console
auth_token = "7e8c193e192c634c2e781a62bca52918"
client = Client(account_sid, auth_token)

# Passo a passo de s olução

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # clsprint(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No mês {mes} alguém bateu a meta, vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5586994323050",
            from_="+19036664516",
            body=f'No mês {mes} alguém bateu a meta, vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


# print(tabela_vendas)
# Verificar se algum valor na coluna vendas é maior que 55.000

# Se for maior do que 55.000 -> Envia SMS com o Nome, o mês e as vendas dele

# Caso não seja maior que 55.000 não fazer nada
