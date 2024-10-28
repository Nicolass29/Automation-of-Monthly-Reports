import pandas as pd


def gerar_relatorio(caminho_entrada, caminho_saida):
    dados = pd.read_excel(caminho_entrada)
    dados['Valor recebido'] = dados['Valor recebido'].replace(
        {r'R\$': '', r'\.': '', ',': '.'}, regex=True).astype(float)

    relatorio = dados.groupby('Clientes').agg(
        {'Horas gastas': 'sum', 'Valor recebido': 'sum',
            'Satisfacao': lambda x: round(x.mean())}
    ).reset_index()

    relatorio['Valor recebido'] = relatorio['Valor recebido'].apply(
        lambda x: f'R${x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

    relatorio.to_excel(caminho_saida, index=False)
    return relatorio
