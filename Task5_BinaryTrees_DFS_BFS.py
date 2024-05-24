import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

def hex_color(value):
    """
    Повертає кольоровий код у форматі hex (#RRGGBB) на основі значення від 0 до 1
    """
    r = int(0 + (255 - 0) * value)
    g = int(0 + (255 - 0) * value)
    b = int(0 + (255 - 0) * value)
    return f'#{r:02x}{g:02x}{b:02x}'

def bfs_coloring(node):
    queue = [(node, 0)]
    order = 0
    while queue:
        current, level = queue.pop(0)
        current.color = hex_color(order / 10)
        order += 1
        if current.left:
            queue.append((current.left, level + 1))
        if current.right:
            queue.append((current.right, level + 1))

def dfs_coloring(node, order=0):
    if node is not None:
        node.color = hex_color(order / 10)
        order += 1
        if node.left:
            order = dfs_coloring(node.left, order)
        if node.right:
            order = dfs_coloring(node.right, order)
    return order

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з обходом у ширину (BFS)
bfs_coloring(root)
draw_tree(root, "Обхід у ширину (BFS)")

# Відображення дерева з обходом у глибину (DFS)
dfs_coloring(root)
draw_tree(root, "Обхід у глибину (DFS)")
