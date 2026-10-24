class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==0:
            return False
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (
                  stack[-1]=="(" and s[i]==")"
                  or stack[-1]=="[" and  s[i]=="]" or 
                  stack[-1]=="{" and s[i]=="}") :
                  stack.pop()
          
                else:
                    return False
        return len(stack)==0
solver=Solution()
print(solver.isValid("[[}]]"))
      
      