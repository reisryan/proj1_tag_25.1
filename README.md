# Projeto de Análise de Rede Social Twitter - Proj1_TAG_25.1

**Disciplina:** Teoria e Aplicação de Grafos - TAG, 2025/1
**Professor:** Díbio
**Autores:**
* Luiz Henrique Silva de Andrade - 211010430
* Marcelo Marques Rodrigues - 221018960
* Ryan Reis Fontenele - 211036132

**Objetivo:** Este projeto visa analisar estruturas de uma rede social baseada em dados do Twitter para identificar características da rede, nós influentes e comunidades, e discutir o potencial de disseminação de informação (incluindo notícias falsas) através dessa estrutura.

**Dependências:**

Execute no terminal o comando:
pip install -r requirements.txt

**Implementação:**

Cria um grafo apartir do dataset twitter_combined.txt com as frequências de interações entre os usuários da rede social Twitter através de retweets e mentions, sendo direcionado e com pesos em suas arestas.

Calcula PageRank em busca dos usuários mais influentes.

Analisa Centralidade de Grau , Proximidade e Intermediação. Indicadores de conexão entre comunidades, nível compartilhação e nível de alcance.

Encontra comunidades, agrupamentos de usuários.

Gera visualizações dos grafos e exporta para Gephi.


