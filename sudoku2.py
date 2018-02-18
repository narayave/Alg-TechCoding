def sudoku2(grid):

	size = len(grid)

	track = {} # hashes for row

	# Check rows for dups
	for i in grid:
		for j in i:
			if j == '.':
				continue
			if j in track:
				track[j] += 1
				if track[j] > 1:
					return False
			else:
				track[j] = 1
		track = track.fromkeys(track, 0)


	# Check cols for dups
	for i in xrange(size):
		for j in xrange(size):
			if grid[j][i] == '.':
				continue
			if grid[j][i] in track:
				track[grid[j][i]] += 1
				if track[grid[j][i]] > 1:
					return False
			else:
				track[grid[j][i]] = 1
		track = track.fromkeys(track, 0)


	# Check boxes for dups

	for over in range(3):
		for i in range(3):
			for j in range(3):
				if grid[j][i] == '.':
					continue
				if grid[j][i] in track:
					track[grid[j][i]] += 1
					if track[grid[j][i]] > 1:
						return False
				else:
					track[grid[i][j]] = 1
			track = track.fromkeys(track, 0)


			for j in range(3):
				if grid[j][i] == '.':
					continue
				if grid[j][i] in track:
					track[grid[j][i]] += 1
					if track[grid[j][i]] > 1:
						return False
				else:
					track[grid[i][j]] = 1
			track = track.fromkeys(track, 0)


			for j in range(3):
				if grid[j][i] == '.':
					continue
				if grid[j][i] in track:
					track[grid[j][i]] += 1
					if track[grid[j][i]] > 1:
						return False
				else:
					track[grid[i][j]] = 1
			track = track.fromkeys(track, 0)


	return True
