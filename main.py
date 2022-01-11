import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7b1e81193a3226766a75faa8329d2e8e"
# Your Auth Token from twilio.com/console
auth_token = "1b318eb2820cc05a8cef414db819c9b9"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Exel
lista_meses = ['janeiro','fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

# Em cada arquivo: Verificar se algum valor da coluna vendas do arquivo x é maior que 55.000
# Caso seja maior -> enviar sms com nome, mês, quantidade de vendas e o nome do vendedor
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        # vendas, vendedor = tabel_vendas.loc[linha, coluna]
        print(f'No mês {mes}  alguem a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511963740364",
            from_="+19285507913",
            body=f'No mês {mes}  alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
# Caso não seja: Nada