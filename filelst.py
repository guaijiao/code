def isLeapYear(year):
	if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
		return 1
	return 0

def getTimeLst(begin, end):
	res = []
	month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	bY = int(begin[0:4])
	eY = int(end[0:4])
	bM = int(begin[4:6])
	eM = int(end[4:6])
	bD = int(begin[6:8])
	eD = int(end[6:8])
	bH = int(begin[8:10])
	eH = int(end[8:10])

	for y in range(bY, eY + 1):
		tmpY = ""
		if y == bY:
			bbM = bM
		else:
			bbM = 1
		if y == eY:
			eeM = eM
		else:
			eeM = 12
		tmpY += str(y)
		for m in range(bbM, eeM + 1):
			tmpM = tmpY
			if m == bM and y == bY:
				bbD = bD
			else:
				bbD = 1
			if m == eM and y == eY:
				eeD = eD
			else:
				eeD = month[m - 1]
				if m == 2:
					eeD += isLeapYear(y)
			if m < 10:
				tmpM += "0"
			tmpM += str(m)
			for d in range(bbD, eeD + 1):
				tmpD = tmpM
				if d == bD and m == bM and y == bY:
					bbH = bH
				else:
					bbH = 0
				if d == eD and m == eM and y == eY:
					eeH = eH
				else:
					eeH = 23
				if d < 10:
					tmpD += "0"
				tmpD += str(d)
				for h in range(bbH, eeH + 1):
					tmpH = tmpD
					if h < 10:
						tmpH += "0"
					tmpH += str(h)
					res.append(tmpH)
	return res

def getRequestFileLst(begin, end):
	lst = getTimeLst(begin, end)
	for i in range(len(lst)):
		lst[i] += "1"
	return lst

def getResponseFileLst(begin, end):
	lst = getTimeLst(begin, end)
	for i in range(len(lst)):
		lst[i] += "2"
	return lst