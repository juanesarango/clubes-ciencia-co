#Raise These!

Here is a list of exceptions in Ruby:

```ruby
NoMemoryError
ScriptError
  LoadError
  NotImplementedError
  SyntaxError
SecurityError
SignalException
  Interrupt
StandardError -- default for rescue
  ArgumentError
    UncaughtThrowError
  EncodingError
  FiberError
  IOError
    EOFError
  IndexError
    KeyError
    StopIteration
  LocalJumpError
  NameError
    NoMethodError
  RangeError
    FloatDomainError
  RegexpError
  RuntimeError -- default for raise
  SystemCallError
    Errno::*
  ThreadError
  TypeError
  ZeroDivisionError
SystemExit
SystemStackError
```

These all inherit from the Exception Class, and this list was taken from here: http://blog.honeybadger.io/understanding-the-ruby-exception-hierarchy/.

Write a line (or a few lines) of code for each of these exceptions that will cause it to be raised. For example, the following code will raise a TypeError:

```ruby
1 + "2"
```
