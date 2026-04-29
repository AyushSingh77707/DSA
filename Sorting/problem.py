'''BUBBLE SORT'''
def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

nums=[2,5,3,1,10]
print(bubble_sort(nums))

'''INSERTION SORT'''
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertion_sort(nums))

'''SELECTION SORT'''
def selection_Sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

print(selection_Sort(nums))

'''MERGE SORT'''
def merge(arr,l,mid,r):
    a=[]
    b=[]
    for i in range(l,mid+1):
        a.append(arr[i])
    for i in range(mid+1,r+1):
        b.append(arr[i])
    i,j,k=0,0,l
    while k<=r:
        if j==len(b):
            arr[k]=a[i]
            i+=1
            k+=1
        elif i==len(a):
            arr[k]=b[j]
            j+=1
            k+=1
        elif a[i]<b[j]:
            arr[k]=a[i]
            i+=1
            k+=1
        else:
            arr[k]=b[j]
            j+=1
            k+=1
def mergesort(arr,l,r):
    if l>=r:
        return
    mid=(l+r)//2
    mergesort(arr,l,mid)
    mergesort(arr,mid+1,r)
    merge(arr,l,mid,r)

def Mergesortarray(arr):
    mergesort(arr,0,len(arr)-1)
    return arr

print(Mergesortarray(nums))

'''QUICK SORT'''
def pivot(arr,l,r):
    key=arr[r]
    start=l
    for i in range(l,r+1):
        if arr[i]<=key:
            arr[i],arr[start]=arr[start],arr[i]
            start+=1
    return start-1

def quick_sort(arr,l,r):
    if l>=r:
        return
    p=pivot(arr,l,r)
    quick_sort(arr,l,p-1)
    quick_sort(arr,p+1,r)

def quicksortarray(arr):
    quick_sort(arr,0,len(arr)-1)
    return arr

print(quicksortarray(nums))

