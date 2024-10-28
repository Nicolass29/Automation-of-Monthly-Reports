import numpy as np
import matplotlib.pyplot as plt


def gerar_grafico(df, caminho_imagem):
    # Converter o valor recebido para float se necessário
    df['Valor recebido'] = df['Valor recebido'].replace(
        {r'R\$': '', r'\.': '', ',': '.'}, regex=True).astype(float)

    # Criando uma figura
    fig, ax = plt.subplots(figsize=(10, 6))

    # Definindo a largura das barras
    bar_width = 0.2

    # Posições das barras no eixo X
    clientes = np.arange(len(df['Clientes']))

    # Gráfico de Horas Gastas
    ax.bar(clientes, df['Horas gastas'] / 10000, width=bar_width,
           color='b', alpha=0.6, label='Horas')

    # Gráfico de Valor Recebido (deslocado para a direita)
    ax.bar(clientes + bar_width, df['Valor recebido'] / 1000000, width=bar_width,
           color='g', alpha=0.6, label='R$')

    # Configurando os rótulos do eixo X com os nomes dos clientes
    # Posiciona os rótulos dos clientes no centro das barras
    ax.set_xticks(clientes + bar_width / 2)
    # Substitui os valores numéricos pelos nomes dos clientes
    ax.set_xticklabels(df['Clientes'])

    # Definindo o título e os rótulos dos eixos
    ax.set_title('Comparação de Horas Gastas e Valor Recebido por Cliente')
    ax.set_xlabel("Clientes")
    ax.set_ylabel("Valores em Horas/10000 e R$/1000000")

    # Adicionando legenda
    ax.legend(loc='upper left')

    # Salvando o gráfico e fechando a figura
    plt.savefig(caminho_imagem, format='png')
    plt.show()  # Opcional: mostra o gráfico no console
    plt.close(fig)  # Fecha a figura após salvar
