import pandas as pd


def gerar_relatorio(caminho_entrada, caminho_saida):
    # Lê os dados do arquivo Excel
    dados = pd.read_excel(caminho_entrada)

    # Converte a coluna 'Valor recebido' de string para float para cálculos
    dados['Valor recebido'] = dados['Valor recebido'].replace(
        {r'R\$': '', r'\.': '', ',': '.'}, regex=True).astype(float)

    # Agrupa os dados por cliente e calcula totais e média de satisfação
    relatorio = dados.groupby('Clientes').agg(
        {'Horas gastas': 'sum',
         'Valor recebido': 'sum',
         'Satisfacao': lambda x: round(x.mean())}
    ).reset_index()

    # Formata a coluna 'Valor recebido' de volta para string com o formato monetário
    relatorio['Valor recebido'] = relatorio['Valor recebido'].apply(
        lambda x: f'R${x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

    # Salva o relatório consolidado em um novo arquivo Excel
    relatorio.to_excel(caminho_saida, index=False)
    return relatorio
