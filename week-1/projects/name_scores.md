# Name Scores

## Part 1

Here we're going to work on another problem taken from Project Euler:

https://projecteuler.net/problem=22

Using what you've learned about I/O, download the names.txt file and write a Ruby program to parse the file and return the name scores for each name in the file.

## Part 2

Now, upgrade your program from Part 1 to write the names from the names.txt file into a separate CSV file in alphabetical order including each name's alphabetical position, alphabetical value, and name score. For example:

Colin,938,53,49714

This would be one line of the resulting output file, in the format NAME,POSITION,VALUE,SCORE. Learn about the Ruby CSV library and CSVs in-general here:

http://ruby-doc.org/stdlib-2.0.0/libdoc/csv/rdoc/CSV.html

https://en.wikipedia.org/wiki/Comma-separated_values

## Part 3

Let's upgrade our program even further. Now, let's allow the user to specify the input file from the command line. So, rather than running the program like so:

```
ruby name_scores.rb
```

Let's add in an argument so we can specify which file we want to use. For example, I should be able to run this if the names.txt file is in my Downloads folder:

```
ruby name_scores.rb ~/Downloads/names.txt
```
## Part 4

Write a separate program that can take the CSV generated from Part 2 and search it for a particular name, returning its name score and printing it to the screen. For example:

```
$ ruby find_name.rb ~/Desktop/names.csv colin
$ 49714
```
