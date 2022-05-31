# libraries
import os
import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.colors

def update_opinions(n1, n2, alpha, colorDict):
    colorDict[n1] = colorDict[n1] + alpha * (colorDict[n2] - colorDict[n1])
    colorDict[n2] = colorDict[n2] + alpha * (colorDict[n1] - colorDict[n2])
    return colorDict

### USER FILE PATHS AND PARAMETERS ###
cwd = os.getcwd()

images_path = rf"{cwd}\images\\"

isExist = os.path.exists(images_path)
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(images_path)

colorbar_path = rf"{images_path}\colorbar.jpeg"
base_path = rf"{images_path}\base.jpeg"

# Define constants
C = .6
alpha = .5
num_iterations = 250
num_nodes = 25
######################

# Build your graph
nodeList = range(num_nodes)
G = nx.complete_graph(nodeList) 
G_pos = nx.spring_layout(G)

# Randomly init opionion profile
colorDict = {}
for node in G:
    colorDict[node] = random.uniform(0, 1)

# Create colorbar, and save externally
# a = np.array([[0,1]])
# pl.figure(figsize=(9, 1.5))
# img = pl.imshow(a, cmap=plt.cm.bwr)
# pl.gca().set_visible(False)
# cax = pl.axes([0.1, 0.2, 0.8, 0.6])
# pl.colorbar(orientation="horizontal", cax=cax)
# colorbar_path = r"\Users\danec\Desktop\Seminar Material\animation\illustration\colorbar.jpeg"
# plt.savefig(colorbar_path)

# Draw base graph
nx.draw(G, with_labels=True, node_size=500, node_color = list(colorDict.values()), width = .1, pos=G_pos, font_size=16, vmin = 0,vmax = 1,cmap = plt.cm.bwr)
plt.savefig(base_path)


for timestep in range(num_iterations):
    # randomly choose two nodes
    n1 = random.choice(nodeList)
    n2 = random.choice(nodeList)

    # Omit the option where nodes are the same
    if n1 == n2:
        continue
    # Force n1 to be the smaller, for coloring reasons
    if n1 > n2:
        temp = n2
        n2 = n1
        n1 = temp

    # Highlight nodes
    # nx.draw_networkx(G.subgraph([n1, n2]), node_size=500, pos=G_pos, width=0, font_size=16, node_color=[colorDict[n1], colorDict[n2]], font_color='yellow',vmin = 0,vmax = 1, cmap = plt.cm.bwr)
    # # nx.draw(G, with_labels=False, node_size=500, node_color = list(colorDict.values()), pos=G_pos, width=.5, font_size=14, cmap = plt.cm.bwr)
    # highlight_path = rf"{images_path}\highlight_{timestep}.jpeg"
    # plt.savefig(highlight_path)

    # Update Opinion
    colorDict = update_opinions(n1, n2, alpha, colorDict)

    # Save updated graph
    nx.draw(G, with_labels=True, node_size=500, node_color = list(colorDict.values()), pos=G_pos, font_size = 16, font_color = "black", width=0, vmin = 0,vmax = 1,cmap = plt.cm.bwr)
    updated_graph_path = rf"{images_path}\update_{timestep}.jpeg"
    plt.savefig(updated_graph_path)
    # else:
        # No opinion updates
        # Highlight edge nodes
        # nx.draw_networkx(G.subgraph([n1, n2]), node_size=500, pos=G_pos, width=0, font_size=16, font_color = "cyan", node_color=[colorDict[n1], colorDict[n2]], vmin = 0,vmax = 1, cmap = plt.cm.bwr)
        # bad_graph_path = rf"{images_path}\update_{timestep}.jpeg"
        # plt.savefig(bad_graph_path)
