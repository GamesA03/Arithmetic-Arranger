def arithmetic_arranger(problems, display_answers=False):
  # Check if there are too many problems
  if len(problems) > 5:
      return "Error: Too many problems."

  arranged_problems = []  # List to hold each line of the arranged problems

  # Splitting each problem into its components and arranging them
  for problem in problems:
      parts = problem.split()
      operator = parts[1]
      operand1 = parts[0]
      operand2 = parts[2]

      # Validate operator
      if operator not in ["+", "-"]:
          return "Error: Operator must be '+' or '-'."

      # Validate operands are digits and not too long
      if not (operand1.isdigit() and operand2.isdigit()):
          return "Error: Numbers must only contain digits."
      if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."

      # Determine spacing
      length = max(len(operand1), len(operand2)) + 2  # +2 for operator and space
      top = operand1.rjust(length)
      bottom = operator + operand2.rjust(length - 1)
      line = "-" * length
      sum = ""
      if display_answers:
          if operator == "+":
              sum = str(int(operand1) + int(operand2)).rjust(length)
          else:
              sum = str(int(operand1) - int(operand2)).rjust(length)

      # Add to the arranged_problems list
      if not arranged_problems:  # If first problem, initialize lists
          arranged_problems = [top, bottom, line, sum]
      else:  # Append to existing lists with spacing
          arranged_problems[0] += "    " + top
          arranged_problems[1] += "    " + bottom
          arranged_problems[2] += "    " + line
          if display_answers:
              arranged_problems[3] += "    " + sum

  # Join each line with a newline and return
  arranged_problems = '\n'.join(arranged_problems).rstrip()
  return arranged_problems