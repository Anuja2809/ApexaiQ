def min_magic_shows(N, A, B):
    # Combine arrival and departure times as pairs (A[i], B[i]) and sort by B[i]
    intervals = list(zip(A, B))
    intervals.sort(key=lambda x: x[1])
    
    # Count the number of shows required
    count = 0
    last_end_time = -1  # The time when the last show ended
    
    for start, end in intervals:
        if start > last_end_time:  # If current student's arrival time is after the last show ends
            count += 1
            last_end_time = end  # Set the end time of the current magic show
            
    return count

# Input reading and processing
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Number of students
    A = list(map(int, input().split()))  # Arrival times
    B = list(map(int, input().split()))  # Departure times
    
    # Find the minimum number of magic shows for each test case
    result = min_magic_shows(N, A, B)
    print(result)