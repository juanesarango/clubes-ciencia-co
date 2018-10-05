# Binary Search

Binary search is a common algorithm used to search a sorted list of values. The binary search algorithm compares the target value to the middle value in the list. If the target is greater than the middle value, it performs the same procedure on the left half of the list - comparing to the middle value of the left side of the list. If the number is smaller, it does the same on the right side of the list, continuing to subdivide in this manner until the target value is retrieved, or every value is searched.

Read more about the algorithm here: https://en.wikipedia.org/wiki/Binary_search_algorithm

Also, watch this video: https://www.youtube.com/watch?v=5xlIPT1FRcA

Then:

Write a recursive method `bsearch(array,
target)`. Keep in mind: Binary search will only work on a sorted array! Sort every array input you plug into your function.

Part 1:

return true if the value exists in the array, else return false.

```rb
bsearch([1, 2, 3], 1) # => true
bsearch([2, 3, 4, 5], 3) # => true
bsearch([2, 4, 6, 8, 10], 6) # => true
bsearch([1, 3, 4, 5, 9], 5) # => true
bsearch([1, 2, 3, 4, 5, 6], 6) # => true
bsearch([1, 2, 3, 4, 5, 6], 0) # => nil
bsearch([1, 2, 3, 4, 5, 7], 6) # => nil
```

Part 2 (bonus):

return the index of the value if it exists in the array, else return nil.

```rb
bsearch([1, 2, 3], 1) # => 0
bsearch([2, 3, 4, 5], 3) # => 1
bsearch([2, 4, 6, 8, 10], 6) # => 2
bsearch([1, 3, 4, 5, 9], 5) # => 3
bsearch([1, 2, 3, 4, 5, 6], 6) # => 5
bsearch([1, 2, 3, 4, 5, 6], 0) # => nil
bsearch([1, 2, 3, 4, 5, 7], 6) # => nil
```
