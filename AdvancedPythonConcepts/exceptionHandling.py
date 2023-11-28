'''
section 2 lecture 5: Exception Handling
concentrating mostly on Runtime Errors.
Decided to addd some extras as this is very low level exception handling.
Really don't like that if the exception is raised it is not handled in any way
and the program is allowed to continue to the next statements.
Tutor puts all the code into the try block, but I think it is better to have 2 try blocks
to handle the errors with various print statements thus you can give plain language
and loop back to the input to try again.

Note that when run the result of the division always seems to come  back as a float
which makes sense as wouldn't want an integer return if the result had a decimal fraction.
'''
try:
    a: int = int(input('Enter a:> '))
    b: int = int(input('Enter b:> '))
except ValueError as inp_err:
    print(f'One of your values is not within range.  Please check and try again.  Error Raised: {
          inp_err}')
    exit()
try:
    print(a/b)
except (ZeroDivisionError, ValueError) as er:
    print(
        f'Sorry. Your input has a problem.  Please review your input.  If error continues please phone helpdesk quating: "{er}"')
finally:
    print('Very important line')
