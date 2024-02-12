import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_paths = {}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_paths

def draw_graph(graph, shortest_paths, start_node, end_node):
    G = nx.DiGraph()

    for node, edges in graph.items():
        for edge, weight in edges.items():
            G.add_edge(node, edge, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color='lightblue', font_size=12)

    nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green', node_size=7000)
    nx.draw_networkx_nodes(G, pos, nodelist=[end_node], node_color='red', node_size=7000)

    path = [end_node]
    current_node = end_node
    while current_node != start_node:
        current_node = shortest_paths[current_node]
        path.append(current_node)
    path.reverse()

    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Shortest Path from {} to {}".format(start_node, end_node))
    plt.show()

# Definimos el grafo que representa la red social
graph = {
    'Alice': {'Bob': 5, 'Charlie': 2},
    'Bob': {'Alice': 5, 'David': 3},
    'Charlie': {'Alice': 2, 'David': 7},
    'David': {'Bob': 3, 'Charlie': 7}
}

# Especificamos los nodos de inicio y fin para encontrar la distancia más corta entre ellos
start_node = 'Alice'
end_node = 'David'

# Aplicamos el algoritmo de Dijkstra para encontrar la distancia más corta y el camino más corto
distances, shortest_paths = dijkstra(graph, start_node)

# Imprimimos la distancia más corta entre los nodos especificados
print("Distancia más corta entre {} y {}: {}".format(start_node, end_node, distances[end_node]))

# Imprimimos el camino más corto entre los nodos especificados
path = [end_node]
current_node = end_node
while current_node != start_node:
    current_node = shortest_paths[current_node]
    path.append(current_node)
path.reverse()
print("Camino más corto:", ' -> '.join(path))

# Dibujamos el grafo y el camino más corto
draw_graph(graph, shortest_paths, start_node, end_node)
