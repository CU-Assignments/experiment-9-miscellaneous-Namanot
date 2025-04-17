class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_freq = 0
        for f in freq:
            if f > max_freq:
                max_freq = f

        max_count = 0
        for f in freq:
            if f == max_freq:
                max_count += 1

        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count

        return max(len(tasks), empty_slots)

        