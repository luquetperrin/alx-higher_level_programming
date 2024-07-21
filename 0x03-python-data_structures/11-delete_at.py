#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    
    new_list = []

    for i, item in enumerate(my_list):
        if i !=  idx:
            new_list.append(item)

    return new_list

