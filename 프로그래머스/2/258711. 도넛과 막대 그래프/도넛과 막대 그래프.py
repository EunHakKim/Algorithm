def solution(edges):
    answer = [0, 0, 0, 0]
    graph = {}
    
    for v in edges:
        if v[0] in graph:
            graph[v[0]][0] += 1
        else:
            graph[v[0]] = [1, 0]
        
        if v[1] in graph:
            graph[v[1]][1] += 1
        else:
            graph[v[1]] = [0, 1]
    
    for key in graph.keys():
        if graph[key][0] == 0:
            answer[2] += 1
        elif graph[key][0] == 2:
            if graph[key][1] > 0:
                answer[3] += 1
            else:
                answer[0] = key
        elif graph[key][0] > 2:
            answer[0] = key
            
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]
    
    return answer