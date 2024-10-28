import numpy as np
import matplotlib.pyplot as plt


def gerar_grafico(df, caminho_imagem):
    # Converte a coluna 'Valor recebido' para float se necessário
    df['Valor recebido'] = df['Valor recebido'].replace(
        {r'R\$': '', r'\.': '', ',': '.'}, regex=True).astype(float)

    # Criação da figura do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    # Largura das barras
    bar_width = 0.2

    # Posições das barras no eixo X
    clientes = np.arange(len(df['Clientes']))

    # Gráfico de Horas Gastas
    ax.bar(clientes, df['Horas gastas'] / 10000, width=bar_width,
           color='b', alpha=0.6, label='Horas')

    # Gráfico de Valor Recebido (deslocado para a direita)
    ax.bar(clientes + bar_width, df['Valor recebido'] / 1000000, width=bar_width,
           color='g', alpha=0.6, label='R$')

    # Configurações do eixo X com os nomes dos clientes
    ax.set_xticks(clientes + bar_width / 2)
    ax.set_xticklabels(df['Clientes'])

    # Definições do título e rótulos dos eixos
    ax.set_title('Comparação de Horas Gastas e Valor Recebido por Cliente')
    ax.set_xlabel("Clientes")
    ax.set_ylabel("Valores em Horas/10000 e R$/1000000")

    # Adiciona legenda
    ax.legend(loc='upper left')

    # Salva o gráfico e fecha a figura
    plt.savefig(caminho_imagem, format='png')
    plt.show()  # Opcional: exibe o gráfico
    plt.close(fig)  # Fecha a figura após salvar
