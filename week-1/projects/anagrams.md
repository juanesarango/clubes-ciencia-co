# Anagrams

For this problem, we want to write a method that determines if two strings are anagrams. Two words are anagrams if they can be rearranged to form one another. For example:

```ruby
anagram?("hello", "hola")    #=> false
anagram?("program", "romprag")    #=> true
```

You can assume that there is no whitespace or punctuation in the given strings.

## Learning Goals

* Calculate time and space complexity of an algorithm
* Recognize when and how time or space complexity can be improved
* Compare different methods and discuss how changing inputs affects each one's overall runtime

## Part 1
Write a method `#first_anagram?` that will generate and store all the possible anagrams of the first string. Check if the second string is one of these.

**Hints:**
* **For testing your method, start with small input strings, otherwise you might wait a while**

What is the time complexity of this solution? What happens if you increase the size of the strings?

## Part 2
Write a method `#second_anagram?` that iterates over both strings. As you find letters that appear in both words, delete them one at a time. They are anagrams if both the strings are empty at the end.

Try varying the length of the input strings. What are the differences between `#first_anagram?` and `#second_anagram?`?

## Part 3
Write a method `#third_anagram?` that solves the problem by sorting both strings alphabetically. The strings are then anagrams if and only if the sorted versions are the identical.

What is the time complexity of this solution? Is it better or worse than `#second_anagram?`?

## Part 4
Write one more method `#fourth_anagram?`. This time, use two Hashes to store the number of times each letter appears in both words. Compare the resulting hashes.

What is the time complexity?
