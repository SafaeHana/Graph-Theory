import networkx as nx
import matplotlib.pyplot as plot
from tabulate import tabulate




class G:

    def __init__(self, Entries, cout_exist):
        self.cout_exist = cout_exist
        self.enodes = []
        self.liste_associee = {}
        self.M_incidence = []
        self.list_Ad = {}
        self.nodes = []
        self.edges = []
        self.Entries = Entries

    def create_edges(self):
        
        if self.cout_exist:
            self.edges = [edge[0] for edge in self.Entries]
        else:
            self.edges = [edge for edge in self.Entries]
        return self.edges

    def create_nodes(self):
       
        for edge in self.edges:
            for node in edge:
                if node not in self.nodes:
                    self.nodes.append(node)
        self.nodes.sort()

        return self.nodes

    def create_list_Ad(self):

       
        for node in self.nodes:
            self.list_Ad[node] = []

        

        for edge in self.edges:
            if edge[0] not in self.list_Ad[edge[1]]:
                self.list_Ad[edge[1]].append(edge[0])
                if edge[1] not in self.list_Ad[edge[0]]:
                    self.list_Ad[edge[0]].append(edge[1])

        return self.list_Ad

    def create_M_incidence(self):
        

        self.M_incidence = []
        for node in self.nodes:
            self.M_incidence.append([])
        for j in range(len(self.nodes)):
            for i in range(len(self.nodes)):
                self.M_incidence[i].append(0)

        

        for i in range(len(self.M_incidence)):
            actuel_row = self.M_incidence[i]
            actuel_node = self.nodes[i]
            actuel_node_list_Ad = self.list_Ad[actuel_node]
            for element in actuel_node_list_Ad:
                actuel_row[self.nodes.index(element)] = 1

        return self.M_incidence

    def is_simple(self):
        for edge in self.edges:
            if edge[0] == edge[1]:
                return False
        for i in range(len(self.edges)):
            actuel_edge = self.edges[i]
            for j in range(len(self.edges)):
                actuel_compared_edge = self.edges[j]
                if actuel_edge == actuel_compared_edge:
                    pass
                elif actuel_edge[0] == actuel_compared_edge[1] and actuel_edge[1] == actuel_compared_edge[0]:
                    text="n'est pas simple"
           
                    return text
                else:
                    pass
            text="Simple"
            return text

    def is_complete(self):
        if self.is_simple():
            for node in self.nodes:
                if len(self.list_Ad[node]) == len(self.nodes) - 1:
                    pass
                elif len(self.list_Ad[node]) != len(self.nodes) - 1:
                    text="n'est pas Complet"
                
                    return text
            text="Complet"
            return text
        else:
            text="n'est pas Complet"
            return text

    def True_associee(self):

        def list_associee_remp():

            for node in self.nodes:
                self.liste_associee[node] = []
                for element in self.list_Ad[node]:
                    if element == node:
                        pass
                    elif element not in self.liste_associee[node]:
                        self.liste_associee[node].append(element)
                        for member in self.list_Ad[element]:
                            if member == node:
                                pass
                            elif member not in self.list_Ad[node]:
                                self.list_Ad[node].append(member)
                            else:
                                pass
                    else:
                        pass

            return self.liste_associee

        list_associee_remp()
        for node in self.nodes:
            if len(self.liste_associee[node]) == len(self.nodes) - 1:
                pass
            elif len(self.liste_associee[node]) != len(self.nodes) - 1:
                text="n'est pas connex"
                return text
            text="Connex"
            return text

    def is_eulerian(self):
        if self.True_associee():
            self.enodes = []
            for node in self.nodes:
                if len(self.list_Ad[node]) % 2:
                    self.enodes.append(node)
                else:
                    pass
            if len(self.enodes) >= len(node) - 2:
                text="Eulerien"
                return text
            else:
                text="n'est pas Eulerien"
                return text

    def Tracer_Graph(self):
        my_graph = nx.Graph()
        for Entry_element in self.Entries:
            if self.cout_exist:
                my_graph.add_edge(Entry_element[0][0], Entry_element[0][1], weight=Entry_element[1])
            else:
                my_graph.add_edge(Entry_element[0], Entry_element[1])
        pos = nx.circular_layout(my_graph)

        nx.draw(my_graph, pos=pos, with_labels=True, node_size=1500, node_color='#FAEBD7', edge_color='#6A67CE',
                font_color='#FFF')
        nx.draw_networkx_edge_labels(my_graph, pos, font_size=15, font_color='#A52A2A',
                                     edge_labels=nx.get_edge_attributes(my_graph, 'weight'))
        plot.show()

    def Tracer_DiGraph(self):
        # edge_list = [(Entry_element[0][0], Entry_element[0][1], {'weight': Entry_element[1]}) for Entry_element in self.Entries]
        my_graph = nx.DiGraph()
        for Entry_element in self.Entries:
            if self.cout_exist:
                my_graph.add_edge(Entry_element[0][0], Entry_element[0][1], weight=Entry_element[1])
            else:
                my_graph.add_edge(Entry_element[0], Entry_element[1])
        pos = nx.circular_layout(my_graph)

        nx.draw(my_graph, pos=pos, with_labels=True, node_size=1500, node_color='#7D1E6A', edge_color='#6A67CE',
                font_color='#FFF')
        nx.draw_networkx_edge_labels(my_graph, pos, font_size=15, font_color='#242F9B',
                                     edge_labels=nx.get_edge_attributes(my_graph, 'weight'))
        plot.show()
    def kruskal(self):
        kruskal_list = []
        
        initial_list = self.Entries
        initial_list.sort(key=lambda Entry_element: Entry_element[1])
        childhood_list = {}
        parent_list = []
     
        kruskal_edges = []
        for Entry_element in initial_list:
            kruskal_edges.append((Entry_element[0][0], Entry_element[1], Entry_element[0][1]))

        # filling kruskal list.
        def is_child(Entry_element):

            for char in parent_list:
                if Entry_element in childhood_list[char]:
                    return True
                else:
                    return False

        def is_parent(Entry_element):
            for char in parent_list:
                if Entry_element != char:
                    pass
                else:
                    return True
            return False

        def get_parent(Entry_element):
            for char in parent_list:
                if Entry_element in childhood_list[char]:
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
        self.create_nodes()
        prime_final_list = []
        prim_book = {}
        for node in self.nodes:
            prim_book[node] = []
            for Entry_element in self.Entries:
                if Entry_element[0][0] != node and Entry_element[0][1] != node:
                    pass
                else:
                    prim_book[node].append(Entry_element)

        for node in self.nodes:
            prim_book[node].sort(key=lambda Entry_element: Entry_element[1])

        if start not in self.nodes:
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

        self.create_nodes()
        # ===================================Initialisation======================================
        if start not in self.nodes:
            return "Le Point de départ n'appartient pas a ce graphe. Verifiez vos données"
        for Entry_element in self.Entries:
            if int(Entry_element[1]) < 0:
                return "L'algorithme de Dijkstra ne peut pas être exécuté en raison de l'existence d'un bord négatif, " \
                       "choisissez Bellman-Ford à la place "
        checked_nodes = [start]
        non_checked_nodes = [node for node in self.nodes if node not in checked_nodes]
        current_source = checked_nodes[-1]
        distances_list = {}
        predecessors_list = {}
        for Entry_element in self.Entries:
            if current_source in Entry_element[0]:
                distances_list[Entry_element[0][1]] = Entry_element[1]
                predecessors_list[Entry_element[0][1]] = current_source
            else:
                for char in Entry_element[0]:
                    if char in distances_list:
                        pass
                    else:
                        distances_list[char] = 9999999999999999999999999999
                    if char in predecessors_list:
                        pass
                    else:
                        predecessors_list[char] = "N"
        # ================================= Algorithme Start ====================================
        while len(non_checked_nodes) != 0:

            # Get The Smallest Entry_element in the distances list.

            smallest_one_value = 99999999999999
            smallest_one_key = None
            for dis in distances_list:
                if int(distances_list[dis]) < int(smallest_one_value) and dis not in checked_nodes:
                    smallest_one_value = distances_list[dis]
                    smallest_one_key = dis
                else:
                    pass
            checked_nodes.append(smallest_one_key)
            non_checked_nodes.remove(smallest_one_key)
            # Get The none checked Neighbors of The Smallest One

            smallest_one_neighbors = []
            for element in self.Entries:
                if smallest_one_key == element[0][0] and element[0][1] not in checked_nodes:
                    smallest_one_neighbors.append((element[0][1], element[1]))
                elif smallest_one_key == element[0][1] and element[0][0] not in checked_nodes:
                    smallest_one_neighbors.append((element[0][0], element[1]))
                else:
                    pass

            # Calculate and Update The distances:

            for neighbor in smallest_one_neighbors:
                minimum = min(int(distances_list[neighbor[0]]),
                              int(distances_list[smallest_one_key]) + int(neighbor[1]))
                if int(minimum) < int(distances_list[neighbor[0]]):
                    distances_list[neighbor[0]] = int(minimum)
                    predecessors_list[neighbor[0]] = smallest_one_key
                else:
                    pass
            smallest_one_neighbors.clear()

        # dijkstra_table = {}
        # index = ['Distance', 'Predecesseur']
        # for Entry_element in distances_list:
        #     dijkstra_table[Entry_element] = [distances_list[Entry_element], predecessors_list[Entry_element]]
        # tabulate(dijkstra_table, headers='keys', tablefmt='fancy_grid', showindex=index)
        return f' Distances : {distances_list}, Predecesseurs: {predecessors_list}'

    # Bellman Ford's Algorithme

    def bellman_ford(self, start):
        # ===================================Initialisation======================================
        # Filling Edges List
        self.create_nodes()

        edges_list = []
        for Entry_element in self.Entries:
            source = Entry_element[0][0]
            destination = Entry_element[0][1]
            weight = Entry_element[1]
            edges_list.append((source, destination, weight))

        # Filling Distances List

        distances_list = {}
        for node in self.nodes:
            distances_list[node] = float('infinity') if node != start else 0
        # Filling Predecessors List
        bf_list = []
        predecessors_list = {}
        for node in self.nodes:
            predecessors_list[node] = 'N' if node != start else '-'
        # ================================= Algorithme Start ====================================
        # Bellman-Ford Algorithme Running
        for i in range(len(self.nodes)):
            for edge in edges_list:
                if distances_list[edge[1]] > distances_list[edge[0]] + int(edge[2]):
                    distances_list[edge[1]] = distances_list[edge[0]] + int(edge[2])
                    predecessors_list[edge[1]] = edge[0]

        # bellman_ford_table = {}
        # index = ['Distance', 'Predecessor']
        # for Entry_element in distances_list:
        #     bellman_ford_table[Entry_element] = [distances_list[Entry_element], predecessors_list[Entry_element]]
        # tabulate(bellman_ford_table, headers='keys', tablefmt='fancy_grid', showindex=index)
        return f' Distances : {distances_list}, Predecesseurs: {predecessors_list}'


   