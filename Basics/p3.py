for i in range(int(input())):
    n=int(input())
    list_of_numbers=[1]
    start=1
    for y in range(2,n+1):
        add=start+y+(start%1000000007*y%1000000007)
        start=add%1000000007
        list_of_numbers.append(start)
    print(list_of_numbers[len(list_of_numbers)-1]%1000000007)    