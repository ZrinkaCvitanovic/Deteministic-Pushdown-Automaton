import sys


class Transition:
    def __init__(self, attr1, attr2, attr3, attr4, attr5):
        self.initialState = attr1
        self.inputChar = attr2
        self.stackTop = attr3
        self.newState = attr4
        self.newStackTop = attr5


currentLine = input()
testExamples = currentLine.split("|")

currentLine = input()
substrings = currentLine.split(",")
states = set(substrings)

currentLine = input()
substrings = currentLine.split(",")
inputAlphabet = set(substrings)

currentLine = input()
substrings = currentLine.split(",")
stackAlphabet = set(substrings)

currentLine = input()
acceptable = currentLine.split(",")


initialState = input()
initialStackChar = input()

transitions = []
epsilon = []
currentLine = sys.stdin.readline().strip()
while currentLine:
    if len(currentLine) == 0:
        break
    substrings = currentLine.split("->")
    begin = substrings[0].split(",")
    if len(begin) >= 3:
        currentState = begin[0]
        inputChar = begin[1]
        stackChar = begin[2]
        end = substrings[1].split(",")

        newState = end[0]
        stack = end[1]
        t = Transition(currentState, inputChar, stackChar, newState, stack)
        transitions.append(t)
        if inputChar == "$":
            epsilon.append(t)
        currentLine = sys.stdin.readline().strip()

stack = [initialStackChar]
exists = False
myState = initialState

for element in testExamples:
    currentInput = element.split(",")
    print(initialState + "#" + initialStackChar, end="|")
    currentStackTop = initialStackChar
    stack = [initialStackChar]
    myState = initialState
    existsE = True
    existsAny = True
    for char in currentInput:
        exists = False
        existsAny = any(t.inputChar == char for t in transitions)
        charRead = False
        fail = True
        for value in transitions:
            if not existsAny:
                break
            if (
                value.initialState == myState
                and value.inputChar == char
                and value.stackTop == currentStackTop
            ):
                exists = True
                charRead = True
                fail = False
                stack.pop(0)
                for j, s in enumerate(value.newStackTop):
                    stack.insert(j, s)
                currentStackTop = value.newStackTop[0]
                if stack[0] == "$":
                    stack.pop(0)
                    if len(stack) >= 1:
                        currentStackTop = stack[0]
                    else:
                        currentStackTop = "$"

                if len(stack) == 0:
                    stack.append("$")
                print(value.newState + "#", end="")
                for s in stack:
                    print(s, end="")
                print("|", end="")
                myState = value.newState
                break
        if not exists:
            existsE = False
        for ep in epsilon:
            if myState in acceptable and charRead:
                break
            if ep.initialState == myState and ep.stackTop[0] == currentStackTop:
                myState = ep.newState
                existsE = True
                stack.pop(0)
                for j, s in enumerate(ep.newStackTop):
                    stack.insert(j, s)
                currentStackTop = ep.newStackTop[0]
                if stack[0] == "$":
                    stack.pop(0)
                if len(stack) == 0:
                    stack.append("$")
                print(ep.newState + "#", end="")
                for s in stack:
                    print(s, end="")
                print("|", end="")
                if myState in acceptable:
                    exists = True
                    for ep in transitions:
                        if myState in acceptable and charRead:
                            break
                        if (
                            ep.initialState == myState
                            and ep.stackTop[0] == currentStackTop
                            and ep.inputChar == char
                        ):
                            myState = ep.newState
                            existsE = True
                            fail = False
                            stack.pop(0)
                            for j, s in enumerate(ep.newStackTop):
                                stack.insert(j, s)
                            currentStackTop = ep.newStackTop[0]
                            if stack[0] == "$":
                                stack.pop(0)
                            if len(stack) == 0:
                                stack.append("$")
                            print(ep.newState + "#", end="")
                            for s in stack:
                                print(s, end="")
                            print("|", end="")
        if fail:
            print("fail|", end="")
            myState = ""
            break
        if not existsE:
            break
    if myState in acceptable and acceptable[0] != "":
        print("1")
    else:
        print("0")
        if fail:
            continue
