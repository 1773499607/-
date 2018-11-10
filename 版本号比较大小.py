# 版本号比较大小
# import re

# def ver(v1,v2):
#    re1 = re.match("\d+(\.\w+){0,2}",v1)
#    re2 = re.match("\d+(\.\w+){0,2}",v2)

#    if re1 is None or re2 is None or re1.group() != v1 or re2.group() != v2:
#       return "版本号格式不对,可匹配3段 x.x.x"

#    l1 = v1.split(".")
#    l2 = v2.split(".")
#    v1_len = len(l1) 
#    v2_len = len(l2)

#    if v1_len > v2_len:
#       for i in range(v1_len - v2_len):
#          l2.append("0")
#          print("l2",l2)

#    elif v2_len > v1_len:
#       for i in range(v2_len - v1_len):
#          l1.append("0")
#          print("l1",l1)

#    for i in range(len(l1)):
#       if str(l1[i]) > str(l2[i]):
#          return 'v1大'
#       if str(l1[i]) < str(l2[i]):
#          return 'v2大'
#    return '相等'

# print(ver(v1='1.2.3a', v2='1.2.4b'))