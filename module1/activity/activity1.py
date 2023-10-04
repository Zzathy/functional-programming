def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == "+":
            return add(tree(left_operand), tree(right_operand))
        elif operator == "-":
            return minus(tree(left_operand), tree(right_operand))
        elif operator == "*":
            return mult(tree(left_operand), tree(right_operand))
        elif operator == "/":
            return div(tree(left_operand), tree(right_operand))
        
expression_tree = ((2, "+", 3), "*", (5, "-", 1))

result = tree(expression_tree)

print("hasil evaluasi pohon ekspresi: ", result)