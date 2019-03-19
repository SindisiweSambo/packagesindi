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
   quick_sortHelp(items,0,len(items)-1)
   
def quick_sortHelp(items,first,last):
   if first<last:

       splitpoint = partition(items,first,last)

       quick_sortHelp(items,first,splitpoint-1)
       quick_sortHelp(items,splitpoint+1,last)

def partition(items,first,last):
   pivotvalue = items[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and items[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while items[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = items[leftmark]
           items[leftmark] = items[rightmark]
           items[rightmark] = temp

   temp = items[first]
   items[first] = items[rightmark]
   items[rightmark] = temp
   return rightmark
   '''Return array of items, sorted in ascending order'''
