def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    matching_item = {}
    for i, weight in enumerate(weights):
        try:
            # Check if the matching item exists in the hash table
            matching_index = matching_item[limit - weight]
        except KeyError:
            # If not, add the item to the table
            matching_item[weight] = i
        else:
            # If so, return the indices of the items
            return tuple([i, matching_index])

    return None
