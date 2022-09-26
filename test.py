COLUMNS = ["ABC", "DEF", "GHI"]
ROWS = ["abc", "def", "ghi"]

#a = COLUMNS[0]
#print(a[0])
i = 0
for up_letter in range(4):
	if up_letter == 3:
		i += 1
		up_letter = 0
		continue
	else:
		SELECTED_UP_LIST = COLUMNS[i]
		print(SELECTED_UP_LIST[up_letter])

#	SELECTED_UP_LIST = COLUMNS[i]
#	print(SELECTED_UP_LIST[up_letter])
#	if up_letter == 
#	for down_letter in range(len(ROWS[0])):
		