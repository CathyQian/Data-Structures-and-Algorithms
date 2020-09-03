"""
Find Duplicate File in System

Given a list of directory info including directory path, and all the files with contents in this directory, 
you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, 
respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory 
is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of 
the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

 

Note:

    No order is required for the final output.
    You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
    The number of files given is in the range of [1,20000].
    You may assume no files or directories share the same name in the same directory.
    You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.

 
Follow-up beyond contest:

    Imagine you are given a real file system, how will you search files? DFS or BFS?
    If the file content is very large (GB level), how will you modify your solution?
    If you can only read the file by 1kb each time, how will you modify your solution?
    What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
    How to make sure the duplicated files you find are not false positive?


"""
# use HashMap
# Time complexity: O(n∗x). n strings of average length x is parsed.
# Space complexity: O(n∗x). map and res size grows up to n∗x.
import collections

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path = collections.defaultdict(list)
        for path in paths:
            path = path.split(' ')
            for i in range(1, len(path)):
                pp = path[i].split('(')
                p, c = pp[0], pp[1][:-1]
                content_path[c].append(path[0]+'/'+p)

        return [x for x in content_path.values() if len(x) > 1] 

"""
    Imagine you are given a real file system, how will you search files? DFS or BFS?
    If the file content is very large (GB level), how will you modify your solution?
    If you can only read the file by 1kb each time, how will you modify your solution?
    What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
    How to make sure the duplicated files you find are not false positive?

"""
"""
Solution:
??? BFS, search by directory, BFS is easier to parellelize (DFS is a sequential procedure and thus cannot be parallelized easily)
(FYI: files which are close in filesystem may not exist close in the physical memory as well.)
Do the following for comparing multiple files:
    compare sizes, if not equal, then files are different and stop here!
    hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet), if not equal then stop here!
    compare byte by byte to avoid false positives due to collisions.
- before hash, we can use partially hash code of contents as keys to group them in a map, and continue to hash the rest of the content to
further separate each group. We can continue to do this untill we have to compare them byte-by-byte. And time complexity should be N*L.
"""