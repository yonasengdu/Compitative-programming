class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        Duplicate_file_path = dict()
        length_paths_array = len(paths)
        
        #get a path 
        for path_index in range(length_paths_array):
            path = paths[path_index]
            files = path.split()
            root_path = files[0]
            length_files_array = len(files)
            for file_index in range(1,length_files_array):
                file_in_one_path = files[file_index]
                Type,nth_file = file_in_one_path.split("(")
                temp_file_path = [root_path, "/",Type]
                formatted_nth_file = nth_file[:-1]
                new_val = ''.join(temp_file_path)
                if formatted_nth_file in  Duplicate_file_path:
                        val = Duplicate_file_path[formatted_nth_file]
                        val.append(new_val)
                        Duplicate_file_path[formatted_nth_file] = val
                        
                else:
                    Duplicate_file_path[formatted_nth_file] = [new_val]
        ans  = [arr for arr in  Duplicate_file_path.values() if len(arr)>=2]
        return ans
                    
                    
                
        