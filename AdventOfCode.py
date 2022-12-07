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

def runAll(runExample=False):

	for d in range(1, 31):
		runDay(d, None, runExample)

def runDay(day, part=None, runExample=False):

	directory = "day{:02d}".format(day)
	if not os.path.exists("./"+directory):
		print("Day %d skipped, dir '%s' not found" % (day, directory))
		return

	if not os.path.exists("./"+directory+"/day.py"):
		print("Day %d skipped, file '%s/day.py' not found" % (day, directory))
		return

	if runExample == True:
		if not os.path.exists("./"+directory+"/example.txt"):
			print("Day %d skipped, file '%s/example.txt' not found" % (day, directory))
			return
	else:
		if not os.path.exists("./"+directory+"/input.txt"):
			print("Day %d skipped, file '%s/input.txt' not found" % (day, directory))
			return

	module = "day{:02d}.day".format(day)

	try:
		moduleObj = __import__(module)
		submodule = getattr(moduleObj, 'day')    # returns the module object "modules.update"
		puzzle = getattr(submodule, 'puzzle')    # returns the module object "modules.update"

	except ImportError:
		return

	# Open text file in read mode and read puzzle input
	#
	if runExample == True:
		input_file = open("./"+directory+"/example.txt", "r")
	else:
		input_file = open("./"+directory+"/input.txt", "r")

	puzzle_input = input_file.read()
	input_file.close()

	if puzzle_input == "":
		print("Day %d skipped, input from file was empty" % (day, directory))
		return

	if(part != None):
		print("- Day %d, Part %d : \"%s\"" % (day, part, getTitle(day)))
	else:
		print("- Day %d : \"%s\"" % (day, getTitle(day)))

	puzzle = puzzle()
	puzzle.setInput(puzzle_input)
	puzzle.handleInput()

	if part==None or part == 1:

		answer = puzzle.part1()
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
		
		answer = puzzle.part2()
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

def runPart(day, part, runExample=False):
	return runDay(day, part, runExample)

def getTitle(day):
	if day == 1: return "Calorie Counting"
	if day == 2: return "Rock Paper Scissors"
	if day == 3: return "Rucksack Reorganization"
	if day == 4: return "Camp Cleanup"
	if day == 5: return "Supply Stacks"
	if day == 6: return "Tuning Trouble"
	if day == 7: return "No Space Left On Device"
	return ""

def getAnswer(day, part, runExample=False):

	exampleAnswers = {
		1: {1: 24000, 	2: 45000},
		2: {1: 15, 	2: 12},
		3: {1: 157, 	2: 70},
		4: {1: 2, 	2: 4},
		5: {1: 'CMZ', 	2: 'MCD'},
		6: {1: 7, 	2: 19},
		#7: {1: 95437,	2: 24933642}
	}

	answers = {
		1: {1: 75501, 		2: 215594},
		2: {1: 14163, 		2: 12091},
		3: {1: 8105, 		2: 2363},
		4: {1: 588, 		2: 911},
		5: {1: 'SVFDLGLWV', 	2: 'DCVTCVPCL'},
		6: {1: 1140, 		2: 3495},
		7: {1: 1513699, 	2: 7991939}
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

def hasAnswer(day, part, answer, runExample=False):
	return getAnswer(day, part, runExample) is not None

def checkAnswer(day, part, answer, runExample=False):

	goodAnswer = getAnswer(day, part, runExample)
	return answer == goodAnswer

if __name__ == "__main__":

	print("-----------------------------------------------------------------")
	print("                                                                 ")
	print("      _      _             _      ___   __    ___         _      ")
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
