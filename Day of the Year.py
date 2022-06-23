# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: date = "2019-02-10"
# Output: 41

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        day_of_month = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day_of_month[2] += 1
        return sum(day_of_month[:month]) + day
        gy