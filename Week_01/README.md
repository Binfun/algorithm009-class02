## Python版本的 Queue 和 Priority Queue 的源码的分析
### Queue
python的queue的实现在源代码的queue.py里面，
queue里面的真正的写和读的操作的对象其实是 deque，在此基本上增加了一把锁，为了在生产者和消费者的对于queue的操作进行同步。比如join和task_done函数为了让生产者和消费者之间对队列完成的状态进行通知。

队列的主体是deque，deque定义在_collectionsmodule.c里面，对deque的append的操作是deque_append_internal 代码里面可以看到最小块是block。
```
typedef struct BLOCK {
    struct BLOCK *leftlink;
    PyObject *data[BLOCKLEN];
    struct BLOCK *rightlink;
} block;
```

这个结构就是双向链表，对于队列来说，这是一个很好的数据结构。
### Priority Queue
PriorityQueue是继承Queue的，只不过重载了几个函数。

```
    def _put(self, item):
        heappush(self.queue, item)
    def _get(self):
        return heappop(self.queue)
```
这里使用了heapq，可以参考：
https://docs.python.org/2/library/heapq.html
https://docs.python.org/2/library/collections.html

```
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent: # 数字越小，优先级越高
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```

```
                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30
```

可以看到整个heap是这样的形状，存储在0这个位置的item是优先级最高的，其他的依次1，2，3，4优先级逐渐变低。

_siftdown里面需要把刚插入的item的优先级和上一层的parent进行比较，如果优先级高的话，会逐步直到上升到0这个位置上。

而对于左右叶子（比如1和2，3和4）的优先级的调整会在heappop里面的_siftup进行。看到这里我震撼到了，虽然没有了解到完全的细节，但是直观地感受到了这个数据结构的高效——每次pop和push的时候都是O(log(n))的时间复杂度。

## 各类数据结构的时间复杂度如下：
http://www.bigocheatsheet.com
数组：访问O(1)，查找O(n)，插入O(n)，删除O(n)
链表：访问O(n)，查找O(n)，插入O(1)，删除O(1)
跳表：访问O(log(n))，查找O(log(n))，增加O(log(n))，删除O(log(n))
栈：访问O(n)，查找O(n)，插入O(1)，删除O(1)
队列：访问O(n)，查找O(n)，插入O(1)，删除O(1)

跳表是真的牛，用空间换时间，把时间从n换到了log(n)。
三数之和，我以前知道排序之后暴力遍历两个数，然后通过二分查找定位第三个数。可竟然还有两个左右两端的指针不断往中间靠的遍历方法。类似的遍历方法在盛水最多这道题里面也有体现。这么优秀的算法在leetcode里面还很多，要看题解！

## 职业态度
工欲善其事，必先利其器。vs code的一些使用方法：使用ctrl + 左右箭头跳转，使用fn + 左右箭头跳转。不是开玩笑，突然意识到自己原来是个职业程序员，自己多久没有打磨自己的武器了，一身冷汗。

## 代码风格
学习像写报纸一样地写代码，把最重要的函数写在最前面，自顶向下的编程风格。回想起我之前解过的leetcode的题目，我现在都看不懂了，代码的第一眼应该能够让别人猜出你的思路是什么，最好函数名能精确表达意思。

## 解题思路
第一步：把能想到的最笨的办法实现出来，也就是暴力破解法。
第二步：根据题目的规律，找出最多重复的子问题，删除掉不必要的动作进行优化。

## 解题心态
刷题死磕一定要做出来，是因为坚定地认为自己很聪明？其实看题解，理解题解有时候更难。刷题只做一遍，是对自己记忆力的自信？其实这只是为了逃避刷第二次时发现自己原来已经忘记了的尴尬。

一看就会，一写就废，是多数人的常态。解决办法只有：练习是伟大的魔术师，它使看来无法演奏的乐曲得以演奏，并使它变得容易，得心应手——车尔尼。

用开放的心态，多尝试不同的解题思路，比如递归，我之前很排斥递归，因为工程中根本不敢用，怕爆栈，但是这是一种更加贴合现实逻辑的迭代思路，需要学习。我也排斥过哈希表，认为它太占用内存，但是这一次，我败倒在了她绝对速度的石榴裙下。
