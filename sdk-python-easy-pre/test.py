# s =[[1,2,3,4,5],[],[1,2,3]]
# for inedx, i in enumerate(s):
#     if i ==[]:
#         s.pop(inedx)
# print(s)\
# s ={}
# for key,value in s.items():
#     print(key)
# x = [1,2,1,1]
# i=0
# while i < len(x) - 1:
#     try:
#         Sk_Pmax = x.index(max(x),i)
#         i = Sk_Pmax+1
#         print(Sk_Pmax)
#     except:
#         break
# s =[1,2,3]
# d =[2,3,4]
# o = zip(s,d)
# p,l = zip(*o)
# p = list(p)
# l = list(l)
# l = [2,3,9]
# print(d)

#
s = [[1,1],[1,2],[13]]
s_mat = matrix(s)
print(s_mat.rowvec(1))