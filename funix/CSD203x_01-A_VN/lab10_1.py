# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    # n = int(input())
    n = 5
    # self._data = [int(s) for s in input().split()]
    self._data = [5, 4, 3, 2, 1]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps0(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def GenerateSwaps(self):
    def siftDown( i ):
      """
      Sift down operation to maintain the heap property.
      Compares the element at index i with its children
      and swaps it with the smaller child if necessary.

      :param i: Index of the element to sift down
      """
      minI = i
      leftChild = 2 * i + 1
      if leftChild < size and self._data[leftChild] < self._data[minI]:
        minI = leftChild
      rightChild = 2 * i + 2
      if rightChild < size and self._data[rightChild] < self._data[minI]:
        minI = rightChild
      if i != minI:
        # Swap the element at index i with the smaller child
        self._swaps.append((i, minI))
        self._data[i], self._data[minI] = self._data[minI], self._data[i]
        siftDown(minI)
    size = len(self._data)
    for i in range(size//2-1, -1, -1):
      siftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
  heap_builder = HeapBuilder()
  heap_builder.Solve()