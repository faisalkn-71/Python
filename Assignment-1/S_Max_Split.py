def max_balanced_str(str):
    count_L = 0
    count_R = 0
    balanced_str = []
    current_str = ""
    
    for char in str:
        current_str += char
        if char == 'L':
            count_L += 1
        else:
            count_R += 1
        
        
        if count_L == count_R:
            balanced_str.append(current_str)
            current_str = ""  
            count_L = count_R = 0  
    
    
    print(len(balanced_str))  
    for balanced in balanced_str:
        print(balanced)  


str = input()  
max_balanced_str(str)
