import networkx as nx
import matplotlib.pyplot as plt


def k_centers_objective_value(G, centers):
    obj_val = 0
    nodes = G.number_of_nodes()
    for i in range(0, nodes):# edw exw diale3ei ena node
        if i not in centers:
            temp = 1000000
            for j in range(0, len(centers)):#edw to sugrinw me ena kentro
                if nodes_connected(G, i, centers[j]):
                    if G[i][centers[j]]['weight'] < temp:
                        temp = G[i][centers[j]]['weight']#edw to temp exei parei thn mikroterh timh akmhs se kentro
            if temp>obj_val:
                obj_val = temp
    return obj_val


def nodes_connected(g, u, v):
    return u in g.neighbors(v)

def distFromC(graph,centers):
    obj_val = 0
    nodes = graph.number_of_nodes()
    for i in range(0, nodes):  # edw exw diale3ei ena node
        if i not in centers:
            temp = 1000000
            for j in range(0, len(centers)):  # edw to sugrinw me ena kentro
                if nodes_connected(graph, i, centers[j]):
                    if graph[i][centers[j]]['weight'] < temp:
                        temp = graph[i][centers[j]]['weight']  # edw to temp exei parei thn mikroterh timh akmhs se kentro
            if temp > obj_val:
                obj_val = temp
                solution=i
    return solution

def Greedy(G,k,first_center):
    center_solution = []
    nodes=G.number_of_nodes()
    center_solution.append(first_center)
    #first_center=center_solution[0]
    for i in range(1,k):#gia kathe kentro
        temp = distFromC(G,center_solution)
        center_solution.append(temp)
    obj_val=k_centers_objective_value(G,center_solution)
    return center_solution,obj_val


def Greedy2(G,k):
    first_center=0
    nodes=G.number_of_nodes()
    center_solution = []
    templist=[]
    for j in range(0,nodes):
        templist=[]
        first_center = j
        templist.append(first_center)
        for i in range(1,k):#gia kathe kentro
            temp = distFromC(G,templist)
            templist.append(temp)
        center_solution.append(templist)
    obj_list=[0]*k
    obj_val=1000000
    for i in range(0,len(center_solution)):
        tempval = k_centers_objective_value(G, center_solution[i])
        if (tempval<obj_val):
            obj_val=tempval
            obj_list=center_solution[i]

    return obj_list,obj_val

def k_center_greedy_based(G, k):
    first_center = 0
    nodes = G.number_of_nodes()
    obj_list = [0] * k
    obj_val = 1000000
    for j in range(0, nodes):
        templist = []
        first_center = j
        templist.append(first_center)
        for i in range(1, k):  # gia kathe kentro
            temp = distFromC(G, templist)
            templist.append(temp)

        tempval = k_centers_objective_value(G, templist)
        if (tempval < obj_val):
            obj_val = tempval
            obj_list = templist.copy()

    return  obj_val,obj_list

def Greedy4(G, k):
    first_center = 0
    nodes = G.number_of_nodes()
    obj_list = [0] * k
    obj_val = 1000000
    for j in range(0, nodes):
            print(j)
            templist = []
            first_center = j
            templist.append(first_center)
            for i in range(1, k):  # gia kathe kentro
                temp = distFromC(G, templist)
                templist.append(temp)

            tempval = k_centers_objective_value(G, templist)
            if (tempval < obj_val):
                obj_val = tempval
                obj_list = templist.copy()

    templist = obj_list.copy()
    obj_val=k_centers_objective_value(G, obj_list)
    for f in range(0,nodes):

                    print(f)
                    templist[k-1]=f
                    tempval = k_centers_objective_value(G, templist)
                    if(tempval<obj_val):
                        obj_val = tempval
                        obj_list = templist.copy()
                        print(obj_list)
                        print(obj_val)
    return obj_list, obj_val


