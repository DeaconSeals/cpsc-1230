def evaluate_postfix(expression: Queue):
   value_stack = LinkedStack()
   while not expression.is_empty():
      token = expresion.dequeue()
      if is_operator(token):
         right_val = value_stack.pop()
         left_val = value_stack.pop()
         value_stack.push(evaluate(token, left_val, right_val))
      elif is_value(token):
         value_stack.push(float(token))
   return value_stack.peek()