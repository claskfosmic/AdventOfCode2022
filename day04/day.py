# --- Day 4: Camp Cleanup ---
# Space needs to be cleared before the last supplies can be unloaded from the
# ships, and so several Elves have been assigned the job of cleaning up
# sections of the camp. Every section has a unique ID number, and each Elf is
# assigned a range of section IDs.
#
# However, as some of the Elves compare their section assignments with each
# other, they've noticed that many of the assignments overlap. To try to
# quickly find overlaps and reduce duplicated effort, the Elves pair up and
# make a big list of the section assignments for each pair (your puzzle
# input).
#
# For example, consider the following list of section assignment pairs:
#
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# 
# For the first few pairs, this list means:
#
#  - Within the first pair of Elves, the first Elf was assigned sections
#    2-4 (sections 2, 3, and 4), while the second Elf was assigned sections
#    6-8 (sections 6, 7, 8).
#  - The Elves in the second pair were each assigned two sections.
#  - The Elves in the third pair were each assigned three sections: one got
#    sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
#
# This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:
#
# .234.....  2-4
# .....678.  6-8
#
# .23......  2-3
# ...45....  4-5
#
# ....567..  5-7
# ......789  7-9
#
# .2345678.  2-8
# ..34567..  3-7
#
# .....6...  6-6
# ...456...  4-6
#
# .23456...  2-6
# ...45678.  4-8
#
# Some of the pairs have noticed that one of their assignments fully contains
# the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained
# by 4-6. In pairs where one assignment fully contains the other, one Elf in
# the pair would be exclusively cleaning sections their partner will already
# be cleaning, so these seem like the most in need of reconsideration. In
# this example, there are 2 such pairs.
#

class puzzle:

	#
	def setInput(self, input):
		self.input = input
		self.lines = self.input.split("\n")

	#
	def handleInput(self):
		self.elvenPairs = [];

		for line in self.lines:
			
			pairs = line.split(",")
			
			firstPair = pairs[0].split("-")
			secondPair = pairs[1].split("-")

			sectionsElf1 = []
			sectionsElf2 = []

			for s in range(int(firstPair[0]), int(firstPair[1])+1):
				sectionsElf1.append(s)

			for s in range(int(secondPair[0]), int(secondPair[1])+1):
				sectionsElf2.append(s)

			self.elvenPairs.append([sectionsElf1, sectionsElf2])

		return

	#
	def getOverlappingSections(self, sectionsElf1, sectionsElf2):
		return list(filter(lambda x: x in sectionsElf1, sectionsElf2))

	def hasDoubleSections(self, sectionsElf1, sectionsElf2):
		doubleSections = self.getOverlappingSections(sectionsElf1, sectionsElf2)
		return len(doubleSections) == len(sectionsElf1) or len(doubleSections) == len(sectionsElf2)

	def hasOverlappingSections(self, sectionsElf1, sectionsElf2):
		doubleSections = self.getOverlappingSections(sectionsElf1, sectionsElf2)
		return len(doubleSections) > 0
		

	# --- Part One ---
	#
	# In how many assignment pairs does one range fully contain the other?
	#
	def part1(self):

		doubleSections = 0

		for elvenPair in self.elvenPairs:
			if self.hasDoubleSections(elvenPair[0], elvenPair[1]):
				doubleSections += 1

		return doubleSections;

	# --- Part Two ---
	#
	# It seems like there is still quite a bit of duplicate work planned.
	# Instead, the Elves would like to know the number of pairs that overlap at
	# all.
	#
	# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't
	# overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and
	# 2-6,4-8) do overlap:
	#
	#  - 5-7,7-9 overlaps in a single section, 7.
	#  - 2-8,3-7 overlaps all of the sections 3 through 7.
	#  - 6-6,4-6 overlaps in a single section, 6.
	#  - 2-6,4-8 overlaps in sections 4, 5, and 6.
	# 
	# So, in this example, the number of overlapping assignment pairs is 4.
	# 
	# In how many assignment pairs do the ranges overlap?
	#
	def part2(self):

		overlappingSections = 0

		for elvenPair in self.elvenPairs:
			if self.hasOverlappingSections(elvenPair[0], elvenPair[1]):
				overlappingSections += 1

		return overlappingSections;