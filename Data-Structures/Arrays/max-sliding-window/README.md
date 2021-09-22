Find the maximum number in a sliding window of an array problem.
Given a large array of integers and a window of size ww, find the current maximum value in the window as the window slides through the entire array.

Let’s try to find all maximums for a window size equal to 33 in the array given below:

[-4,2,-5,3,6]

Step 1: For the first 33 elements in the window, max is 22.

max = 2 [-4,2,-5 ,3,6]

Step 2: Slide window one position to the right and max for window becomes 33.

max = 3 [-4,2,-5 ,3,6]

Step 3: In the last window, max is 66.

max = 6 [-4,2,-5 ,3,6]
