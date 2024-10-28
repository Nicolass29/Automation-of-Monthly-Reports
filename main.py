from dados import gerar_dados
from filtro import gerar_relatorio
from grafico import gerar_grafico
from datetime import datetime

if __name__ == "__main__":
    # Defina o caminho do arquivo de entrada
    caminho_entrada = r'C:\Users\MEUCOMPUTADOR\Desktop\teste\teste.xlsx'
    # Defina o caminho do arquivo de saída
    now = datetime.now().strftime("%d-%m-%Y_%H-%M")
    caminho_saida = fr'C:\Users\MEUCOMPUTADOR\Desktop\teste\novo\novos_{
        now}.xlsx'
    caminho_imagem = fr'C:\Users\MEUCOMPUTADOR\Desktop\teste\grafico_{now}.png'
    gerar_dados(10000, caminho_entrada)
    relatorio = gerar_relatorio(caminho_entrada, caminho_saida)
    gerar_grafico(relatorio, caminho_imagem)
