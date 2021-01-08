# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
rooms = list(map(int, input().rstrip().split()))
roomSet = set(rooms)
print((sum(roomSet)*size-sum(rooms))//(size-1))