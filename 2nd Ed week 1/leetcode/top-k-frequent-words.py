class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def insertion_sort(bucket):
            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
                
            return bucket

        count_dict = {}
        word_set = set(words)
        
        for word in word_set:
            count = words.count(word)

            if count in count_dict:
                count_dict[count].append(word)
            else:
                count_dict[count] = [word]
        
        check = list(count_dict.keys())
        check.sort(reverse = True)

        answer_array = []
        for key in check:
            array = count_dict[key]
            answer_array.extend(insertion_sort(array))

        return answer_array[:k]