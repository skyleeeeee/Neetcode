class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def get(self, i: int) -> int:
        """Return the element at index i."""
        # assumes 0 <= i < self._size
        return self._data[i]

    def set(self, i: int, n: int) -> None:
        """Set the element at index i to n."""
        # assumes 0 <= i < self._size
        self._data[i] = n

    def pushback(self, n: int) -> None:
        """Append n to the end of the array, resizing if needed."""
        if self._size >= self._capacity:
            self.resize()
        self._data[self._size] = n
        self._size += 1

    def popback(self) -> int:
        """Remove and return the last element."""
        if self._size == 0:
            raise IndexError("popback from empty DynamicArray")
        val = self._data[self._size - 1]
        self._size -= 1
        return val

    def resize(self) -> None:
        """Double the capacity of the array."""
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for idx in range(self._size):
            new_data[idx] = self._data[idx]
        self._data = new_data
        self._capacity = new_capacity

    def getSize(self) -> int:
        """Return the number of stored elements."""
        return self._size

    def getCapacity(self) -> int:
        """Return the total capacity of the array."""
        return self._capacity
