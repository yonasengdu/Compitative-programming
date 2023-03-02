class Solution:
    def simplifyPath(self, path: str) -> str:
        # create an arry of path elements whithout including "/"
        path_arr = path.split("/")
        
        canonical_path_tracker = []
        canonical_path = ""
        
        # build my new path based on the parameters (its an array)
        for ind in range(len(path_arr)):
            if path_arr[ind] == ".."  :
                if canonical_path_tracker:
                    canonical_path_tracker.pop()
                else: 
                    continue
            elif path_arr[ind] == "" or path_arr[ind] == ".":
                continue
            else:
                 canonical_path_tracker.append(path_arr[ind])
                    
                    
        # finishing to build the path by including the "/" as a separator
        canonical_path += "/"          
        for ind in range(len(canonical_path_tracker)):
            if canonical_path[-1] != "/":
                canonical_path += "/"  
            canonical_path += canonical_path_tracker[ind]
            
            
        return canonical_path 
            
            
            
                