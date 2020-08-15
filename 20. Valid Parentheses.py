def isValid(self, s):
  """
  :type s: str
  :rtype: bool
  """
  # stack
  stack = []

  if len(s) == 0:
      return True

  for i in s:
      if i == '(' or i == '[' or i == '{':
          stack.append(i)
          continue
      
      if len(stack) == 0:
          return False

      else:
          popped = stack.pop()
          if (popped == '(' and i != ')') or (popped == '[' and i != ']') or (popped == '{' and i != '}'):
              return False

  return len(stack) == 0
