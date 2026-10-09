def quick_sort(data):
  if len(data)<=1:
    return data

  pivot=data[len(data)//2]
  left=[x for x in data if x>pivot]
  right=[x for x in data if x<pivot]
  mid=data[pivot]

  return quick_sort(left)+mid+quick_sort(right)

data=list(map(int,input().split()))
print(quick_sort(data))  

