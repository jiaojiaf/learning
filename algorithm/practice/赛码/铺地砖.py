# encoding=utf8
'''
http://exercise.acmcoder.com/online/online_judge_ques?ques_id=2318&konwledgeId=141
>题目描述									
	小赛最近承接了一个工程，为一块广场铺设地砖。待铺设的广场是矩形的，大小为N*M平米，业主要求铺设的地砖规格统一，大小为a*a平米。地砖可以超出待铺设的区域，但必须将指定的区域完全覆盖。铺设时，要求地砖边缘需与指定区域边缘平行，且必须用整块的地砖铺设，不允许将地砖破碎铺设。
	为节约成本，小赛需要知道铺设最少需要多少地砖。请你帮忙计算她最少需要采购的地砖数。
>输入
	输入的第一行为一个正整数T，表示有T组测试数据。随后的T行中，每行为一组测试数据。每组测试数据包含由3个正整数构成，分别为N、M和a，其中1<=N, M, a <=10^9。
>输出
	对每组测试数据，单独输出一行，为所需采购的地砖数。
>样例输入
	1
	6 6 4
>样例输出
	4
>时间限制
	C/C++语言：1000MS其它语言：3000MS	
>内存限制
	C/C++语言：65536KB其它语言：589824KB
'''
import math
T = int(raw_input())  
for i in xrange(0, T):
	m, n, a = map(float, raw_input().split())
	print(int(math.ceil(m/a) * math.ceil(n/a)))
