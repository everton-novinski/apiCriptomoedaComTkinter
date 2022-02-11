from turtle import color

import requests
import tkinter as tk
from tkinter import * 


menu = tk.Tk()
menu.title('CRIPTOMOEDAS')
menu.geometry('600x400')
menu.resizable(False, False)
menu.configure(background='#002080')
menu.iconbitmap('imagens/icon.ico')


moeda_var = tk.StringVar()

def cotacao():
    moeda = moeda_var.get().upper().strip()    

    if moeda == 'ADA' or moeda == 'CARDANO':
        req = requests.get(f'https://www.mercadobitcoin.net/api/ADA/ticker/')
        req_dic = req.json()
        
        cotaçao_ada = float(req_dic['ticker']['sell'])

        texto = f'Valor da Moeda Cardano é de R${cotaçao_ada:.2f} reais.'

        texto_cotacao['text'] = texto

        moeda_var.set('')

    elif moeda == 'BTC' or moeda == 'BITCOIN':
        req = requests.get(f'https://www.mercadobitcoin.net/api/BTC/ticker/')
        req_dic = req.json()
        
        cotaçao_btc = float(req_dic['ticker']['sell'])

        texto = f'Valor da Moeda Bitcoin é de R${cotaçao_btc:.2f} reais.'

        texto_cotacao['text'] = texto

        moeda_var.set('')

    elif moeda == 'ETH' or moeda == 'ETHEREUM':
        req = requests.get(f'https://www.mercadobitcoin.net/api/ETH/ticker/')
        req_dic = req.json()
        
        cotaçao_eth = float(req_dic['ticker']['sell'])

        texto = f'Valor da Moeda Ethereum é de R${cotaçao_eth:.2f} reais.'

        texto_cotacao['text'] = texto

        moeda_var.set('')

    elif moeda == 'SOL' or moeda == 'SOLANA':
        req = requests.get(f'https://www.mercadobitcoin.net/api/SOL/ticker/')
        req_dic = req.json()
        
        cotaçao_sol = float(req_dic['ticker']['sell'])

        texto = f'Valor da Moeda Solana é de R${cotaçao_sol:.2f} reais.'

        texto_cotacao['text'] = texto

        moeda_var.set('')

    elif moeda == 'AVAX' or moeda == 'AVALANCHE':
        req = requests.get(f'https://www.mercadobitcoin.net/api/AVAX/ticker/')
        req_dic = req.json()
        
        cotaçao_avax = float(req_dic['ticker']['sell'])

        texto = f'Valor da Moeda Avalanche é de R${cotaçao_avax:.2f} reais.'

        texto_cotacao['text'] = texto

        moeda_var.set('')

    elif moeda == 'LINK' or moeda == 'CHAINLINK':
        req = requests.get(f'https://www.mercadobitcoin.net/api/LINK/ticker/')
        req_dic = req.json()
        
        cotaçao_link = float(req_dic['ticker']['sell'])

        texto = f'Valor da Moeda Chainlink é de R${cotaçao_link:.2f} reais'

        texto_cotacao['text'] = texto

        moeda_var.set('')

    else:
        texto = 'Moeda invalida, somente moedas do menu.'
        texto_cotacao['text'] = texto

        moeda_var.set('')

          

moedas_label = tk.Label(menu,text='QUAL MOEDA VOCÊ DESEJA CONSULTAR?',bg='#002080',fg='#f2f2f2', font=('calibre',10,'normal'))
moedas_entry = tk.Entry(menu, textvariable= moeda_var, font=('calibre',10,'normal'))


botao = tk.Button(menu,text='Consultar',bg="black",fg="white", command=cotacao)


texto_cotacao = tk.Label(menu, text='',bg='#002080',fg='#f2f2f2', font=('calibre',15,'normal'))

menu_moedas = tk.Label(menu, text='CARDANO(ADA) \n'
    'BITCOIN(BTC)\n'
    'ETHEREUM(ETH)\n'
    'SOLANA(SOL)\n'
    'AVALANCHE(AVAX)\n'
    'CHAINLINK(LINK)',bg='#002080', fg='#ffd700',font=('calibre',12,'normal'))


menu_moedas.place(y=20,x=230)
moedas_label.place(y=160,x=180)
moedas_entry.place(y=200, x=240)

botao.place(y=240,x=280)
texto_cotacao.place(y=300,x=130)



menu.mainloop()