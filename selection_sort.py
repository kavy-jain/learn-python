def selection_sort(data):
  n=len(data)
  for i in range(n-1):
    mini=i
    for j in range(i+1,n):
      if data[j]<data[mini]:
        data[i],data[data]=data[mini],data[i]
  return data

data=list(map(int,input().split()))
print(selection_sort(data))      
