class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(len(word))
        def is_anagram(existing_word, sus_word)->bool:
            if not (len(existing_word) == len(sus_word)):
                return False
            # create hash map for existing word
            mymap = defaultdict(int)
            for char in existing_word:
                mymap[char] +=1

            # create hash map for sus word
            susmap = defaultdict(int)
            for char in sus_word:
                susmap[char] +=1

            #check if sus word is anagram of existing word
            return susmap == mymap

        # build the groups
        groups = []
        for cur_str in strs:
            found = False
            for i in range(len(groups)):
                if is_anagram(groups[i][0], cur_str):
                    groups[i].append(cur_str)
                    found = True
                    break
                
            # no existing group of anagrams
            if not found:
                groups.append([cur_str])  # add a list with the current word to groups
                    
        return groups