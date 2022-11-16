from tabulate import tabulate

inputs = [
    ("AC", 2),
    ("AB", 4),
    ("BD", 1),
    ("CB", 1),
    ("CD", 8)
]

nodes = ['A', 'B', 'C', 'D']


class Algorithms:

    def __init__(self, inputs):
        self.inputs = inputs

    # Kruskal Algorithm

    def kruskal(self):
        kruskal_list = []
        # sorting the inputs by their arc's weight
        initial_list = self.inputs
        initial_list.sort(key=lambda item: item[1])
        childhood_list = {}
        parent_list = []
        # transferring inputs to tuples (source, weight, destination)
        kruskal_edges = []
        for item in initial_list:
            kruskal_edges.append((item[0][0], item[1], item[0][1]))

        # filling kruskal list.
        def is_child(item):

            for char in parent_list:
                if item in childhood_list[char]:
                    return True
                else:
                    return False

        def is_parent(item):
            for char in parent_list:
                if item != char:
                    pass
                else:
                    return True
            return False

        def get_parent(item):
            for char in parent_list:
                if item in childhood_list[char]:
                    return char
                else:
                    return None

        for couple in kruskal_edges:
            element0 = couple[0]
            element2 = couple[2]
            parent0 = get_parent(couple[0])
            parent2 = get_parent(couple[2])
            isChild0 = is_child(couple[0])
            isChild2 = is_child(couple[2])
            isParent0 = is_parent(couple[0])
            isParent2 = is_parent(couple[2])
            if len(kruskal_list) == 0:
                kruskal_list.append(couple)
                childhood_list[couple[0]] = [couple[2]]
                parent_list.append(couple[0])
            else:
                if (not isChild0 and not isParent0) and (not isChild2 and not isParent2):
                    kruskal_list.append(couple)
                    parent_list.append(element0)
                    childhood_list[element0] = [element2]
                elif (not isChild0 and not isParent0) and isChild2:
                    kruskal_list.append(couple)
                    childhood_list[parent2].append(element0)
                elif (not isChild0 and not isParent0) and isParent2:
                    kruskal_list.append(couple)
                    childhood_list[element2].append(element0)
                elif (not isChild2 and not isParent2) and isParent0:
                    kruskal_list.append(couple)
                    childhood_list[element0].append(element2)
                elif (not isChild2 and not isParent2) and isChild0:
                    kruskal_list.append(couple)
                    childhood_list[parent0].append(element2)
                elif isChild0 and isChild2:
                    if parent0 == parent2:
                        pass
                    else:
                        kruskal_list.append(couple)
                        for cha in childhood_list[parent0]:
                            childhood_list[parent2].append(cha)
                        childhood_list[parent2].append(parent0)
                        parent_list.remove(parent0)
                        childhood_list.pop(parent0)
                elif isChild0 and isParent2:
                    if parent0 == element2:
                        pass
                    else:
                        kruskal_list.append(couple)

                        for el in childhood_list[parent0]:
                            childhood_list[element2].append(el)
                        childhood_list[element2].append(parent0)
                        childhood_list.pop(parent0)
                        parent_list.remove(parent0)
                elif isChild2 and isParent0:
                    if parent2 == element0:
                        pass
                    else:
                        kruskal_list.append(couple)
                        for char in childhood_list[parent2]:
                            childhood_list[element0].append(char)
                        childhood_list[element0].append(parent2)
                        childhood_list.pop(parent2)
                        parent_list.remove(parent2)
                else:
                    if element0 == element2:
                        pass
                    else:
                        kruskal_list.append(couple)
                        for ch in childhood_list[element0]:
                            childhood_list[element2].append(ch)
                        childhood_list[element2].append(element0)
                        childhood_list.pop(element0)
                        parent_list.remove(element0)
        return kruskal_list

    # DFS Algorithm

    visited_dfs = set()  # Set to keep track of visited nodes of the graph.

    def dfs(self, visited_dfs, graph, node):  # graph is the adj_list || visited is the set that will be
        if node not in visited_dfs:  # returned || node is the node to start from
            visited_dfs.add(node)
            for neighbour in graph[node]:
                self.dfs(visited_dfs, graph, neighbour)
        return visited_dfs

    visited_bfs = []  # List for visited nodes.

    def bfs(self, visited_bfs, graph, node):  # function for BFS
        queue = []  # Initialize a queue
        visited_bfs.append(node)
        queue.append(node)

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)
            print(m, end=" ")

            for neighbour in graph[m]:
                if neighbour not in visited_bfs:
                    visited_bfs.append(neighbour)
                    queue.append(neighbour)
        return visited_bfs

    # Prime's Algorithme:

    def prime(self, start):

        prime_final_list = []
        prim_book = {}
        for node in nodes:
            prim_book[node] = []
            for item in self.inputs:
                if item[0][0] != node and item[0][1] != node:
                    pass
                else:
                    prim_book[node].append(item)

        for node in nodes:
            prim_book[node].sort(key=lambda item: item[1])

        if start not in nodes:
            return "The Given node does not exist in this Graph"
        else:
            pass

        checked_nodes = []

        def fill_prime():
            while len(prim_book) != 1:
                if len(checked_nodes) == 0:
                    checked_nodes.append(start)
                next_edge = prim_book[start][0]
                next_node = next_edge[0][1] if (next_edge[0][1] not in checked_nodes) else next_edge[0][0]
                prime_final_list.append(next_edge)
                checked_nodes.append(next_node)
                prim_book[start].remove(next_edge)
                prim_book[next_node].remove(next_edge)
                for lis in prim_book[next_node]:
                    prim_book[start].append(lis)
                del prim_book[next_node]
                prim_book[start].sort(key=lambda ite: ite[1])

        fill_prime()

        return prime_final_list

    # Dijkstra's Algorithm

    def dijkstra(self, start):
        # ===================================Initialisation======================================
        for item in self.inputs:
            if item[1] < 0:
                return "The Dikjsta's Algorithme can't be executed because the exist of a negative edge choose Bellman Ford Instead"
        checked_nodes = [start]
        non_checked_nodes = [node for node in nodes if node not in checked_nodes]
        current_source = checked_nodes[-1]
        distances_list = {}
        predecessors_list = {}
        for item in self.inputs:
            if current_source in item[0]:
                distances_list[item[0][1]] = item[1]
                predecessors_list[item[0][1]] = current_source
            else:
                for char in item[0]:
                    if char in distances_list:
                        pass
                    else:
                        distances_list[char] = float('infinity')
                    if char in predecessors_list:
                        pass
                    else:
                        predecessors_list[char] = "N"
        # ================================= Algorithme Start ====================================
        while len(non_checked_nodes) != 0:

            # Get The Smallest item in the distances list.

            smallest_one_value = 99999999999999
            smallest_one_key = None
            for dis in distances_list:
                if distances_list[dis] < smallest_one_value and dis not in checked_nodes:
                    smallest_one_value = distances_list[dis]
                    smallest_one_key = dis
                else:
                    pass
            checked_nodes.append(smallest_one_key)
            non_checked_nodes.remove(smallest_one_key)
            # Get The none checked Neighbors of The Smallest One

            smallest_one_neighbors = []
            for element in self.inputs:
                if smallest_one_key == element[0][0] and element[0][1] not in checked_nodes:
                    smallest_one_neighbors.append((element[0][1], element[1]))
                elif smallest_one_key == element[0][1] and element[0][0] not in checked_nodes:
                    smallest_one_neighbors.append((element[0][0], element[1]))
                else:
                    pass

            # Calculate and Update The distances:

            for neighbor in smallest_one_neighbors:
                minimum = min(distances_list[neighbor[0]], distances_list[smallest_one_key] + neighbor[1])
                if minimum < distances_list[neighbor[0]]:
                    distances_list[neighbor[0]] = minimum
                    predecessors_list[neighbor[0]] = smallest_one_key
                else:
                    pass
            smallest_one_neighbors.clear()

        dijkstra_table = {}
        index = ['Distance', 'Predecessor']
        for item in distances_list:
            dijkstra_table[item] = [distances_list[item], predecessors_list[item]]
        return tabulate(dijkstra_table, headers='keys', tablefmt='fancy_grid', showindex=index)

    # Bellman Ford's Algorithme

    def bellman_ford(self, start):
        # ===================================Initialisation======================================
        # Filling Edges List

        edges_list = []
        for item in self.inputs:
            source = item[0][0]
            destination = item[0][1]
            weight = item[1]
            edges_list.append((source, destination, weight))

        # Filling Distances List

        distances_list = {}
        for node in nodes:
            distances_list[node] = float('infinity') if node != start else 0
        # Filling Predecessors List

        predecessors_list = {}
        for node in nodes:
            predecessors_list[node] = 'N' if node != start else '-'
        # ================================= Algorithme Start ====================================
        # Bellman-Ford Algorithme Running
        for i in range(len(nodes)):
            for edge in edges_list:
                if distances_list[edge[1]] > distances_list[edge[0]] + edge[2]:
                    distances_list[edge[1]] = distances_list[edge[0]] + edge[2]
                    predecessors_list[edge[1]] = edge[0]
        bellman_ford_table = {}
        index = ['Distance', 'Predecessor']
        for item in distances_list:
            bellman_ford_table[item] = [distances_list[item], predecessors_list[item]]
        return tabulate(bellman_ford_table, headers='keys', tablefmt='fancy_grid', showindex=index)


