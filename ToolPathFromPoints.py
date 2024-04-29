import pandas as pd
import pandas as pd
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

#get coords from file
inputFileName = "Coords3.csv"
outputFileName = "saida.txt"
coords_df = pd.read_csv(inputFileName, sep=';', header=0)

#Calculate distance matrix
points = coords_df[['X', 'Y']].values # Extract X and Y coordinates
distances = cdist(points, points)# Calculate pairwise distances
distances_df = pd.DataFrame(distances, index=coords_df.index, columns=coords_df.index)# Create DataFrame from distances
    
#Solve Traveling merchant   
n = len(coords_df)
ordered_indices = [0]  # Começamos com o primeiro ponto
remaining_indices = set(range(1, n))  # Índices dos pontos restantes

while remaining_indices:
    last_index = ordered_indices[-1]
    nearest_index = min(remaining_indices, key=lambda x: distances_df[last_index][x])
    ordered_indices.append(nearest_index)
    remaining_indices.remove(nearest_index)

route = coords_df.iloc[ordered_indices]# Reordenando as coordenadas de acordo com a ordem encontrada

#Plot the Route
plt.figure(figsize=(8, 6))
plt.plot(route['X'], route['Y'], marker='o', linestyle='-')
plt.title('Ordered Coordinates')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
        