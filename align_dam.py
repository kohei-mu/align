#/usr/bin/env python
# -*- coding: utf-8 -*-

import re, argparse

parser = argparse.ArgumentParser(description="help messages") 
parser.add_argument("-correct", dest="corr", help="correct sentence")
parser.add_argument("-incorrect", dest="incor", help="incorrect sentence")
parser.add_argument("-alignOut", dest="align", help="output alignment")
args = parser.parse_args()

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

	return m

def alignment(correct, incorrect):
    correct_al = []
    incorrect_al = []
    correct = re.split(r'\s', correct)
    incorrect = re.split(r'\s', incorrect)
    correct_len = len(correct)
    incorrect_len = len(incorrect)
    count_null = []
    dp = levenshtein_distance(correct, incorrect)
    if correct_len == incorrect_len:
        count = max(correct_len, incorrect_len)
        for m in xrange(1, max(correct_len, incorrect_len)+8):
            num = min(dp[correct_len-1][incorrect_len], dp[correct_len][incorrect_len-1], dp[correct_len-1][incorrect_len-1])
            if correct_len == 0 and incorrect_len == 0:break
            if num == dp[correct_len-1][incorrect_len-1]:
                correct_al.append(correct[correct_len-1] +" " + "({ " + str(count) + " })")
                incorrect_al.append(incorrect[incorrect_len-1])
                count -= 1
                correct_len -= 1
                incorrect_len -= 1
            elif num == dp[correct_len][incorrect_len-1]:
                incorrect_al.append(incorrect[incorrect_len-1])
                incorrect_len -= 1
            elif num == dp[correct_len-1][incorrect_len]:
                correct_al.append(correct[correct_len-1] + " " + "({ " + str(count) + " })")
                count -= 1
                correct_len -= 1
        count_null = " ".join(count_null[::-1]) + " "
        if len(count_null) > 1:
            correct_al.append("NULL ({ " + str(count_null) + "})")
        else:
            correct_al.append("NULL ({ })")

    elif correct_len < incorrect_len:
        count = max(correct_len, incorrect_len)
        for m in xrange(1, max(correct_len, incorrect_len) + 8):
            num = min(dp[correct_len-1][incorrect_len], dp[correct_len][incorrect_len-1], dp[correct_len-1][incorrect_len-1])
            if num == dp[correct_len-1][incorrect_len-1]:
                if correct_len == 0 or incorrect_len == 0: break
                try:
                    if correct_len != 0:
                        correct_al.append(correct[correct_len-1] + " " + "({ " + str(count) + " })")
                        incorrect_al.append(incorrect[incorrect_len-1])
                        count -= 1
                        correct_len -= 1
                        incorrect_len -= 1
                    elif correct_len == 0:
                        incorrect_al.append(incorrect[incorrect_len-1])
                        incorrect_len -= 1
                except:
                    pass
            elif num == dp[correct_len][incorrect_len-1]:
                if incorrect_len == 0:break
                if count > 0:count_null.append(str(count))
                count -= 1
                if incorrect_len > 0:incorrect_al.append(incorrect[incorrect_len-1])
                incorrect_len -= 1
            elif num == dp[correct_len-1][incorrect_len]:
                if correct_len != 0:
                    try:
                        correct_al.append(correct[correct_len-1] + " " + "({ })")
                    except:
                        correct_al.append(correct[correct_len-1] + " " + "({ " + str(count) + " })")
                        count -= 1
                    correct_len -= 1
                elif correct_len == 0:
                    if count > 0:count_null.append(str(count))
                    count -= 1
                    if incorrect_len > 0:incorrect_al.append(incorrect[incorrect_len-1])
                    incorrect_len -= 1
	
        count_null = " ".join(count_null[::-1])+" "
        if len(count_null) > 1 :
            correct_al.append("NULL ({ " + str(count_null) + "})")
        else:
            correct_al.append("NULL ({ })")

    elif correct_len > incorrect_len:
        count = min(correct_len, incorrect_len)
        for m in xrange(1,max(correct_len, incorrect_len) + 8):
            num = min(dp[correct_len-1][incorrect_len],dp[correct_len][incorrect_len-1],dp[correct_len-1][incorrect_len-1])
            if correct_len == 0:break
            if num == dp[correct_len-1][incorrect_len-1]:
                try:
                    if incorrect_len != 0:
                        correct_al.append(correct[correct_len-1]+ " " + "({ " + str(count) + " })")
                        incorrect_al.append(incorrect[incorrect_len-1])
                        count -= 1
                        correct_len -= 1
                        incorrect_len -= 1
                    elif incorrect_len == 0:
                        correct_al.append(correct[correct_len-1] + " " + "({ })")
                        correct_len -= 1
                except:
                    pass
            elif num == dp[correct_len][incorrect_len-1]:
                if incorrect_len != 0:
                    if count > 0:count_null.append(str(count))
                    count -= 1
                    incorrect_len.append(incorrect_al[incorrect_len-1])
                    incorrect_len -= 1
                elif incorrect_len == 0:
                    try:
                        correct_al.append(correct[correct_len-1] + " " + "({ " + str(count) + " })")
                    except:
                        correct_al.append(correct[correct_len-1] + " " + "({ })")
                    correct_len -= 1
            elif num == dp[correct_len-1][incorrect_len]:
                correct_al.append(correct[correct_al-1] + " " + "({ })")
                correct_len -= 1

        count_null = " ".join(count_null[::-1])+" "
        if len(count_null) > 1 :
            correct_al.append("NULL ({ " + str(count_null) + "})")
        else:
            correct_al.append("NULL ({ })")

    correct_al.reverse()
    incorrect_al.reverse()
    return "#comment" + "\n" + " ".join(incorrect_al) + "\n" + " ".join(correct_al) + "\n"

def main(corr, incor, align):
    correct = open(corr, "r").readlines()
    incorrect = open(incor, "r").readlines()
    writeAlign = open(align,"w")
    for i in xrange(0, len(correct)):
        correct[i] = correct[i].rstrip()
        incorrect[i] = incorrect[i].rstrip()
        writeAlign.write(alignment(correct[i],incorrect[i]))
    correct.close()
    incorrect.close()
    writeAlign.close()


main(args.corr, args.incor, args.align)
