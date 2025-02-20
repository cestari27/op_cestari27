
import requests
import json

# esse link pode mudar se os donos da API mudarem
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
cotacoes_dic = cotacoes.json()

cotacao_dolar = cotacoes_dic['ETHBRL']['bid']
print('A cotação do etherium é: R$', cotacao_dolar)
