
a = input("Enter a list of numbers: ")
i = list(map(int, a.split())) 


if i:
    max_value = max(i)      
    min_value = min(i)      
    count = len(i)          
    reversed_list = i[::-1]  
    total_sum = sum(i)       
    sorted_list = sorted(i)   

    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
    print(f"count of the list: {count}")
    print(f"Reversed list: {reversed_list}")
    print(f"Sum of the values: {total_sum}")
    print(f"Sorted list: {sorted_list}")
else:
    print("The list is empty.")
