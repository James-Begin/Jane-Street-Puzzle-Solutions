![Screenshot 2022-07-11 134345](https://user-images.githubusercontent.com/103123677/178325886-b7cabbd0-9bbb-44e0-93a1-14c2570593e5.png)

The taxicab distance is defined as |y2 - y1| + |x2 - x1| where the first point is (x1, y1) and the second point is (x2, y2). Basically, it is the sum of the vertical and horizontal distance from one point to another.

Because all the distances are easily calculatable and all positive integers, this problem can be done by hand relatively easily. Although, this could be solved using programming as well.

# Solution
![20220711_140932](https://user-images.githubusercontent.com/103123677/178330116-986a0c6b-f854-4211-ae3c-db57e3b5394a.jpg)

The first step is to fill in the easy spots like the single 1s and use the given values to try filling in as much as you can. At the later stages of the puzzle, guess and check becomes more difficult as you have to backtrack alot more and confirm each change doesn't mess up the surrounding values. Overall, keep track of the given values and focus on the larger values as there are fewer different spots they can be placed.
