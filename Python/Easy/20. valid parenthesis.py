def valid_paren(input_str):
  # Declaring stack
  stack = []

  # looping through the strings
  for paren in input_str:
    if paren == '[' or paren == '{' or paren == '(':
      stack.append(paren)
    
    else:
      # In the case of valid parenthesis, the stack cannot be empty. So if stack is empty the
      # parenthesis is invalid.
      if not stack: # If stack is empty this code will run
        print(input_str, 'contain invalid parenthesis')
        return

      else:

        # check if the last character matches the right closing, if it does remove it.
        top = stack[-1]
        if paren == ']' and top == '[' or paren == ')' and top == '(' or paren == '}' and top == '{':
          stack.pop()

        # the below line of code is actually not necessary.
        else:
          print(input_str, 'contains invalid parenthesis')
          return

    '''Remember you pop out all the values that match so if the list is empty the string is valid.
       If it is not empty then it is invalid.'''
  if not stack:
    print(input_str, 'The string is valid')

  else:
    print(input_str, 'the string is not valid')

  return


input1 = "{{}}()[()]"
input2 = "{][}"
input3 = '()()'
input4 = '('

valid_paren(input1)
valid_paren(input2)
valid_paren(input3)
valid_paren(input4)


      