
data = {
	"Apples": 1,
	"Grapes": 2,
	"Pineapples": 3,
	"Pears": 4
}

char = '█'

# horizontal
width = 20 # width of biggest value

# vertical
max_height = 20 # height of biggest value
padding = 5 # gap between each bar
bar_width =4 # width of each bar

max_val = data[max(data, key=data.get)]


def vertical(data):

	grid = []
	for y in range(max_height):
		row = []
		for x in range(len(data)):
			row.append(' ' * bar_width)
		grid.append(row)

	longest_name = 0

	for j, i in enumerate(data):
		percent_of_max = data[i] / max_val
		bar_height = int(max_height * percent_of_max)
		start = max_height - bar_height
		for p in range(max_height-1, start-1, -1):
			grid[p][j] = char * bar_width
		if len(i) > longest_name:
			longest_name = len(i)




	for row in grid:
		for col in row:
			print(col + (" " * padding), end="")
		print()

	items = [i[0] for i in data.items()]


	lbudge = (" " * int(bar_width/2))

	if bar_width & 1 == 0:
		rbudge = (" " * (int(bar_width/2)-1))
	else:
		rbudge = lbudge


	for i in range(longest_name):
		for item in items:
			if i >= len(item):
				print(lbudge + " " + rbudge + (" " * padding), end="")
			else:
				print(lbudge + item[i] + rbudge + (" " * padding), end="")
		# make text slant to the right
		#lbudge += " "
		print()


def horizontal(data):
	longest_name = 0
	for i in data:
		if len(i) > longest_name:
			longest_name = len(i)
	for i in data:
		percent_of_max = data[i] / max_val
		bar_length = int(width * percent_of_max)
		print(i.ljust(longest_name)+" |"+"\t", str(data[i]).rjust(len(str(max_val))), (char * bar_length))

horizontal(data)
print()
vertical(data)