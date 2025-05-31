#!/usr/bin/env python3

class CountedIterator:
    """An iterator that counts how many items have been iterated over."""
    
    def __init__(self, iterable):
        """Initialize with an iterable and reset counter."""
        self.iterator = iter(iterable)
        self.count = 0
    
    def __next__(self):
        """Return next item while incrementing counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise
    
    def get_count(self):
        """Return current iteration count."""
        return self.count
    
    def __iter__(self):
        """Return self to make it both iterator and iterable."""
        return self
