class Solution:
    def interpret(self, command: str) -> str:
        command_map = {'G':'G','()':'o','(al)':'al'}
        command_str = ""
        out_put = ""
        for _ in command:
            if _ == ')' :
                command_str += ") "
            elif _ == 'G':
                command_str += "G "
            else:
                command_str += _
                
        for i in command_str.split():
            if i :
                out_put += command_map[i]
        return out_put
            
        