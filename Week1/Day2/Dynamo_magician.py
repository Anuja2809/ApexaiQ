def min_trick_shows(T, test_cases):
    results = []
    
    for i in range(T):
        N = test_cases[i][0]
        A = test_cases[i][1]
        B = test_cases[i][2]
        
        
        # Combine start and end times into tuples and sort by start time
        intervals = sorted(zip(A, B), key=lambda x: x[0])
        
        # Use a min heap to track end times of active intervals
        from heapq import heappush, heappop
        min_heap = []
        min_shows = 0
        
        for start, end in intervals:
            # Remove intervals that have already ended
            while min_heap and min_heap[0] < start:
                heappop(min_heap)
            
            # Add current interval's end time
            heappush(min_heap, end)
            
            # If a new trick performance is needed
            if len(min_heap) == 1:
                min_shows += 1
        
        results.append(min_shows)
    
    return results


# Sample Input Processing
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    N = int(input())  # Number of students
    A = list(map(int, input().split()))  # Start times
    B = list(map(int, input().split()))  # End times
    test_cases.append((N, A, B))

# Get the result
output = min_trick_shows(T, test_cases)

# Print output for each test case
for res in output:
    print(res)
