def isBalanced(s):
    stack = []
    for char in s:
        if (char=="(") or (char=="[") or (char=="{"):
            stack.append(char)
        if (char==")") or (char=="]") or (char=="}"):
            if len(stack)==0:
                return "NO"
            current = stack.pop()
            if current == "(" and char == ")":
                continue
            elif current == "[" and char == "]":
                continue
            elif current == "{" and char == "}":
                continue
            else:
                return "NO"
        
    if len(stack)>0:
        return "NO"
    return "YES"

print(isBalanced("}][}}(}][))]"))
print(isBalanced("[](){()}"))
print(isBalanced("()"))
print(isBalanced("({}([][]))[]()"))
print(isBalanced("{)[](}]}]}))}(())("))
print(isBalanced("([[)"))

#Complexity: O(n)