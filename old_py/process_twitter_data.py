"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import community.community_louvain as louvain #in PyPi = import community as louvain
from itertools import count
"""


"""
# ========== PARTE 1: PROCESSAMENTO COM AMOSTRA DE 1000 LINHAS ==========
def process_twitter_data():
    if os.path.exists('twitter_network.csv'):
        print("Arquivo 'twitter_network.csv' já existe. Pulando processamento.")
        return
    
    # Ler APENAS 1000 linhas para teste mínimo
    df = pd.read_csv(
        'twitter_combined.txt', 
        sep=' ', 
        header=None, 
        names=['user1', 'user2'],
        nrows=1000  # AMOSTRA DE 1000 LINHAS
    )
    
    # Calcular pesos corretamente
    interaction_counts = df.groupby(['user1', 'user2']).size().reset_index(name='weight')
    interaction_counts.to_csv('twitter_network.csv', index=False)
    print(f"Arquivo gerado com {len(interaction_counts)} interações!")

# ========== PARTE 2: CARREGAR GRAFO (MANTIDO PARA 1000) ==========
def load_full_graph():
    df = pd.read_csv('twitter_network.csv')
    G = nx.from_pandas_edgelist(
        df, 
        'user1', 
        'user2', 
        edge_attr='weight', 
        create_using=nx.DiGraph()
    )
    print(f"Grafo carregado: {len(G.nodes)} nós e {len(G.edges)} arestas")
    return G

# ========== PARTE 3: ALGORITMOS (AJUSTADOS PARA PEQUENAS AMOSTRAS) ==========
def calcular_metricas(G):
    # PageRank com alpha ajustado para redes pequenas
    pagerank = nx.pagerank(G, alpha=0.85)
    top_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:3]  # Top 3 apenas
    
    return {
        'pagerank': pagerank,
        'top_influencers': top_pagerank
    }

def detectar_comunidades(G):
    # Reduzir complexidade para redes pequenas
    G_undir = G.to_undirected()
    partition = louvain.best_partition(G_undir, resolution=1.5)  # Aumentar resolução
    nx.set_node_attributes(G, partition, 'community')
    return G, partition

# ========== PARTE 4: VISUALIZAÇÃO SIMPLIFICADA ==========
def made_gephi_file(G):
    # Cria o arquivo de visualização para o Gephi
    nx.write_gexf(G, "grafo_trabalho.gexf")

def plotar_grafo_completo(G, metrics):
    plt.figure(figsize=(10, 7))
    
    # Cores e tamanhos adaptados
    communities = list(nx.get_node_attributes(G, 'community').values())
    node_size = [metrics['pagerank'][n] * 5000 for n in G.nodes()]  # Tamanho reduzido
    
    pos = nx.spring_layout(G, k=0.5, seed=42)  # Layout reprodutível
    
    nx.draw(
        G, pos,
        node_size=node_size,
        node_color=communities,
        cmap=plt.cm.tab10,
        with_labels=True,  # Rótulos habilitados para amostras pequenas
        font_size=8,
        width=0.8
    )
    
    plt.title("Rede Twitter (Amostra de 1000 Interações)")
    plt.show()
    """

# ========== EXECUÇÃO PRINCIPAL ==========
"""if __name__ == "__main__":
    process_twitter_data()  # Amostra fixa de 1000 linhas
    G = load_full_graph()
    G, partition = detectar_comunidades(G)
    metrics = calcular_metricas(G)
    
    print("\nTop 3 Influenciadores:")
    for node, score in metrics['top_influencers']:
        print(f"Usuário {node}: PageRank {score:.4f}")
    
    made_gephi_file(G)
    plotar_grafo_completo(G, metrics)"""