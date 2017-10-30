 while( current != g1):
        #loop begins
        n1 = {}
        #del openset[current]
        if current in openset:
            del openset[current]
        #add current to closedset
        closedset.append(current)
        #Calculate all fronitier nodes
        #calculate left frontier node
        #check for blockage
        blockage_found = 0
        left_flag = 0
        l1.sort(key=lambda tup: tup[1])
        for i in l1:
            if(i[0] == current[0] and i[1] < current[1]):
                left_node = (current[0],i[1]+1)
                blockage_found = 1
                #print("Blockage found")
        if(blockage_found == 0):
            left_node = (current[0],0)
        #print("left node is ",left_node)
        if(left_node == current):
            left_flag = 1
        for i in closedset:
            if(i[0] == current[0] and i[1] < current[1]):
                left_flag = 1
        if(left_flag == 0):
            n1[left_node] = 0
        if(left_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        #calculate right frontier node
        #check for blockage
        blockage_found = 0
        right_flag = 0
        l1.sort(key=lambda tup: tup[1], reverse= True)
        for i in l1:
            if(i[0] == current[0] and i[1] > current[1]):
                right_node = (current[0],i[1]-1)
                blockage_found = 1
        if(blockage_found == 0):
            right_node = (current[0],cnum-1)
        #print(right_node)
        if(right_node == current):
            right_flag = 1
        for i in closedset:
            if(i[0] == current[0] and i[0] > current[0]):
                right_flag = 1
        if(right_flag == 0):
            n1[right_node] = 0
        if(right_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        #calculate upper frontier node
        #check for blockage
        blockage_found = 0
        upper_flag = 0
        l1.sort(key=lambda tup: tup[0])
        for i in l1:
            if(i[1] == current[1] and i[0] < current[0]):
                upper_node = (i[0]+1,current[1])
                blockage_found = 1 
        if(blockage_found == 0):
            upper_node = (0,current[1])
        #print(upper_node)
        if(upper_node == current):
            upper_flag = 1
        for i in closedset:
            if(i[1] == current[1] and i[0] < current[0]):
                upper_flag = 1
        if(upper_flag == 0):
            n1[upper_node] = 0
        if(upper_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        #calculate lower frontier node
        #check for blockage
        blockage_found = 0
        lower_flag = 0
        l1.sort(key=lambda tup: tup[0], reverse = True)
        for i in l1:
            if(i[1] == current[1] and i[0] > current[0]):
                lower_node = (i[0]-1,current[1])
                blockage_found = 1 
        if(blockage_found == 0):
            lower_node = (rnum-1,current[1])      
        for i in closedset:
            if(i[1] == current[1] and i[0] > current[0]):
                lower_flag = 1
        if(lower_node == current):
            lower_flag = 1
        if(lower_flag == 0):
            n1[lower_node] = 0
        if(lower_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        delete = 0
        for i in n1:
            if i in closedset:
                #print("Do not consider",i)
                delete = i
                continue
            tent_gscore = gscore[current] + (abs(i[0] - current[0]) + abs(i[1] - current[1]))
            #print(tent_gscore)
            gscore[i] = tent_gscore
            n1[i] = gscore[i] + (abs(i[0] - g1[0]) + abs (i[1] - g1[1]))
            if i not in openset:
                openset[i] = gscore[i] + (abs(i[0] - g1[0]) + abs (i[1] - g1[1]))
                #print("openset is:",openset)
            elif(tent_gscore >= gscore[i]):
                continue
            camefrom[i] = current
            gscore[i] = tent_gscore
            fscore[i] = gscore[i] + (abs(i[0] - g1[0]) + abs(i[1] - g1[1])) 
        if delete in n1:
            del n1[delete]
        if not n1:
            current = min(openset, key=openset.get)
            path = []
        else:
            current = min(n1, key=n1.get) 
        path.append(current)
            
    return(path)