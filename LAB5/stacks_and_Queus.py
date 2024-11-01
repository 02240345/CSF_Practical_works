# Part 1: Implementing a Stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) 
print(stack.peek())  
print(stack.size())  


# Part 2: Implementing a Queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.front())  
print(queue.size()) 


# Part 3: Solving Practical Problems

def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))")) 
print(is_balanced("(()"))  


# Problem 2: Reverse a String

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, I am Choeying!"))  


# Problem 3: Hot Potato Simulation

def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Karma", "Thug", "Dechen", "Nima", "Dechen", "Choeying"]
print(hot_potato(names, 7))  





# Exercises

# 1.Using a stack to evaluate postfix expressions.

def evaluate_postfix(expression):
    stack = Stack()
    for token in expression:
        if token.isdigit():  
            stack.push(int(token))
        else:  
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    
    return stack.pop()

# Test the function
postfix_expr = "53+82-*"
print(f"Result of postfix expression '{postfix_expr}': {evaluate_postfix(postfix_expr)}")



# 2.Using two stacks to implement a queue.

class QueueUsingStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, item):
        self.stack_in.push(item)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if not self.stack_out.is_empty():
            return self.stack_out.pop()
        else:
            raise IndexError("Queue is empty")

# Test the function
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
queue.enqueue(4)
print(queue.dequeue())  
print(queue.dequeue())  



# 3.Implementing a basic task scheduler that processes tasks in the order they were added.

class TaskScheduler:
    def __init__(self):
        self.tasks = Queue()

    def add_task(self, task):
        self.tasks.enqueue(task)

    def process_tasks(self):
        while not self.tasks.is_empty():
            current_task = self.tasks.dequeue()
            print(f"Processing task: {current_task}")

# Test the function
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.process_tasks()



# 4.Using a stack to convert infix expressions to postfix.

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    output = []
    operators = Stack()

    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':  # Left parenthesis
            operators.push(token)
        elif token == ')':  # Right parenthesis
            while not operators.is_empty() and operators.peek() != '(':
                output.append(operators.pop())
            operators.pop()  # Pop the '('
        else:  # Operator
            while (not operators.is_empty() and precedence[operators.peek()] >= precedence[token]):
                output.append(operators.pop())
            operators.push(token)
    
    while not operators.is_empty():
        output.append(operators.pop())
    
    return ''.join(output)

# Test the function
infix_expr = "A+B*(C-D)"
print(f"Postfix of '{infix_expr}': {infix_to_postfix(infix_expr)}")

