#! /usr/bin/env python

"""
Merge two sorted arrays and put the result in array1.
"""


def sort_lists(list_1, list_2):
    # since list_1 and list_2 are each sorted, use lower_bound to
    # set the starting point in list_1 where we should begin trying
    # to insert the next item in list_2. We could always start with 
    # 0 (the first elelemnt in list_1) but that's not efficient.
    lower_bound = 0
    for item in list_2:
        merged = False
        for index in range(lower_bound, len(list_1)):
            if item < list_1[index]:
                list_1.insert(index, item)
                lower_bound = index
                merged = True
                break
        # If we never merged, then the item in list_2 is bigger than the
        # biggest element in list_1.
        if not merged:
            list_1.append(item)
    print(list_1)

def main():
    list_1 = [3, 5, 7, 11, 12]
    list_2 = [2, 4, 6, 8,  9, 10, 13]
    sort_lists(list_1, list_2)

if __name__ == '__main__':
    main()
