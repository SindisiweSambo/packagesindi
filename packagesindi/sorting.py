def bubble_sort(items):
    arr=[]
    for i in items:
        arr.append(i)
    return sorted(arr)
    '''Return array of items, sorted in ascending order'''

def merge_sort(items):

    new_len = len(items)
    if new_len == 1:
        return items

    mid_point = int(new_len / 2)
    item1 = merge_sort(items[:mid_point])
    item2 = merge_sort(items[mid_point:])
    new_list = []
    while len(item1) > 0 and len(item2) > 0:
        if item1[0] < item2[0]:
            new_list.append(item1[0])
            item1.pop(0)
        else:
            new_list.append(item2[0])
            item2.pop(0)

    if len(item1) == 0:
        new_list = new_list + item2
    if len(item2) == 0:
        new_list = new_list + item1

    return new_list
    '''Return array of items, sorted in ascending order'''


def quick_sort(items):
    for i in range(len(items)):  
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # if this item is bigger than next item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!
                
    return items
    '''Return array of items, sorted in ascending order'''
