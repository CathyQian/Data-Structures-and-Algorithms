"""
Design Log Storage System

You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.

int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:

put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.

Note:

    There will be at most 300 operations of Put or Retrieve.
    Year ranges from [2000,2017]. Hour ranges from [00,23].
    Output for Retrieve has no order required.

"""

class LogSystem:

    def __init__(self):
        self.time2id = collections.defaultdict(list)

    def put(self, id: int, timestamp: str) -> None:
        self.time2id[timestamp].append(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        granu2length = {'Year':4, 'Month':7, 'Day':10, 'Hour':13, 'Minute':16, 'Second':19}
        length = granu2length[granularity]
        start, end = start[:length], end[:length]
        
        res = []
        for time, ids in self.time2id.items():
            if start <= time[:length] <= end:
                res.extend(ids)
        return res

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)


# change list to set if consider duplicated input
class LogSystem:

    def __init__(self):
        self.time2id = collections.defaultdict(set)
        self.granularity = {"Year": 4, "Month": 7, "Day": 10, 
                            "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id: int, timestamp: str) -> None:
        self.time2id[timestamp].add(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        length = self.granularity[granularity]
        start, end = start[:length], end[:length]
        for time, ids in self.time2id.items():
            if start <= time[:length] <= end:
                res += list(ids)
        return res
            


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)