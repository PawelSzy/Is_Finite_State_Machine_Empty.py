def nfsmaccepts(current, edges, accepting, visited): 
        def return_num_edge(edges, current):
            for edge in edges:
                if edge[0]==current:
                    return edge
            return False  
        
        def return_string(visited):
            pass
            
        # write your code here 
        current_edge = return_num_edge(edges, current)
        if current in accepting:
            visited.append(current)
            #return visited
            return ""
        elif current_edge in visited:
            return None
        else:
            if current in [edge[0] for edge in edges]:
                #return True
                #print current_edge
                if not current_edge in visited:
                    visited.append(current_edge)
                    #print "visited: ", visited
                for edge in edges[current_edge]:
                    #print "edge: ", edge
                    path_to_end = nfsmaccepts(edge, edges, accepting, visited)
                    #print "path to end: ",path_to_end
                    if path_to_end!=None:
                        if path_to_end == "":
                            return current_edge[1]
                        else:
                            return current_edge[1]+path_to_end
                        return path_to_end;
                return None
            else:
                return None