def insertion_sort(data):
  n=len(data)
  for i in range(1,n):
    key=data[i]
    j=i-1
    while j>=0 and key<data[j]:
      data[j+1]=data[j]
      j-=1
    data[j+1]=key
  return data


data=list(map(int,input().split()))
print(insertion_sort(data))