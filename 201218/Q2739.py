'''첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
출력예제
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
'''
a = input()
a = int(a)
for i in range(1, 10):
    print ("{0} * {1} = {2}".format(a, i, a*i))