class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start_times = sorted([iv[0] for iv in intervals])
        end_times = sorted([iv[1] for iv in intervals])
        start_ptr, end_ptr = 0, 0
        used_rooms = 0
        while start_ptr < len(intervals):
            if start_times[start_ptr] >= end_times[end_ptr]:
                used_rooms -= 1
                end_ptr +=1
            used_rooms += 1
            start_ptr += 1
        return used_rooms
