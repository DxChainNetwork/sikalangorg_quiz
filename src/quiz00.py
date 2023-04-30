#!/usr/bin/env python
""" 
挑战出处:
https://twitter.com/AllanGeBTCclub/status/1652192405255520261
挑战开始: https://sikalang.org/
挑战答案: https://sikalang.org/19073486328125.html
难度: 乘方 m.pow(day)
"""

dates = [
    [5, 19], # “5·19”币圈不眠夜！比特币狂跌30%
    [5, 20], # 
    [9, 15], # 9.15, 进一步防范和处置虚拟货币交易炒作风险的通知
]

for m, day in dates:
    result = m ** day
    url = 'https://sikalang.org/{}.html'.format(result)
    print(url)
 
# result
# https://sikalang.org/19073486328125.html Yes
# https://sikalang.org/95367431640625.html  No
# https://sikalang.org/205891132094649.html No
