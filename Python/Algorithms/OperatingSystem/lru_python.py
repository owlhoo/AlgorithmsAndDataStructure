# LRU Cache 
# This replacement policy is used in cache as a policy that removes
# the item that is least recently used with having in mind that if
# the item is used now, it is more probable that it will be used again sooner 
# than the one least recently used


# Class representing Cache using LRU replacement policy
class LruCache():
    # initialise with capacity which represents max number of items in cache 
    def __init__(self, capacity = 5):
        self.cache = []
        self.max_capacity = capacity

    # if the queue is full, remove the least recently used element (always at the start of list)
    # then append the new item
    def add_item(self, item):
        if len(self.cache) + 1 > self.max_capacity:
            del self.cache[0]
        self.cache.append(item)
        return self

    # remove item from LRU cache
    def remove_item(self, item):
        self.cache.remove(item)
        return self

    # simulate the usage of item (i.e. referencing a page in memory)
    def use_item(self, item):
        self.remove_item(item)
        self.add_item(item)
        return self
    
    def print(self):
        print(f"Max capacity of cache is: {self.max_capacity}")
        print(f"LRU cache content is: {self.cache}/n")


def main():
    l1 = LruCache(3)

    # add 4 items to cache
    l1.add_item(1).print()
    l1.add_item(2).print()
    l1.add_item(3).print()
    l1.add_item(4).print()

    # use 2 items to simulate the LRU behavior
    l1.use_item(2).print()
    l1.use_item(3).print()
    l1.use_item(2).print()

    # add even more items to the cache
    l1.add_item(5).print()
    l1.add_item(1).print()
    l1.add_item(2).print()


if __name__ == "__main__":
    main()

