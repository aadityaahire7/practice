def nested_list_operations():
    list1 = [[1,2], [7,8], [3, 4], [5, 6], [7,8]]
    list2 = [[8,9], [6,7]]
    
    print("Length of list1:", len(list1))

    concatenated_list = list1 + list2
    print("Concatenated list:", concatenated_list)

    # Membership
    element_to_check = 4
    if element_to_check in list1:
        print(f"{element_to_check} is present in list1")
    else:
        print(f"{element_to_check} is not present in list1")

    # Iteration
    print("Iterating through list1:")
    for element in list1:
        if type(element)==list:
            for sub_element in element:
                print(sub_element)
        else:
            print(element)
    # Reverse Iteration
    print("Reverse Iterating through list1:")
    for element in reversed(list1):
        if type(element)==list:
            for sub_element in reversed(element):
                print(sub_element)
                
        else:
            print(element)

    # Indexing
    index_to_get = 2
    print(f"Element at index {index_to_get} in list1:", list1[index_to_get])

    # Slicing
    start_index = 2
    end_index = 5
    sliced_list = list1[start_index:end_index]
    print(f"Sliced list from index {start_index} to {end_index}:", sliced_list)

nested_list_operations()
