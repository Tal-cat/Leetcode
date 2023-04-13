class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #if an element is pushed onto the stack, it can only be popped after all the elements pushed before it have been popped.
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return stack == []
