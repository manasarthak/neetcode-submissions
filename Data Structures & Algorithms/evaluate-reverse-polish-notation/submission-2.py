class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch not in ("+","-","*","/"):
                st.append(ch)
            else:
                num1,num2=int(st.pop()),int(st.pop())
                if ch == "+":
                    st.append(num1+num2)
                elif ch == "-":
                    st.append(num2-num1)
                elif ch == "*":
                    st.append(num1*num2)
                else:
                    st.append(num2/num1)
        return int(st.pop())
        