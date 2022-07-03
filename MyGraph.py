## Graph represented as adjacency list using a dictionary
## keys are vertices
## values of the dictionary represent the list of adjacent vertices of the key node

class MyGraph:
    def __init__(self, g = {}):
        ''' Constructor - takes dictionary to fill the graph as input; default is empty dictionary '''
        self.graph = g    

    def print_graph(self):
        ''' Prints the content of the graph as adjacency list '''
        for v in self.graph.keys():
            print (v, " -> ", self.graph[v])

    ## get basic info
    def get_nodes(self):
        ''' Returns list of nodes in the graph '''
        # ....
        return list(self.graph.keys())
        
    def get_edges(self): 
        ''' Returns edges in the graph as a list of tuples (origin, destination) '''
        # ...
        edge = []
        for i in self.graph.keys():
            for j in self .graph[j]:
                edge.append((j,i))
        return edge
      
    def size(self):
        ''' Returns size of the graph : number of nodes, number of edges '''
        # ...
        return len( self.get_nodes()), len ( self.get_edges())
      
    ## add nodes and edges    
    def add_vertex(self, v):
        ''' Add a vertex to the graph; tests if vertex exists not adding if it does '''
        # ...
        if v not in self.graph.keys():
            self.graph[v] = []
        
    def add_edge(self, o, d):
        ''' Add edge to the graph; if vertices do not exist, they are added to the graph ''' 
        # ...
        if o not in self.graph.keys():
            self.add_vertex(o)
        if d not in self .graph.keys():
            self.add_vertex(d)
        if d not in self.graph[o]:
            self.graph[o].append(d)

    ## successors, predecessors, adjacent nodes
        
    def get_successors(self, v):
        return list(self.graph[v])     # needed to avoid list being overwritten of result of the function is used           
             
    def get_predecessors(self, v):
        res = []
        for k in self.graph.keys(): 
            if v in self.graph[k]: 
                res.append(k)
        return res
    
    def get_adjacents(self, v):
        suc = self.get_successors(v)
        pred = self.get_predecessors(v)
        res = pred
        for p in suc: 
            if p not in res: res.append(p)
        return res
        
    ## degrees    
    
    def out_degree(self, v):
        # ...
        return len( self.graph[v])
    def in_degree(self, v):
        # ...
        return len( self.get_predecessors(v))
    def degree(self, v):
        # ...
        return len( self.get_adjacents(v))
        
    def all_degrees(self, deg_type = "inout"):
        ''' Computes the degree (of a given type) for all nodes.
        deg_type can be "in", "out", or "inout" '''
        degs = {}
        for v in self.graph.keys():
            if deg_type == "out" or deg_type == "inout":
                degs[v] = len(self.graph[v])
            else: degs[v] = 0
        if deg_type == "in" or deg_type == "inout":
            for v in self.graph.keys():
                for d in self.graph[v]:
                    if deg_type == "in" or v not in self.graph[d]:
                        degs[d] = degs[d] + 1
        return degs
    
    def highest_degrees(self, all_deg= None, deg_type = "inout", top= 10):
        if all_deg is None: 
            all_deg = self.all_degrees(deg_type)
        ord_deg = sorted(list(all_deg.items()), key=lambda x : x[1], reverse = True)
        return list(map(lambda x:x[0], ord_deg[:top]))
        
    
    ## topological metrics over degrees

    def mean_degree(self, deg_type = "inout"):
        ''' average degree of all nodes: sum of all degrees divided by number of nodes'''
        #....
        degs = self.all_degrees(deg_type)
        return sum(degs.values()) / float ( len (degs))
        
        
    def prob_degree(self, deg_type = "inout"):
        # count the number of occurrences of each degree in the network and derive its frequencies
        # ...
        degs = self.all_degrees(deg_type)
        res = {}
        
        for k in degs.keys():
            if degs[k] in res.keys():
                res[degs[k]] += 1
            else:
                res[degs[k]] = 1
                
        for k in res.keys():
            res[k] /= float ( len (degs))
            
        return res

    
    def print_prob_degree(self, counts):

        for k,v in counts.items():
            print(str(k) + " " + str(v))
    
    ## BFS and DFS searches    
    
    def reachable_bfs(self, v):
        l = [v]   # list of nodes to be handled
        res = []  # list of nodes to return the result
        while len(l) > 0:
            node = l.pop(0)  # implements a queue: LILO
            if node != v: res.append(node)
            for elem in self.graph[node]:
                if elem not in res and elem not in l and elem != node:
                    l.append(elem)
        return res
        
    def reachable_dfs(self, v):
        l = [v]
        res = []
        while len(l) > 0:
            node = l.pop(0) # implements a stack: 
            if node != v: res.append(node)
            s = 0
            for elem in self.graph[node]:
                if elem not in res and elem not in l:
                    l.insert(s, elem)
                    s += 1
        return res 

    def reachable_bfs_with_distance(self, v):
        l = [(v,0)]   # list of nodes to be handled
        res = []  # list of nodes to return the result
        while len(l) > 0:
            tuple = l.pop(0)
            node = tuple[0]  # implements a queue: LILO
            dist = tuple[1]  
            if node != v: res.append((node,dist))
            for elem in self.graph[node]:
                if len([item for item in res if item[0] == elem]) == 0 and len([item for item in l if item[0] == elem]) == 0 and elem != node:
                    l.append((elem,dist+1))
        return res  
    
    def distance(self, s, d):
        if s == d: return 0
        l = [(s,0)]
        visited = [s]
        while len(l) > 0:
            node, dist = l.pop(0)
            for elem in self.graph[node]:
                if elem == d: return dist + 1
                elif elem not in visited: 
                    l.append((elem,dist+1))
                    visited.append(elem)
        return None
        
    def shortest_path(self, s, d):
        if s == d: return 0
        l = [(s,[])]
        visited = [s]
        while len(l) > 0:
            node, preds = l.pop(0)
            for elem in self.graph[node]:
                if elem == d: return preds+[node,elem]
                elif elem not in visited: 
                    l.append((elem,preds+[node]))
                    visited.append(elem)
        return None

                
    ## clustering
        
    def clustering_coef(self, v):
        adjs = self.get_adjacents(v)
        if len(adjs) <=1: return 0.0
        # calculate the number of links of the adjacent nodes 
        ligs = 0
        # compare pairwisely if nodes in this list are connected between them
        for i in adjs:
            for j in adjs:
                if i != j:
                    # check if i and j are connected to each other; if yes increment counter of links
                    if j in self.graph[i] or i in self.graph[j]:
                        ligs = ligs + 1
        return float(ligs)/(len(adjs)*(len(adjs)-1))
        
    def all_clustering_coefs(self):
        # go through all the nodes and calculate its cc
        # put those in a dictionary and return
        ccs = {}
        for k in self.graph.keys():
            ccs[k] = self.clustering_coef(k)
        return ccs

    def k_clustering_coefs(self, dic_cc, dic_dg):
        dic = {}
        dic_final = {}

        for k,v in dic_dg.items():
          if v not in dic:
            dic[v] = [k] 
          else:
            dic[v].append(k)
        
        for k,v in dic.items():
          count = len(v)
          sum = 0
          for value in v:
            sum += dic_cc[value]
          total = sum/count
          dic_final[k] = total

        return sorted(dic_final.items(), key=lambda x: x[0], reverse = False)
        
    def mean_clustering_coef(self):
        # get all the clustering coefficients
        # and return the mean of all ccs
        ccs = self.all_clustering_coefs()
        return sum(ccs.values()) / float ( len (ccs))

    def mean_path_length(self):
        mean_shortest_path = 0
        count = 0
        for node1 in self.get_nodes():
          for node2 in self.get_nodes():
            if node1 != node2:
              sp = self.shortest_path(node1,node2)
              if isinstance(sp, list):
                mean_shortest_path += len(sp) - 1
              count+=1
        return mean_shortest_path/count

    def stats(self):
        print("======================================================================")
        print("| Statistic                       | Feature                          |")
        print("======================================================================")
        print("| " + '{0: <32}'.format('Average Degree') +  "| "+'{0: <32}'.format(str(self.mean_degree()))+" |")
        print("======================================================================")
        print("| " + '{0: <32}'.format('Average Path Length') +  "| "+'{0: <32}'.format(str(self.mean_path_length()))+" |")
        print("======================================================================")
        print("| " + '{0: <32}'.format('Average Clustering Coeficient') +  "| "+'{0: <32}'.format(str(self.mean_clustering_coef()))+" |")
        print("======================================================================")
        print("| " + '{0: ^66}'.format('Degree Distribution') + " |")
        print("======================================================================")

        sorted_degrees = sorted(self.prob_degree().items(), key=lambda x: x[0], reverse = False)

        for tuplo in sorted_degrees:
          print("| " + '{0: <32}'.format('k = '+str(tuplo[0])) +  "| "+'{0: <32}'.format(str(tuplo[1]))+" |")
        print("======================================================================")

        print("| " + '{0: ^66}'.format('Clustering Coeficient') + " |")
        print("======================================================================")

        for tuplo in self.k_clustering_coefs(self.all_clustering_coefs(),self.all_degrees()):
          print("| " + '{0: <32}'.format('k = '+str(tuplo[0])) +  "| "+'{0: <32}'.format(str(tuplo[1]))+" |")
        print("======================================================================")

    def create_network_from_file(self, file, min_correlation):

            f = open(file, "r")
            content = f.read()
            content_list = content.split()
            f.close() 
            k = 1
            i = 3
            while i < len(content_list):

                self.add_vertex(content_list[i])
                #print(content_list[i])
                self.add_vertex(content_list[i+1])
                abs_corr = abs(float(content_list[i+2]))
                if abs_corr > min_correlation:
                    #print("Edge: " + content_list[i] + " " + content_list[i+1])
                    #print("edge corr: ",abs_corr," min_corr: ",min_correlation)
                    self.add_edge(content_list[i], content_list[i+1])
                i += 3


if __name__ == "__main__":
    gr = MyGraph()
    gr.add_vertex(1)
    gr.add_vertex(2)
    gr.add_vertex(3)
    gr.add_vertex(4)
    gr.add_edge(1,2)
    gr.add_edge(2,3)
    gr.add_edge(3,2)
    gr.add_edge(3,4)
    gr.add_edge(4,2)
    gr.print_graph()
    #print(gr.size())
    
    # print (gr.get_successors(2))
    # print (gr.get_predecessors(2))
    # print (gr.get_adjacents(2))
    # 
    # print (gr.in_degree(2))
    # print (gr.out_degree(2))
    # print (gr.degree(2))
    # 
    #print(gr.all_degrees("inout"))
    #print(gr.all_degrees("in"))
    #print(gr.all_degrees("out"))
    # 
    # gr2 = MyGraph({1:[2,3,4], 2:[5,6],3:[6,8],4:[8],5:[7],6:[],7:[],8:[]})
    # print(gr2.reachable_bfs(1))
    # print(gr2.reachable_dfs(1))
    # 
    # print(gr2.distance(1,7))
    # print(gr2.shortest_path(1,7))
    # print(gr2.distance(1,8))
    # print(gr2.shortest_path(1,8))
    # print(gr2.distance(6,1))
    # print(gr2.shortest_path(6,1))
    # 
    # print(gr2.reachable_with_dist(1))

    # print(gr.mean_degree())
    # print(gr.prob_degree())
    # print(gr.mean_distances())
    #print (gr.clustering_coef(1))
    #print (gr.clustering_coef(2)) 

    #2.1
    gr2 = MyGraph()

    gr2.create_network_from_file("m_lung_gexp.tab", 0.5)
    #gr2.print_graph()


    #2.2
    gr2.stats()


    #2.3 
    gr = MyGraph()
    gr.add_vertex('BRAF')
    gr.add_vertex('NF1')
    gr.add_vertex('NRAS')
    gr.add_vertex('ERBB3')
    gr.add_vertex('FLT3')
    gr.add_vertex('FBXW7')
    gr.add_vertex('TP53')
    gr.add_vertex('PTEN')
    gr.add_vertex('PIK3CA')
    gr.add_vertex('DNMT3A')
    gr.add_vertex('CTNNB1')
    gr.add_vertex('APC')
    gr.add_vertex('SF3B1')
    gr.add_vertex('SMAD4')
    gr.add_vertex('LPHN2')
    gr.add_vertex('NCOR1')

    gr.add_edge('BRAF','NRAS')
    gr.add_edge('NRAS','BRAF')
    gr.add_edge('NRAS','NF1')
    gr.add_edge('NF1','NRAS')
    gr.add_edge('ERBB3','NRAS')
    gr.add_edge('NRAS','ERBB3')
    gr.add_edge('FLT3','NRAS')
    gr.add_edge('NRAS','FLT3')
    gr.add_edge('PIK3CA','NRAS')
    gr.add_edge('NRAS','PIK3CA')
    gr.add_edge('ERBB3','PIK3CA')
    gr.add_edge('PIK3CA','ERBB3')
    gr.add_edge('FLT3','PIK3CA')
    gr.add_edge('PIK3CA','FLT3')
    gr.add_edge('PTEN','PIK3CA')
    gr.add_edge('PIK3CA','PTEN')
    gr.add_edge('CTNNB1','PIK3CA')
    gr.add_edge('PIK3CA','CTNNB1')
    gr.add_edge('TP53','PIK3CA')
    gr.add_edge('PIK3CA','TP53')
    gr.add_edge('TP53','PTEN')
    gr.add_edge('PTEN','TP53')
    gr.add_edge('CTNNB1','APC')
    gr.add_edge('APC','CTNNB1')
    gr.add_edge('CTNNB1','SMAD4')
    gr.add_edge('SMAD4','CTNNB1')
    gr.add_edge('NCOR1','SMAD4')
    gr.add_edge('SMAD4','NCOR1')

    print(gr.reachable_bfs_with_distance('TP53'))

    #2.4 
    ''' Tendo em conta os 3 tipos de networks que foram estudadas, a que mais se enquadra neste caso é a Scale-free network
    , visto que os valores de C(k) são independentes do grau do nó, o que significa que poderia ser uma Random network ou uma
    Scale-free network. Tendo em conta que nas Random networks o valor de P(k) descresce exponencialmente, e neste caso isso não acontece,
    podemos concluir que estamos perante uma rede Scale-free '''