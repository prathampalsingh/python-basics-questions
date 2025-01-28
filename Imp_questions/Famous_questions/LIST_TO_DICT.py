def process_list(input_list):
    sum_of_numbers = 0
    error_items = []
    
    for item in input_list:
        if isinstance(item, int):  # Check if the item is an integer
            sum_of_numbers += item
        else:  # If it's not an integer, add it to error_items
            error_items.append(item)
    
    # Create the output dictionary
    input_list = {
        "sum": sum_of_numbers,
        "error": error_items
    }
    return input_list

# Example usage
input_list = [1, 8, 9, 22, 3, 9, "hello", 12 , "HI"]
print(process_list(input_list))


