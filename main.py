import table



print()
print()
print("Welcome to Sudoku Solver by @AliAqa!!!")
print()
print()
print("In order to solve the sudoku game we need all the number that are available on the board.")
print("A sudoku board usually looks something like this:")
print("""  A B C D E F G H I
a 8 2 7 1 5 4 3 9 6
b 9 6 5 3 2 7 1 4 8
c 3 4 1 6 8 9 7 5 2
d 5 9 3 4 6 8 2 7 1
e 4 7 2 5 1 3 6 8 9
f 6 1 8 9 7 2 4 3 5
g 7 8 6 2 3 5 9 1 4
h 1 5 4 7 9 6 8 2 3
i 2 3 9 8 4 1 5 6 7""")
print()
print()
print("""Now we need all the numbers that are available on board with their indices;
uppercase letters A-H for columns at first and lowercase a-h for rows.
like below example:

Aa=8
Ab=9
Dc=6

which corresponds to above solved Sudoku.""")
print()
print("Print the values below. Once you completed, type done")


def USER_INPUT_IS_VALID(USR_INPUT):
	if len(USR_INPUT) != 4:
		return False
	VALID_COLUMN_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
	VALID_ROW_VALUES = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
	FIRST_LETTER_VALID = USR_INPUT[0] in VALID_COLUMN_VALUES
	SECOND_LETTER_VALID = USR_INPUT[1] in VALID_ROW_VALUES
	THIRD_LETTER_VALID = USR_INPUT[2] == "="
	if USR_INPUT[3].isdigit() :
		FOURTH_LETTER_VALID = int(USR_INPUT[3]) in range(1,10)
	else:
		FOURTH_LETTER_VALID = False 
	if FIRST_LETTER_VALID and SECOND_LETTER_VALID and THIRD_LETTER_VALID and FOURTH_LETTER_VALID:
		return True
	else:
		return False


USER_INPUT_NUMBERS = 0
while USER_INPUT_NUMBERS < 81:
	USER_INPUT = input()
	if USER_INPUT == "done":
		print(f"we got {USER_INPUT_NUMBERS} input/s from you.")
		break
	if USER_INPUT_IS_VALID(USER_INPUT) and len(USER_INPUT) == 4:
		print("Input accepted")
		index = USER_INPUT[:2]
		value = int(USER_INPUT[3])
		table.SUDOKU_TABLE[index] = [value]
		#print(table.SUDOKU_TABLE)
		USER_INPUT_NUMBERS += 1
		continue
	else:
		print("Input invalid")
		continue

def X_CALCULATION1():
	COLUMNS = "ABCDEFGHI"
	ROWS = "abcdefghi"
	for column in range(len(COLUMNS)):
		unique_value = 0
		for row in range(len(ROWS)):
			key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
			if len(key) == 1:
				unique_value = key[0]
				row = 0
				for row in range(len(ROWS)):
					key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
					if len(key) != 1 and unique_value in key:
						#print(f"removing {unique_value} from {COLUMNS[column]+ROWS[row]}")
						key.remove(unique_value)



def Y_CALCULATION1():
	COLUMNS = "ABCDEFGHI"
	ROWS = "abcdefghi"
	for row in range(len(ROWS)):
		unique_value = 0
		for column in range(len(COLUMNS)):
			key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
			if len(key) == 1:
				unique_value = key[0]
				column = 0
				for column in range(len(COLUMNS)):
					key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
					if len(key) != 1 and unique_value in key:
						#print(f"removing {unique_value} from {COLUMNS[column]+ROWS[row]}")
						key.remove(unique_value)


def Z_CALCULATION1():
	for z_axis1 in range(len(table.Z_LIST)):
		unique_value = 0
		list1 = table.Z_LIST[z_axis1]
		for z_axis2 in range(len(list1)):
			key = table.SUDOKU_TABLE[list1[z_axis2]]
			#print(list1[z_axis2])
			if len(key) == 1:
				unique_value = key[0]
				z_axis2 = 0
				for z_axis2 in range(len(list1)):
					key = table.SUDOKU_TABLE[list1[z_axis2]]
					if len(key) != 1 and unique_value in key:
						#print(f"removing {unique_value} from {list1[z_axis2]}")
						key.remove(unique_value)




def X_CALCULATION2():
	COLUMNS = "ABCDEFGHI"
	ROWS = "abcdefghi"
	for column in range(len(COLUMNS)):
		list1 = []
		for row in range(len(ROWS)):
			key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
			if len(key) != 1:
				#print(key)
				for value in key:
					#print(value)
					list1.append(value)
		#print(list1)

		for row in range(len(ROWS)):
			key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
			if len(key) != 1:
				for values in key:
					if list1.count(values) == 1:
						#print(values)
						key.clear()
						key.append(values)



def Y_CALCULATION2():
	COLUMNS = "ABCDEFGHI"
	ROWS = "abcdefghi"
	for column in range(len(ROWS)):
		list1 = []
		for row in range(len(COLUMNS)):
			key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
			if len(key) != 1:
				#print(key)
				for value in key:
					#print(value)
					list1.append(value)
		#print(list1)

		for row in range(len(COLUMNS)):
			key = table.SUDOKU_TABLE[COLUMNS[column]+ROWS[row]]
			if len(key) != 1:
				for values in key:
					if list1.count(values) == 1:
						#print(values)
						key.clear()
						key.append(values)



def Z_CALCULATION2():
	for z_axis1 in range(len(table.Z_LIST)):
		list1 = []
		list2 = table.Z_LIST[z_axis1]
		for z_axis2 in range(len(list2)):
			key = table.SUDOKU_TABLE[list2[z_axis2]]
			#print(list2[z_axis2])
			if len(key) != 1:
				#print(key)
				for value in key:
					#print(value)
					list1.append(value)

		#print(list1)

		for z_axis2 in range(len(list2)):
			key = table.SUDOKU_TABLE[list2[z_axis2]]
			if len(key) != 1:
				for values in key:
					if list1.count(values) == 1:
						#print(list2[z_axis2])
						#print(values)
						key.clear()
						key.append(values)
				






X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
X_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Y_CALCULATION2()
X_CALCULATION1()
Y_CALCULATION1()
Z_CALCULATION1()
Z_CALCULATION2()












for solutions in table.SUDOKU_TABLE.keys():
	print(solutions + " => " , table.SUDOKU_TABLE[solutions])