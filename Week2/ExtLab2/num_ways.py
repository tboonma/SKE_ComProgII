def num_ways_with_1_2_to_get(n):
    if n < 2:
        return 1
    return num_ways_with_1_2_to_get_helper(n - 1, [n]) + num_ways_with_1_2_to_get_helper(n - 2, [n])

def num_ways_with_1_2_to_get_helper(n, s):
    s.append(n)
    if n < 2:
        for i in range(1,len(s)):
            if i > 1:
                print(" + ", end="")
            print(s[i-1]-s[i], end="")
        if s[len(s)-1] == 1:
            print(" + 1", end="")
        print()
        s.pop(len(s)-1)
        return 1
    ans = num_ways_with_1_2_to_get_helper(n - 1, s) + num_ways_with_1_2_to_get_helper(n - 2, s)
    s.pop(len(s)-1)
    return ans

#print(num_ways_with_1_2_to_get(3))
# print(num_ways_with_1_2_to_get(4))
# print(num_ways_with_1_2_to_get(5))

def num_ways_with_1_2_3_to_get(n):
    if n < 2:
        return 1
    return num_ways_with_1_2_3_to_get_helper(n - 1, [n]) + num_ways_with_1_2_3_to_get_helper(n - 2, [n]) + num_ways_with_1_2_3_to_get_helper(n - 3, [n])

def num_ways_with_1_2_3_to_get_helper(n, s):
    if n < 0:
        return 0
    s.append(n)
    if n < 2:
        for i in range(1,len(s)):
            if i > 1:
                print(" + ", end="")
            print(s[i-1]-s[i], end="")
        if s[len(s)-1] == 1:
            print(" + 1", end="")
        print()
        s.pop(len(s)-1)
        return 1
    ans = num_ways_with_1_2_3_to_get_helper(n - 1, s) + num_ways_with_1_2_3_to_get_helper(n - 2, s) + num_ways_with_1_2_3_to_get_helper(n - 3, s)
    s.pop(len(s)-1)
    return ans

# print(num_ways_with_1_2_3_to_get(3))
# print(num_ways_with_1_2_3_to_get(4))
# print(num_ways_with_1_2_3_to_get(5))