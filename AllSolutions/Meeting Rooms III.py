"""
Meeting Rooms III

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
 

Constraints:

1 <= n <= 100
1 <= meetings.length <= 105
meetings[i].length == 2
0 <= starti < endi <= 5 * 105
All the values of starti are unique.


"""
# wrong solution, does not satisfy "Each meeting will take place in the unused room with the lowest number."
from heapq import heapify, heappop, heappush
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # use heap
        h = [(0, i) for i in range(n)] #availtime, roomnum
        room_cnts = [0]*n # roomnum: cnts, no dictionary needed here
        heapify(h)
        meetings.sort()
        for meeting in meetings:
            endtime, room = heappop(h)
            endtime = meeting[1] + max(0, endtime - meeting[0])
            heappush(h, (endtime, room))
            room_cnts[room] += 1
        return room_cnts.index(max(room_cnts))
    


# right solution: use two heaps
# Time complexity: O(m∗(log(m)+log(n)))) (actually m*(log(m) + 2log(n)), but big-O notation ignores constants)
# Space complexity: O(n)
# n is room number, m is meeting number
from heapq import heapify, heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meeting_counts = [0] * n
        meeting_ends_heap = []  # [end, room_id]
        free_rooms_heap = list(range(n))
        heapify(free_rooms_heap) # O(n)

        meetings.sort() # O(mlogm)

        for start, end in meetings: # O(m)
            while meeting_ends_heap and start >= meeting_ends_heap[0][0]:
                _, room_id = heappop(meeting_ends_heap) # note only need room number, no need to put back to meeting_ends_heap once the room is free, O(1)
                heappush(free_rooms_heap, room_id) # O(logk)
            
            delay = 0 
            if free_rooms_heap: # O(1)
                room_id = heappop(free_rooms_heap)
            else: # O(1)
                delay = meeting_ends_heap[0][0] - start
                _, room_id = heappop(meeting_ends_heap)
 
            heappush(meeting_ends_heap, [end + delay, room_id]) #O(log(n-k))
            meeting_counts[room_id] += 1
        
        return meeting_counts.index(max(meeting_counts))