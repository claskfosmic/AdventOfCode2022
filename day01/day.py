#
# --- Day 1: Calorie Counting ---
#
# The jungle must be too overgrown and difficult to navigate in vehicles or
# access from the air; the Elves' expedition traditionally goes on foot. As
# your boats approach land, the Elves begin taking inventory of their
# supplies. One important consideration is food - in particular, the number
# of Calories each Elf is carrying (your puzzle input).
#
# The Elves take turns writing down the number of Calories contained by the
# various meals, snacks, rations, etc. that they've brought with them, one
# item per line. Each Elf separates their own inventory from the previous
# Elf's inventory (if any) by a blank line.
#
# For example, suppose the Elves finish writing their items' Calories and end
# up with the following list:
#
# 1000
# 2000
# 3000
#
# 4000
#
# 5000
# 6000
#
# 7000
# 8000
# 9000
#
# 10000
# This list represents the Calories of the food carried by five Elves:
#
#  - The first Elf is carrying food with 1000, 2000, and 3000 Calories, a
#    total of 6000 Calories.
#  - The second Elf is carrying one food item with 4000 Calories.
#  - The third Elf is carrying food with 5000 and 6000 Calories, a total of
#    11000 Calories.
#  - The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a
#    total of 24000 Calories.
#  - The fifth Elf is carrying one food item with 10000 Calories.
#
# In case the Elves get hungry and need extra snacks, they need to know which
# Elf to ask: they'd like to know how many Calories are being carried by the
# Elf carrying the most Calories. In the example above, this is 24000
# (carried by the fourth Elf).
#

class puzzle:

	#
	def setInput(self, input):
		self.input = input
		self.lines = self.input.split("\n")

	#
	def handleInput(self):
		self.elves = {};

		elf = 0;
		for line in self.lines:

			if(line == ""):
				elf = elf+1
			else:
				if not elf in self.elves:
					self.elves[elf] = 0

				self.elves[elf] += int(line)

		sorted_elves = sorted(self.elves.items(), key=lambda x:x[1])
		self.elves = dict(sorted_elves)

	# --- Part One ---
	#
	# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
	#
	def part1(self):

		# Get the elf carrying the most calories and return the amount of calories.
		# 
		k, calories = _, self.elves[k] = self.elves.popitem()
		return calories

	# --- Part Two ---
	#
	# By the time you calculate the answer to the Elves' question, they've already realized
	# that the Elf carrying the most Calories of food might eventually run out of snacks.
	#
	# To avoid this unacceptable situation, the Elves would instead like to know the total
	# Calories carried by the top three Elves carrying the most Calories. That way, even if one
	# of those Elves runs out of snacks, they still have two backups.
	#
	# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then
	# the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of
	# the Calories carried by these three elves is 45000.
	#
	# Find the top three Elves carrying the most Calories. How many Calories are those Elves
	# carrying in total?
	#
	def part2(self):

		#
		top3_total = 0

		# Get the elf carrying the most calories, add it's calories to the total of calories
		# and delete the elf from the list, so a new elf will become the one carrying the
		# most calories.
		# 
		elf, calories = _, self.elves[elf] = self.elves.popitem()
		del self.elves[elf]
		top3_total += calories

		# Again, get the elf carrying the most calories, add it's calories to the total of
		# calories and also delete this elf from the list, so a new elf will become the one
		# carrying the most calories.
		# 
		elf, calories = _, self.elves[elf] = self.elves.popitem()
		del self.elves[elf]
		top3_total += calories

		# For the last time, the elf carrying the most calories and add it's calories to the
		# total of calories.
		# 
		elf, calories = _, self.elves[elf] = self.elves.popitem()
		top3_total += calories

		# Return the total calories for the top 3 elves carrying the most calories
		#
		return top3_total

##
## https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
## https://stackoverflow.com/questions/71740593/retrieving-last-value-of-a-python-dictionary
## https://www.w3schools.com/python/ref_dictionary_popitem.asp
## https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
##
