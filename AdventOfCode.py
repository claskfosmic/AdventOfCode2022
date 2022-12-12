#!/usr/bin/python3
#
# --- Advent Of Code 2022 ---
# 
# Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to
# deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that
# only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove
# where the fruit grows.
#
# To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by
# December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to
# grab any fruit you see along the way, just in case.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent
# calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star.
# Good luck!

import sys, os

#
def runAll(runExample=False):

	for d in range(1, 31):
		runDay(d, None, runExample)

#
def runDay(day, part=None, runExample=False):

	directory = "day{:02d}".format(day)

	if not os.path.exists("./"+directory):
		print("Day %d skipped, dir '%s' not found" % (day, directory))
		return

	if not os.path.exists("./"+directory+"/day.py"):
		print("Day %d skipped, file '%s/day.py' not found" % (day, directory))
		return

	module = "day{:02d}.day".format(day)

	try:
		moduleObj = __import__(module)
		submodule = getattr(moduleObj, "day")    # returns the module object "modules.update"
		puzzle = getattr(submodule, "puzzle")    # returns the module object "modules.update"

	except ImportError:
		return

	input_files = getInputFiles(directory, runExample)
	if len(input_files) == 0:
		print("Day %d skipped, no inputFile(s) found" % (day, directory))
		return

	dailyPuzzle = None

	if len(input_files) == 1:
		puzzle_input = getInput(input_files[0])

		if puzzle_input == "":
			print("Day %d skipped, input file '%s' was empty" % (day, input_files[0]))
			return

		dailyPuzzle = puzzle()
		dailyPuzzle.setInput(puzzle_input)
		dailyPuzzle.handleInput()

	if(part != None):
		print("- Day %d, Part %d : \"%s\"" % (day, part, getTitle(day)))
	else:
		print("- Day %d : \"%s\"" % (day, getTitle(day)))

	if part==None or part == 1:

		if dailyPuzzle != None:
			answer = dailyPuzzle.part1()
		else:
			dailyPuzzle_input_part1 = getInput(input_files[0])
			dailyPuzzle_part1 = puzzle()
			dailyPuzzle_part1.setInput(dailyPuzzle_input_part1)
			dailyPuzzle_part1.handleInput()
			answer = dailyPuzzle_part1.part1()

		if answer is not None and hasAnswer(day, 1, answer, runExample):
			if checkAnswer(day, 1, answer, runExample):
				if runExample:
					print("- Answer for day %d, part 1:\t\033[92m✓\033[00m %s " % (day, answer))
				else:
					print("- Answer for day %d, part 1:\t\033[93m*\033[00m %s " % (day, answer))
			else:
				print("- Answer for day %d, part 1:\t\033[91mx\033[00m %s" % (day, answer))
		else:
			print("- Answer for day %d, part 1:\t\033[95m?\033[00m %s" % (day, answer))

	if part==None or part == 2:

		if dailyPuzzle != None:
			answer = dailyPuzzle.part2()
		else:
			dailyPuzzle_input_part2 = getInput(input_files[1])
			dailyPuzzle_part2 = puzzle()
			dailyPuzzle_part2.setInput(dailyPuzzle_input_part2)
			dailyPuzzle_part2.handleInput()
			answer = dailyPuzzle_part2.part2()

		if answer is not None and hasAnswer(day, 2, answer, runExample):
			if(checkAnswer(day, 2, answer, runExample)):
				if runExample:
					print("- Answer for day %d, part 2:\t\033[92m✓\033[00m %s " % (day, answer))
				else:
					print("- Answer for day %d, part 2:\t\033[93m*\033[00m %s " % (day, answer))
			else:
				print("- Answer for day %d, part 2:\t\033[91mx\033[00m %s" % (day, answer))
		else:
			print("- Answer for day %d, part 2:\t\033[95m?\033[00m %s" % (day, answer))

	print("-----------------------------------------------------------------")		

#
def runPart(day, part, runExample=False):
	return runDay(day, part, runExample)

#
def getInputFiles(directory, runExample=False):
	
	input_files = [];

	if runExample == True:
		if os.path.exists("./"+directory+"/example-part1.txt") and os.path.exists("./"+directory+"/example-part2.txt"):
			input_files.append("./"+directory+"/example-part1.txt")
			input_files.append("./"+directory+"/example-part2.txt")
		elif os.path.exists("./"+directory+"/example.txt"):
			input_files.append("./"+directory+"/example.txt")

	else:
		if os.path.exists("./"+directory+"/input-part1.txt") and os.path.exists("./"+directory+"/input-part2.txt"):
			input_files.append("./"+directory+"/input-part1.txt")
			input_files.append("./"+directory+"/input-part2.txt")
		elif os.path.exists("./"+directory+"/input.txt"):
			input_files.append("./"+directory+"/input.txt")
			
	return input_files

#
def getInput(input_file):

	# Open text file in read mode and read puzzle input
	#
	file = open(input_file, "r")
	puzzle_input = file.read()
	file.close()

	return puzzle_input

#
def getTitle(day):
	titles = {
		1: "Calorie Counting",
		2: "Rock Paper Scissors",
		3: "Rucksack Reorganization",
		4: "Camp Cleanup",
		5: "Supply Stacks",
		6: "Tuning Trouble",
		7: "No Space Left On Device",
		8: "Treetop Tree House",
		9: "Rope Bridge",
		10: "Day 10: Cathode-Ray Tube",
		11: "Monkey in the Middle",
		12: "",
		13: "",
		14: "",
		15: "",
		16: "",
		17: "",
		18: "",
		19: "",
		20: "",
		21: "",
		22: "",
		23: "",
		24: "",
		25: ""
	}

	if day in titles:
		return titles[day]

	return ""

#
def getAnswer(day, part, runExample=False):

	exampleAnswers = {
		1: {1: 24000, 		2: 45000},
		2: {1: 15, 		2: 12},
		3: {1: 157, 		2: 70},
		4: {1: 2, 		2: 4},
		5: {1: "CMZ", 		2: "MCD"},
		6: {1: 7, 		2: 19},
		7: {1: 95437,		2: 24933642},
		8: {1: 21, 		2: 8},
		9: {1: 13, 		2: 36},
		10: {1: 13140, 		2: "\n##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######....."},
		11: {1: 10605,	 	2: 2713310158},
		12: {1: None, 		2: None},
		13: {1: None, 		2: None},
		14: {1: None, 		2: None},
		15: {1: None, 		2: None},
		16: {1: None, 		2: None},
		17: {1: None, 		2: None},
		18: {1: None, 		2: None},
		19: {1: None, 		2: None},
		20: {1: None, 		2: None},
		21: {1: None, 		2: None},
		22: {1: None, 		2: None},
		23: {1: None, 		2: None},
		24: {1: None, 		2: None},
		25: {1: None, 		2: None},
	}

	answers = {
		1: {1: 75501, 		2: 215594},
		2: {1: 14163, 		2: 12091},
		3: {1: 8105, 		2: 2363},
		4: {1: 588, 		2: 911},
		5: {1: "SVFDLGLWV", 	2: "DCVTCVPCL"},
		6: {1: 1140, 		2: 3495},
		7: {1: 1513699, 	2: 7991939},
		8: {1: 1672, 		2: 327180},
		9: {1: 6236, 		2: 2449},
		10: {1: 13720, 		2: "\n####.###..#..#.###..#..#.####..##..#..#.\n#....#..#.#..#.#..#.#..#....#.#..#.#..#.\n###..###..#..#.#..#.####...#..#....####.\n#....#..#.#..#.###..#..#..#...#....#..#.\n#....#..#.#..#.#.#..#..#.#....#..#.#..#.\n#....###...##..#..#.#..#.####..##..#..#."},
		11: {1: 316888,		2: 35270398814},
		12: {1: None, 		2: None	},
		13: {1: None, 		2: None},
		14: {1: None, 		2: None},
		15: {1: None, 		2: None},
		16: {1: None, 		2: None},
		17: {1: None, 		2: None},
		18: {1: None, 		2: None},
		19: {1: None, 		2: None},
		20: {1: None, 		2: None},
		21: {1: None, 		2: None},
		22: {1: None, 		2: None},
		23: {1: None, 		2: None},
		24: {1: None, 		2: None},
		25: {1: None, 		2: None},
	}

	if runExample == True:
		if day in exampleAnswers:
			if part in exampleAnswers[day]:
				return exampleAnswers[day][part]
	else:
		if day in answers:
			if part in answers[day]:
				return answers[day][part]

	return None

#
def hasAnswer(day, part, answer, runExample=False):
	return getAnswer(day, part, runExample) is not None

#
def checkAnswer(day, part, answer, runExample=False):

	goodAnswer = getAnswer(day, part, runExample)
	return answer == goodAnswer

#
if __name__ == "__main__":

	print("-----------------------------------------------------------------")
	print("                                                                 ")
	print("     _      _             _      ___   __    ___         _       ")
	print("    /_\  __| |_ _____ _ _| |_   / _ \ / _|  / __|___  __| |___   ")
	print("   / _ \/ _` \ V / -_) ' \  _| | (_) |  _| | (__/ _ \/ _` / -_)  ")
	print("  /_/ \_\__,_|\_/\___|_||_\__|  \___/|_|    \___\___/\__,_\___|  ")
	print("                                                                 ")
	print("		   ___       __      ___       ___     			")
	print("		 /'___`\   /'__`\  /'___`\   /'___`\   	      	 	")
	print("		/\_\ /\ \ /\ \/\ \/\_\ /\ \ /\_\ /\ \  	      		")
	print("		\/_/// /__\ \ \ \ \/_/// /__\/_/// /__ 	      		")
	print("		   // /_\ \\ \ \_\ \ // /_\ \  // /_\ \	      		")
	print("		  /\______/ \ \____//\______/ /\______/	      		")
	print("		  \/_____/   \/___/ \/_____/  \/_____/ 	      		")
	print("                                                                 ")
	print("-----------------------------------------------------------------")

	if len(sys.argv) == 1:
		runAll()
	
	elif len(sys.argv) == 2:
		if sys.argv[1] == "example":
			runAll(True)
		else:
			runDay(int(sys.argv[1]))

	elif len(sys.argv) == 3:
		if sys.argv[2] == "example":
			runDay(int(sys.argv[1]), None, True)
		else:
			runPart(int(sys.argv[1]), int(sys.argv[2]))

	elif len(sys.argv) == 4:
		if sys.argv[3] == "example":
			runPart(int(sys.argv[1]), int(sys.argv[2]), True)
