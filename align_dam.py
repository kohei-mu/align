#/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def levenshtein_distance(a,b):
	m = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
	for i in xrange(len(a) + 1):
		m[i][0] = i
	for j in xrange(len(b) + 1):
		m[0][j] = j
	for i in xrange(1, len(a) + 1):
		for j in xrange(1, len(b) + 1):
			if a[i-1] == b[j-1]:
				x = 0
			else:
				x = 1
			m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + x)
			
			#if i > 1 and j >1 and (a[i-1] == b[j-2]) and (a[i-2] == b[j-1]):
			#	m[i][j] = min(m[i][j], m[i-2][j-2]+x)

	return m

def output(a,b):
	str1 = []
	str2 = []
	a = re.split(r'\s', a)
	b = re.split(r'\s', b)
	i = len(a)
	j = len(b)
	count_null=[]
	dp = levenshtein_distance(a,b)
	if i == j:
		count = max(i,j)
		for m in xrange(1, max(i,j)+8):
			#dp = levenshtein_distance(a,b)
			num = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
			if (i == 0) and (j == 0):break
			if num == dp[i-1][j-1]:
				str1.append(a[i-1]+" "+"({ "+str(count)+" })")
				str2.append(b[j-1])
				count -= 1
				i -= 1
				j -= 1
			elif num == dp[i][j-1]:
				str2.append(b[j-1])
				j -= 1
			elif num == dp[i-1][j]:
				str1.append(a[i-1]+" "+"({ "+str(count)+" })")
				count -= 1
				i -= 1

		if len(str2) < len(b):
			str1=[]
			str2=[]
			i=len(a)
			j=len(b)
			count = max(i,j)
			for m in xrange(1, max(i,j)+8):
				#dp=levenshtein_distance(a,b)
				num=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
				if num == dp[i-1][j-1]:
					if (i == 0) and (j == 0):break
					if count > 0:
						str1.append(a[i-1]+" "+"({ "+str(count)+" })")
						count -= 1
					str2.append(b[j-1])
					i -= 1
					j -= 1
				elif num == dp[i][j-1]:
					if j==0:break
					if count > 0:
						count_null.append(str(count))
						count -= 1
					str2.append(b[j-1])
					j -=1 
				elif num == dp[i-1][j]:
					if i != 0:
						if count == count:
							str1.append(a[i-1]+" "+"({ })")
						else:
							str1.append(a[i-1]+" "+"({ "+str(count)+" })")
							count -=1
						i -= 1
					elif i == 0:
						continue

		count_null = " ".join(count_null[::-1])+" "
		if len(count_null) > 1 :
			str1.append("NULL ({ "+str(count_null)+"})")
		else:
			str1.append("NULL ({ })")

	elif i < j:
		count = max(i,j)
		count_null=[]
		for m in xrange(1, max(i,j)+8):
			#dp = levenshtein_distance(a,b)
			num = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
			if num == dp[i-1][j-1]:
				if (i == 0) or (j == 0):break
				try:
					if i != 0:
						str1.append(a[i-1]+" "+"({ "+str(count)+" })")
						str2.append(b[j-1])
						count -= 1
						i -= 1
						j -= 1
					elif i ==0:
						print "err",a
						str2.append(b[j-1])
						j -= 1
				except:
					print "err"
			elif num == dp[i][j-1]:
				if j==0:break
				if count > 0:count_null.append(str(count))
				count -= 1
				if j >0:str2.append(b[j-1])
				j -= 1
			elif num == dp[i-1][j]:
				if i != 0:
					if count == count:
						str1.append(a[i-1]+" "+"({ })")
					else:
						str1.append(a[i-1]+" "+"({ "+str(count)+" })")
						count -=1
					i -= 1
				elif i == 0:
					if count > 0:count_null.append(str(count))
					count -=1
					if j > 0:str2.append(b[j-1])
					j-=1

		if len(str2) < len(b):
			str1=[]
			str2=[]
			i = len(a)
			j = len(b)
			count = max(i,j)
			count_null=[]
			for m in xrange(1, max(i,j)+8):
				#dp = levenshtein_distance(a,b)
				num = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
				if j==0:break
				if num == dp[i-1][j-1]:
					try:
						if i != 0:
							str1.append(a[i-1]+" "+"({ "+str(count)+" })")
							str2.append(b[j-1])
							count -= 1
							i -= 1
							j -= 1
						elif i ==0:
						    str2.append(b[j-1])
						    j -= 1
					except:
						print "err"
				elif num == dp[i][j-1]:
					if count > 0:count_null.append(str(count))
					count -= 1
					str2.append(b[j-1])
					j -= 1
				elif num == dp[i-1][j]:
					if i != 0:
						if count == count:
							str1.append(a[i-1]+" "+"({ })")
						else:
							str1.append(a[i-1]+" "+"({ "+str(count)+" })")
							count -=1
						i -= 1
					elif i == 0:
						continue

		count_null = " ".join(count_null[::-1])+" "
		if len(count_null) > 1 :
			str1.append("NULL ({ "+str(count_null)+"})")
		else:
			str1.append("NULL ({ })")


	elif i > j:
		count = min(i,j)
		count_null = []
		for m in xrange(1,max(i,j)+8):
			#dp = levenshtein_distance(a,b)
			num = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
			if i== 0:break
			if num == dp[i-1][j-1]:
				try:
					if j != 0:
						str1.append(a[i-1]+" "+"({ "+str(count)+" })")
						str2.append(b[j-1])
						count -= 1
						i -= 1
						j -= 1
					elif j == 0:
						str1.append(a[i-1]+" "+"({ })")
						i -= 1
				except:
					print "err"
			elif num == dp[i][j-1]:
				if j != 0:
					if count > 0:count_null.append(str(count))
					count -= 1
					str2.append(b[j-1])
					j -= 1
				elif j == 0:
					if count != count:
						str1.append(a[i-1]+" "+"({ "+str(count)+" })")
					else:
						str1.append(a[i-1]+" "+"({ })")
					i-=1
			elif num == dp[i-1][j]:
				str1.append(a[i-1]+" "+"({ })")
				i -= 1



		if len(str2) < len(b):
			str1=[]
			str2=[]
			i = len(a)
			j = len(b)
			count = min(i,j)
			count_null = []
			for m in xrange(1,max(i,j)+8):
				#dp = levenshtein_distance(a,b)
				num = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
				if j== 0:break
				if num == dp[i-1][j-1]:
					try:
						if j != 0:
							str1.append(a[i-1]+" "+"({ "+str(count)+" })")
							str2.append(b[j-1])
							count -= 1
							i -= 1
							j -= 1
						elif j == 0:
							str1.append(a[i-1]+" "+"({ })")
							i -= 1
					except:
						print "err"
				elif num == dp[i][j-1]:
					if j != 0:
						if count > 0:count_null.append(str(count))
						count -= 1
						str2.append(b[j-1])
						j -= 1
					elif j == 0:
						if count > 0:count_null.append(str(count))
						count -= 1
				elif num == dp[i-1][j]:
					str1.append(a[i-1]+" "+"({ })")
					i -= 1

		count_null = " ".join(count_null[::-1])+" "
		if len(count_null) > 1 :
			str1.append("NULL ({ "+str(count_null)+"})")
		else:
			str1.append("NULL ({ })")

	str1.reverse()
	str2.reverse()
	return "#comment"+"\n"\
        +" ".join(str2)+"\n"\
        +" ".join(str1)+"\n"

def file_input(a,b,c):
	f = open(a, "r")
	j = open(b, "r")
	k = open(c,"w")
	m = f.readlines()
	n = j.readlines()
	for i in xrange(0, len(m)):
		m[i] = m[i].rstrip()
		n[i] = n[i].rstrip()
	   	k.write(output(m[i],n[i]))
	f.close()
	j.close()
	k.close()


file_input("correct.txt","learner.txt","output4.txt")
#file_input("learner.txt","correct.txt","output3.txt")
#file_input("corpus/train.incor","corpus/train.corr","alignment/corr-incor.align")
#file_input("corpus/train.corr","corpus/train.incor","alignment/incor-corr.align")
