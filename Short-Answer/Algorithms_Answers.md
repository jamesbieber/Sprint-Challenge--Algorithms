#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(N) for this particular problem smaller inputs are quite simple, but as you increase N the length of time needed to complete the algorithm increases

b) O(log N) as N becomes larger in this case, the operations remain relatively close together and will usually only require 1-2 more operations to reach the desired value

c) O(N) as N becomes larger, so does the time required to get through the required values.

## Exercise II

I think the idea here will be to pass through every floor while keeping a count i. Everytime the egg DOESN'T break when dropped, you can go to the i _ i floor. If the egg breaks on i _ i you can go back and try to go up i _ i/2 this eliminates the need to visit EVERY floor, saving precious eggs. I think the time complexity would be O(log N) because even if you continue to increase the number of floors exponentionally, i _ i ensures that you will navigate the floors quickly.
