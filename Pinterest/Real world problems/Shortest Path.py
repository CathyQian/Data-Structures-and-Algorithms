"""
一个二维的board,里面有0（表示可以通过），1（wall不能通过），6（monster，可以通过但是会丢一条命）。
input是start position, end position 和lives(有多少命)。问start到end的最短距离有没有是不是还需
要记录到达每个点有可能剩几条命和走了几步？
比如 Point(X,Y) 有 (10步，剩3条命) (8步，剩1条命) 这样？
"""