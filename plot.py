import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# load dataset into Pandas DataFrame
heroes_df = pd.read_csv("data/heroes_information.csv")
powers_df = pd.read_csv("data/super_hero_powers.csv")

G = nx.Graph()

#G.add_nodes_from(powers_df.columns.values)
for row_index, row in powers_df.iterrows():
    # print(f"({row_index}, {row[0]}): ")
    for col_index, col in zip(powers_df.columns[1:], row[1:]):
        #print(f"  ({col_index}, {col})")
        if(col): 
            G.add_edge(row[0], col_index)
    
nx.draw_kamada_kawai(G, with_labels = False, node_size = 2) 
plt.show()
