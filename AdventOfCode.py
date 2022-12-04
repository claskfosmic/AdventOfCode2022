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

def runAll():

	for d in range(1, 31):
		runDay(d)

def runDay(day, part=None, runExample=False):

	if(part != None):
		print("- Run day %d - Part %d:" % (day, part))
	else:
		print("- Run day %d:" % (day))

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

	puzzle_input = input_file.read().strip()
	input_file.close()

	if puzzle_input == "":
		print("Day %d skipped, input from file was empty" % (day, directory))
		return

	puzzle = puzzle()
	puzzle.setInput(puzzle_input)
	puzzle.handleInput()

	if part==None or part == 1:
		# from day01.solve import day
		answer = puzzle.part1()
		print("- Answer for day %d - Part 1: %s" % (day, answer))

	if part==None or part == 2:
		answer = puzzle.part2()
		print("- Answer for day %d - Part 2: %s" % (day, answer))

	print("--------------------------------------")

def runPart(day, part, runExample=False):
	return runDay(day, part, runExample)

def checkAnswer(day, part, answer):

	answers = {
		1: {1: 75501, 2: 215594},
		2: {1: 14163, 2: 12091}
	}

	return None

if __name__ == "__main__":

	print("--- Advent Of Code 2022 ---")

	if len(sys.argv) == 1:
		runAll()
	
	elif len(sys.argv) == 2:
		runDay(int(sys.argv[1]))

	elif len(sys.argv) == 3:
		if sys.argv[2] == "example":
			runDay(int(sys.argv[1]), None, True)
		else:
			runPart(int(sys.argv[1]), int(sys.argv[2]))

	elif len(sys.argv) == 4:
		if sys.argv[3] == "example":
			runPart(int(sys.argv[1]), int(sys.argv[2]), True)
