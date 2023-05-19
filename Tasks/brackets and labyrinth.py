from lsq import mycollections as mc


if __name__ == "__main__":
    input_text = input("Text with parentheses: ")
    print(f"INPUT: {input_text}")
    split_text = input_text.split()
    print(f"SPLIT: {split_text}")
    _filter = ('(', ')')
    queue = mc.Queue()
    parentheses = [i for i in input_text if i in _filter]
    print(f"SKOBKI: {parentheses}")
    n = 0
    for i in parentheses:
        if i == '(':
            queue.enqueue(i)
            parentheses.pop(n)
        elif i == ')' and len(queue) != 0:
            queue.dequeue()
            parentheses.pop(n)
        n += 1
    if len(queue) > 0:
        print(f"There is {len(queue)} opening brackets left\n")
    elif len(parentheses) > 0:
        print(f"There is {len(parentheses)} closing brackets left")
    else:
        print("All good")

