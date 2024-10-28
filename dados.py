import pandas as pd
import random


def gerar_dados(linhas, caminho_entrada):
    projetos = ['Projeto A', 'Projeto B', 'Projeto C', 'Projeto D']
    meses = pd.date_range(start='2024-01-01', periods=24,
                          freq='ME').strftime('%b/%Y').tolist()
    clientes = ['Empresa 1', 'Empresa 2',
                'Empresa 3', 'Empresa 4', 'Empresa 5']

    data = {
        'Projeto': [random.choice(projetos) for _ in range(linhas)],
        'Finalização': [random.choice(meses) for _ in range(linhas)],
        'Horas gastas': [random.randint(10, 50) for _ in range(linhas)],
        'Valor recebido': [f'R${random.randint(10, 100):,.2f}' for _ in range(linhas)],
        'Clientes': [random.choice(clientes) for _ in range(linhas)],
        'Satisfacao': [random.randint(1, 10) for _ in range(linhas)]
    }

    df = pd.DataFrame(data)
    df.to_excel(caminho_entrada, index=False)
    return df
