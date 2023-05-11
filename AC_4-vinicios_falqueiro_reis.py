import numpy as np
import matplotlib.pyplot as plt
import statistics as sta
import locale

# Definir a localização (exemplo: formato monetário para o Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Formatando os valores em formato monetário
autopct_formatter = lambda x: locale.currency(x, grouping=True)


# 1) Os dados abaixo se referem ao número de livros comprados nos últimos anos pela biblioteca de uma
# cidade
# 2015 => 296 2016 => 422 2017 => 457 2018 => 718
# 2019 => 741 2020 => 810 2021 => 532 2022 => 681
# Construa um gráfico de barras com os dados acima com as seguintes características
# Título = compra de livros da biblioteca
# Cada barra deve ser de uma cor diferente
# Os valores devem ser centralizados em cada barra
# No eixo x deve ficar o ano e no eixo Y a quantidade de livros

def exercicio01():
    anos = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    numerodelivros = [296, 422, 457, 718, 741, 810, 532, 681]
    cores = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange']
    figura, ax = plt.subplots(figsize = (5,2))
    ax.set_title("Exercicio 1", fontsize = 15)
    ax.bar(anos, numerodelivros, color = cores)
    for idx, val in enumerate (numerodelivros):
        txt = f"{val} pts"
        y_coord = val - 1
        x_coord = idx - 0.3
        ax.text(x=x_coord, y=y_coord, s=txt, fontsize=8, color ="white")
    plt.show()

# exercicio01()

# 2) Vitor vai aproveitar as suas férias para viajar. A previsão de suas despesas ele registrou da seguinte
# forma:
# Diversão 1 R$ 1500,00
# Transporte R$ 2300,00
# Alimentação R$ 700,00
# Diversão 2 R$ 1000,00
# Hospedagem R$ 4500,00
# Construa um gráfico de setores com os dados acima

def exercicio02():
    segmento = ['Diversão 1', 'Transporte', 'Alimentação', 'Diversao 2', 'Hospedagem']
    valores = [1500.00, 2300.00, 700.00, 1000.00, 4500.00]
    cores = ['purple', 'yellow', 'teal', 'pink', 'gray']
    grafico = plt.subplot()
    grafico.pie(valores, labels=segmento, autopct=autopct_formatter, colors=cores)
    grafico.set_title('Exercicio 02', fontsize = 15)
    plt.show()

# exercicio02()



def exercicio03():
    anos = [2019, 2020, 2021, 2022, 2023]
    taxa_desemprego = [11.6, 11.0, 14.1, 11.6, 8.1]

    plt.plot(anos, taxa_desemprego, marker='o', linestyle='-', color='blue')

    # Adicionando a porcentagem da taxa de desemprego nos pontos com espaço maior
    for i in range(len(anos)):
        plt.text(anos[i], taxa_desemprego[i]+0.05, f"{taxa_desemprego[i]}%", ha='center', va='bottom')

    plt.title('Exercicio 03')
    plt.xlabel('Ano')
    plt.ylabel('Taxa de Desemprego')
    plt.xticks(anos)  # Define os valores do eixo x como os anos
    plt.show()
# exercicio03()

def exercicio04():
    regioes = ['Sudeste', 'Nordeste', 'Sul', 'Norte', 'Centro-Oeste']
    casos_acumulados = [14906780, 7353017, 7970469, 2898908, 4320244]
    cores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    plt.pie(casos_acumulados, labels=regioes, autopct='%1.1f%%', colors=cores)
    plt.title('Exercicio 04')
    plt.axis('equal')
    plt.show()

# exercicio04()

def exibir_menu():
    print("Menu:")
    print("1. Exercício 01")
    print("2. Exercício 02")
    print("3. Exercício 03")
    print("4. Exercício 04")
    print("5. Sair")

# Loop principal do menu
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        exercicio01()
    elif opcao == '2':
        exercicio02()
    elif opcao == '3':
        exercicio03()
    elif opcao == '4':
        exercicio04()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    


exibir_menu()
