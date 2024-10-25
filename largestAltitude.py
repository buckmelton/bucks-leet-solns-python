# Leetcode 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

# Constraints:

# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100

# Buck's Observations:
# This is specified as a "prefix sum" problem.
# The solution seems straightforward:
# 
# Initialize current altitude to 0
# Initialize max altitude to 0
# For each gain in gain array
# 	Add gain to current altitude
# 	If new current altitude is greater than max altitude
# 		Set max altitude to current altitude
# Return max altitude

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxAltitude = 0
        curAltitude = 0
        for g in gain:
        	curAltitude += g
        	maxAltitude = max(curAltitude, maxAltitude)
        return maxAltitude