import heapq
import networkx as nx
import matplotlib.pyplot as plt

class User:
    def __init__(self, name):
        self.name = name
        self.shared_with = {}  # Dictionary to keep track of shared times with other users

def update_distance(user1, user2):
    # Update shared times between user1 and user2
    if user2.name not in user1.shared_with:
        user1.shared_with[user2.name] = 1
    else:
        user1.shared_with[user2.name] += 1
        #user2.shared_with[user1.name] += 1
    
    if user1.name not in user2.shared_with:
        user2.shared_with[user1.name] = 1
    else:
        user2.shared_with[user1.name] += 1    

def dijkstra(graph, start):
    distances = {node.name: float('infinity') for node in graph}
    distances[start.name] = 0
    shortest_paths = {}

    priority_queue = [(0, start.name)]

    while priority_queue:
        current_distance, current_user_name = heapq.heappop(priority_queue)
        current_user = next(user for user in graph if user.name == current_user_name)

        if current_distance > distances[current_user_name]:
            continue

        for neighbor, weight in graph[current_user].items():
            neighbor_name = neighbor.name
            distance = current_distance + weight
            if distance < distances[neighbor_name]:
                distances[neighbor_name] = distance
                shortest_paths[neighbor_name] = current_user_name
                heapq.heappush(priority_queue, (distance, neighbor_name))

    return distances, shortest_paths

def calculate_distance(shared_times):
    if shared_times == 0:
        return 100  # Initial distance
    else:
        return 100 / (shared_times + 1)

def find_suggestions(users, distances):
    suggestions = []
    for user1 in users:
        for user2 in users:
            if user1 != user2 and distances[user1.name][user2.name] < 40:
                suggestions.append(user2.name)
    return suggestions

def find_friend_recommendations(users, distances):
    recommendations = []
    for user1 in users:
        for user2 in users:
            if user1 != user2 and distances[user1.name][user2.name] <= 10:
                recommendations.append(user2.name)
    return recommendations

def draw_graph(graph, suggestions, recommendations):
    G = nx.DiGraph()

    for user, edges in graph.items():
        for friend, weight in edges.items():
            G.add_edge(user.name, friend.name, weight=weight, label=f"{weight:.2f}")  # Add edge labels

    pos = nx.fruchterman_reingold_layout(G)  # Utilizar fruchterman_reingold_layout para posicionar los nodos
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10)

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight suggested users
    nx.draw_networkx_nodes(G, pos, nodelist=suggestions, node_color='lightgreen', node_size=1500)

    # Highlight recommended users
    nx.draw_networkx_nodes(G, pos, nodelist=recommendations, node_color='lightcoral', node_size=1500)

    plt.title("Users and Recommendations")
    plt.show()

# Example usage, simulating some users:
users = [User("Alice"), User("Bob"), User("Charlie"), User("Jhon")]

#creation of some simulated interaction between users:
update_distance(users[0], users[1])  # Alice shares with Bob
update_distance(users[1], users[2])  # Bob shares with Charlie
update_distance(users[2], users[0])  # Charlie shares with Alice
update_distance(users[1], users[0])  # Bob shares again with Alice
update_distance(users[1], users[0])  # Bob shares again with Alice
update_distance(users[1], users[0])  # Bob shares again with Alice
update_distance(users[0], users[1])  # Alice shares with Bob
update_distance(users[1], users[0])  # Bob shares again with Alice
update_distance(users[1], users[2])  # Bob shares with Charlie
update_distance(users[0], users[1])  # Alice shares with Bob
update_distance(users[0], users[1])  # Alice shares with Bob
update_distance(users[1], users[0])  # Bob shares again with Alice
update_distance(users[0], users[3])  # Alice shares with Jhon

# Modify the graph creation to use user objects as keys
graph = {user: {} for user in users}
for user1 in users:
    for user2 in users:
        if user1 != user2:
            shared_times = user1.shared_with.get(user2.name, 0)
            distance = calculate_distance(shared_times)
            graph[user1][user2] = distance

# Apply Dijkstra's algorithm to find shortest paths
distances = {}
for user in users:
    dist, _ = dijkstra(graph, user)
    distances[user.name] = dist

# Find suggestions and friend recommendations
suggestions = find_suggestions(users, distances)
recommendations = find_friend_recommendations(users, distances)


print("Suggestions:", suggestions)
print("Friend recommendations:", recommendations)

# Draw graph with suggestions and recommendations
draw_graph(graph, suggestions, recommendations)
