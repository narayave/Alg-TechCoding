def areFollowingPatterns(strings, patterns):

	track = {}
	track2 = {}

	for i in range(0, len(strings)):
		# print track
		if strings[i] in track:
			# print track[strings[i]], patterns[i]
			if track[strings[i]] != patterns[i]:
				return False
		else:
			track[strings[i]] = patterns[i]
		# print track
	# return True


	for i in range(0, len(strings)):
		if patterns[i] in track2:
			# if strings[i] not in track[patterns[i]]:
			#     track[patterns[i]].append(strings[i])
			if track2[patterns[i]] != strings[i]:
			# if len(track[patterns[i]]) > 1:
				return False
		else:
			track2[patterns[i]] = strings[i]

	return True