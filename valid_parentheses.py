# Valid Parentheses - Takes string 
def isValid(s):
        for i in s:
            if(i=="(" or i=="[" or i=="{"):
                arr.append(i)
            elif i == ")" and len(arr)!=0 and arr[-1] == "(":
                arr.pop()
            elif i == "}" and len(arr)!=0 and arr[-1] == "{":
                arr.pop()
            elif i == "]" and len(arr)!=0 and arr[-1] == "[":
                arr.pop()
            else:
                return False
        return len(arr)==0
