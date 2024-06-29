class FrequencyTracker:

    def __init__(self):
        self.num_freq = {}
        self.freq_nums = {}

    def add(self, number: int) -> None:
        curr_freq = self.num_freq.get(number, 0)
        new_freq = curr_freq + 1
        self.num_freq[number] = new_freq

        if curr_freq in self.freq_nums:
            self.freq_nums[curr_freq].remove(number)
            if not self.freq_nums[curr_freq]:
                del self.freq_nums[curr_freq]

        if new_freq not in self.freq_nums:
            self.freq_nums[new_freq] = set()
        self.freq_nums[new_freq].add(number)

    def deleteOne(self, number: int) -> None:
        if number in self.num_freq:
            curr_freq = self.num_freq[number]

            self.freq_nums[curr_freq].remove(number)
            if not self.freq_nums[curr_freq]:
                del self.freq_nums[curr_freq]

            if curr_freq > 1:
                self.num_freq[number] = curr_freq - 1
                new_freq = curr_freq - 1
                
                if new_freq not in self.freq_nums:
                    self.freq_nums[new_freq] = set()
                self.freq_nums[new_freq].add(number)
            
            else:
                del self.num_freq[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_nums and bool(self.freq_nums[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)