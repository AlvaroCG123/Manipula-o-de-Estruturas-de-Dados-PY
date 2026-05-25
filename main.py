import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('one_piece_bounties.csv')
    df['Bounty'] = df['Bounty'].fillna(0) 
except FileNotFoundError:
    print("Erro: O arquivo 'one_piece_bounties.csv' não foi localizado no diretório atual.")
    exit()

def agrupar_afiliacao():
    print("\n--- 1. Agrupar por Afiliação (Top 10 Tripulações) ---")
    top_grupos = df['Affiliation'].value_counts().head(10)
    print(top_grupos.to_string())

def ordenar_recompensa():
    print("\n--- 2. Ordenar por Recompensa (Top 15 Procurados) ---")
    top_procurados = df.sort_values(by='Bounty', ascending=False).head(15)
    for index, row in top_procurados.iterrows():
        print(f"{row['Name']}: {row['Bounty']:,.0f} Berries")

def comparar_recompensas():
    print("\n--- 3. Comparação: Chapéus de Palha vs. Marinha ---")
    soma_chapeus = df[df['Affiliation'] == 'Straw Hat Pirates']['Bounty'].sum()
    soma_marinha = df[df['Affiliation'] == 'Marines']['Bounty'].sum()
    
    print(f"Total Chapéus de Palha: {soma_chapeus:,.0f} Berries")
    print(f"Total Marinha: {soma_marinha:,.0f} Berries")
    
    if soma_chapeus > soma_marinha:
        print("Resultado: A tripulação dos Chapéus de Palha possui o maior valor acumulado.")
    else:
        print("Resultado: A Marinha possui o maior valor acumulado.")

def interseccao_conjuntos():
    print("\n--- 4. Intersecção: Marinheiros E Usuários de Akuma no Mi ---")
    set_marinheiros = set(df[df['Is_Marine'] == True]['Name'])
    set_usuarios_fruta = set(df[df['Has_Devil_Fruit'] == True]['Name'])
    
    marinheiros_com_poder = set_marinheiros.intersection(set_usuarios_fruta)
    
    print(f"Encontrados {len(marinheiros_com_poder)} marinheiros com Akuma no Mi:")
    for nome in marinheiros_com_poder:
        print(f"- {nome}")

def grafico_barras():
    print("\n--- 5. Gerando Gráfico de Barras... ---")
    top_10 = df.sort_values(by='Bounty', ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_10['Name'], top_10['Bounty'], color='crimson')
    plt.title('Top 10 Maiores Recompensas de One Piece')
    plt.ylabel('Recompensa (em Berries)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def grafico_pizza():
    print("\n--- 6. Gerando Gráfico de Pizza... ---")
    frutas_df = df[df['Devil_Fruit_Type'].notna() & (df['Devil_Fruit_Type'] != 'None')]['Devil_Fruit_Type'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(frutas_df, labels=frutas_df.index, autopct='%1.1f%%', startangle=140)
    plt.title('Proporção dos Tipos de Akuma no Mi')
    plt.show()

while True:
    print("\n=========================================")
    print("   MENU ONE PIECE - ESTRUTURA DE DADOS   ")
    print("=========================================")
    print("1. Agrupar por afiliação")
    print("2. Ordenar por recompensa")
    print("3. Comparar recompensas: Soma")
    print("4. Intersecção: Marinheiros com Fruta")
    print("5. Gráfico de Barras: Top 10")
    print("6. Gráfico de Pizza: Frutas")
    print("0. Encerrar o programa")
    print("=========================================")
    
    opcao = input("Selecione uma opção (0 a 6): ")
    
    if opcao == '1':
        agrupar_afiliacao()
    elif opcao == '2':
        ordenar_recompensa()
    elif opcao == '3':
        comparar_recompensas()
    elif opcao == '4':
        interseccao_conjuntos()
    elif opcao == '5':
        grafico_barras()
    elif opcao == '6':
        grafico_pizza()
    elif opcao == '0':
        print("Sistema encerrado com sucesso.")
        break
    else:
        print("Opção inválida. Por favor, insira um valor numérico válido.")