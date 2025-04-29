# qustion 1

# nums = list(map(int, input().split()))
# target = int(input())
# n = len(nums)
# found = False
# for i in range(n-1):
#     if found==True:
#         break
#     for j in range(i+1,n):
#         if nums[i] + nums[j] == target:
#             print(i,j)
#             found=True

# qustion 2

# s = input()
# for _ in range(len(s)//2):
#     if '()' in s:
#         s=s.replace('()','')
#     elif '{}' in s:
#         s=s.replace('{}','')
#     elif '[]' in s:
#         s=s.replace('[]','')
#     elif '<>' in s:
#         s=s.replace('<>','')
# if len(s) == 0:
#     print(True)
# else:
#     print(False)

# qustion 3

s = input()
n = len(s)

for i in range(n//2):
    if s[i] != s[n-i-1]:
        print('False')
        break