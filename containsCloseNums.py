
# Codefights

def containsCloseNums(nums, k):

	track = {}

	for i in range(len(nums)):
		if nums[i] in track:
			track[nums[i]].append(i)

			x = 0
			y = len(track[nums[i]]) - 1
			arr = track[nums[i]]
			while x != y:
				diff = abs(arr[x] - arr[y])
				if diff <= k:
					return True
				else:
					# Figure out which pointer to move
					diff1 = abs(arr[x+1] - arr[y])
					diff2 = abs(arr[x] - arr[y-1])
					if diff1 <= diff2:
						x += 1
					else:
						y -= 1

		else:
			track[nums[i]] = [i]


	return False