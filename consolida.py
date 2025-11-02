import pandas as pd
import glob
import os

# Caminho da pasta (ajuste se necessário)
pasta = os.path.dirname(__file__)

# Lista apenas arquivos mensais (2023 e 2024)
padroes = [
    os.path.join(pasta, "*.csv"),
    os.path.join(pasta, "*.xlsx"),
]

arquivos = []
for padrao in padroes:
    arquivos.extend(glob.glob(padrao))

# Ignorar arquivos que não são dos meses
meses_validos = [
    "JANEIRO", "FEVEREIRO", "MARCO", "ABRIL", "MAIO", "JUNHO",
    "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
]

# Lista final apenas com meses (2023 e 2024)
arquivos_mensais = [
    a for a in arquivos
    if any(mes in os.path.basename(a).upper() for mes in meses_validos)
    and "CONSOLIDADO" not in os.path.basename(a).upper()
]

print(f"📂 {len(arquivos_mensais)} arquivos mensais encontrados:")

tabelas = []
for arquivo in arquivos_mensais:
    nome = os.path.basename(arquivo)
    print(f"→ Lendo {nome}")
    try:
        if arquivo.endswith(".csv"):
            df = pd.read_csv(arquivo, sep=";", encoding="utf-8", dtype=str)
        else:
            df = pd.read_excel(arquivo, dtype=str)
        df["Origem"] = nome
        tabelas.append(df)
    except Exception as e:
        print(f"❌ Erro ao ler {nome}: {e}")

if tabelas:
    consolidado = pd.concat(tabelas, ignore_index=True)
    caminho_saida = os.path.join(pasta, "Consolidado_SP.csv")
    consolidado.to_csv(caminho_saida, sep=";", index=False, encoding="utf-8-sig")
    print(f"\n✅ Consolidado salvo em: {caminho_saida}")
else:
    print("⚠️ Nenhum arquivo válido encontrado.")
