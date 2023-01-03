![2023-01-02 163912](https://user-images.githubusercontent.com/103123677/210279667-c8d20ad8-402e-492f-b967-c438a215f811.png)
# Solution  
The sum of unvisited squares is 1935.  
The numbers on the dice are 9,9,6,7,-3,-9.

Trying the problem brute force in python, we manage to get to the upper right corner, with the correct solution. Checking the solution on paper, and with a physical dice, we can easily confirm the solution:

![20230102_200202](https://user-images.githubusercontent.com/103123677/210288617-8f51a3c8-4e46-4112-a40c-fdec25de662b.jpg)  

One simple way to check the answer by hand was to find the differences between each square. This is the difference in the score from one square to another. This makes it easy to see which paths are valid by doing some quick mental math and checking whether the difference was divisible by the move number.  

Using this method, we quickly find the correct solution. However, the code solution is not completely correct. Because it does not track the orientation of the dice (only the values), and which side is face up, it could have made a mistake, especially if given a similar problem with different values.  

After confirming both in code and by hand, the unvisited squares are 445, -7, 452, 228, 57, 268, and 492. All of which sum to 1935.
