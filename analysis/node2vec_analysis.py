import numpy as np
import pandas as pd
import networkx as nx
from node2vec import Node2Vec

EMBEDDING_FILENAME = "EMBEDDING_FILENAME"
EMBEDDING_MODEL_FILENAME = "EMBEDDING_MODEL_FILENAME"
EDGES_EMBEDDING_FILENAME = "EDGES_EMBEDDING_FILENAME"

# Create a graph
#graph = nx.fast_gnp_random_graph(n=100, p=0.5)

edgelist = pd.read_csv('../output/HS6_Proximities_0.5.csv', header=1, index_col=False).values.tolist()


#print(edgelist)

#edgelist['weight'][:] = edgelist['weight'][:]*2


#graph = nx.Graph(edgelist)
#print(nx.degree_histogram(G))



graph = nx.Graph()

print("loading weighted edges")

graph.add_weighted_edges_from(edgelist)
print("control weighted edges")

for n, nbrs in graph.adj.items():
       for nbr, eattr in nbrs.items():
              wt = eattr['weight']
              #eattr['weight'] = 1 - eattr['weight']
              print(f"({n}, {nbr}, {wt:.3})")
              




# Precompute probabilities and generate walks - **ON WINDOWS ONLY WORKS WITH workers=1**
node2vec = Node2Vec(graph, dimensions=64, walk_length=30, num_walks=200, workers=4)  # Use temp_folder for big graphs

# Embed nodes
model = node2vec.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `dimensions` and `workers` are automatically passed (from the Node2Vec constructor)

# Look for most similar nodes
print(model.wv.most_similar('10519'))  # Output node names are always strings

# Save embeddings for later use
model.wv.save_word2vec_format(EMBEDDING_FILENAME)

# Save model for later use
model.save(EMBEDDING_MODEL_FILENAME)

# Embed edges using Hadamard method
from node2vec.edges import HadamardEmbedder

edges_embs = HadamardEmbedder(keyed_vectors=model.wv)

# Look for embeddings on the fly - here we pass normal tuples
print(edges_embs[('10519', '20441')])
''' OUTPUT
array([ 5.75068220e-03, -1.10937878e-02,  3.76693785e-01,  2.69105062e-02,
       ... ... ....
       ..................................................................],
      dtype=float32)
'''

# Get all edges in a separate KeyedVectors instance - use with caution could be huge for big networks
edges_kv = edges_embs.as_keyed_vectors()

# Look for most similar edges - this time tuples must be sorted and as str
print(edges_kv.most_similar(str(('10519', '20441'))))

# Save embeddings for later use
edges_kv.save_word2vec_format(EDGES_EMBEDDING_FILENAME)


