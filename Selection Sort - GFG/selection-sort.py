#User function Template for python3
class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
       
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            self.select(arr,i)
            for j in range(len(arr[:i]),len(arr)):
                if arr[i]>arr[j]:
                    b=arr[i]
                    arr[i]=arr[j]
                    arr[j]=b
        return arr

# } Driver Code Ends

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends