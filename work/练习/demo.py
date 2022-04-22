# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={:2}".format(j, i, i * j), end='\t')
#     # 此处的print()输出每执行完一轮后，打印计算结果到控制台
#     print()
# def func(n):
#     for i in range(n):
#         yield i ** 2
#
#
# for i in func(5):
#     print(i)

a = input()
print("  %s" % a)
print(" %s%s%s" % (a, a, a))
print("%s" % a * 5)
