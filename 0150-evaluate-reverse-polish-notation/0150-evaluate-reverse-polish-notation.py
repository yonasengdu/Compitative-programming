class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_tracker = []
        oprations = {"+","-","*","/"}
        for ind in range(len(tokens)):
           
            if tokens[ind] in oprations:
                first_num = int(eval_tracker.pop())
                second_num = int(eval_tracker.pop())
                if tokens[ind] == "+":
                    eval_tracker.append(first_num + second_num)
                elif tokens[ind] == "-":
                    eval_tracker.append(second_num - first_num )
                elif tokens[ind] == "*":
                    eval_tracker.append(first_num * second_num)
                elif tokens[ind] == "/":
                    if second_num / first_num < 0:
                        eval_tracker.append(ceil(second_num / first_num))
                    else:
                        eval_tracker.append(floor(second_num / first_num))
            else:
                eval_tracker.append(tokens[ind])
        return int(eval_tracker[-1])