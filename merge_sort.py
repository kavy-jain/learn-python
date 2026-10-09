def merge_sort(data):
  n=len(data)
  if n<=1:
    return data
  mid=n//2
  left=merge_sort(data[:mid])
  right=merge_sort(data[mid:])

  result=[]
  i,j=0,0

  while i<len(left) and j<len(right):

    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1

  result.extend(left[i:])    
  result.extend(right[j:])    

  return result

data=list(map(int,input().split()))
print(merge_sort(data))