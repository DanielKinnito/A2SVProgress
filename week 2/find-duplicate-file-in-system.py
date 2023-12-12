class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = {}

        for path in paths:
            elements = path.split()
            directory = elements[0]
            
            for file_info in elements[1:]:
                file_info_split = file_info.split('(')
                file_name = file_info_split[0]
                file_content = file_info_split[1][:-1]  # Remove the closing parenthesis
                
                full_path = f"{directory}/{file_name}"
                
                if file_content not in content_dict:
                    content_dict[file_content] = [full_path]
                else:
                    content_dict[file_content].append(full_path)

        duplicate_groups = [group for group in content_dict.values() if len(group) > 1]
        return duplicate_groups