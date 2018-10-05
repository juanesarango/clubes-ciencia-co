# Palindromes Errors

Remember this problem from the beginning of your prep work? Let's add in some functionality to this method to raise errors when we don't get the expected type of argument (i.e. an array of integers). Do a check at the beginning of the method to raise an ArgumentError if the input is not exactly as expected (nil, a string, an array that's not 100% integers, etc.). Make sure to add in some handy error messages.

```ruby
# Problem 6: Palindromes
#
# Write a method, palindromes, that accepts an array of numbers as an argument and returns
# an array of only the numbers that are palindromes. Palindromes are numbers that are the
# same forward and backward. Numbers in the returned array should be in the same order as
# in the original array.
#
# For Example:
#
# 101 is the same forward and backward. It is a palindrome.
# 102 is 201 backwards; it is not a palindrome.

def palindromes(arr)
  ind = 0
  palindromes = []

  while ind < arr.length
    if arr[ind].to_s.reverse == arr[ind].to_s
      palindromes.push(arr[ind])
    end

    ind = ind + 1
  end

  palindromes
end
```
