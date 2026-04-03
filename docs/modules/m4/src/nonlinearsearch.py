def non_linear_search(initial_state):
   frontier = ???
   visit(initial_state)
   process(initial_state)
   frontier.add(initial_state)
   while not frontier.is_empty():
      state = frontier.next()
      for neighbor in state.get_neighbors():
         if not is_visited(neighbor):
            visit(neighbor)
            process(neighbor)
            frontier.add(neighbor)

def breadth_first_search(initial_state):
   frontier = ArrayQueue()
   visit(initial_state)
   process(initial_state)
   frontier.enqueue(initial_state)
   while not frontier.is_empty():
      state = frontier.dequeue()
      for neighbor in state.get_neighbors():
         if not is_visited(neighbor):
            visit(neighbor)
            process(neighbor)
            frontier.enqueue(neighbor)

def depth_first_search(initial_state):
   frontier = ArrayStack()
   visit(initial_state)
   process(initial_state)
   frontier.push(initial_state)
   while not frontier.is_empty():
      state = frontier.pop()
      for neighbor in state.get_neighbors():
         if not is_visited(neighbor):
            visit(neighbor)
            process(neighbor)
            frontier.push(neighbor)
