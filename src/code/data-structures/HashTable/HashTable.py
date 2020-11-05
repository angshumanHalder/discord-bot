""" This file will contains different hashtable implementations """

# HashTable separate chaining


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash_code = hash(key)

    def equals(self, other):
        if self.hash != other.hash:
            return False
        return self.key == other.key

    def __repr__(self):
        return str(self.key) + " : " + str(self.value)


class HashTableSeparateChaining:
    DEFAULT_CAPACITY = 3
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, capacity=None, max_load_factor=None):
        if capacity and capacity < 0:
            raise ValueError('Capacity cannot be less than 0')
        if max_load_factor and (max_load_factor <= 0 or max_load_factor == float('inf') or not max_load_factor.isnumeric()):
            raise ValueError('Invalid max_load_factor')

        self.__max_load_factor = HashTableSeparateChaining.DEFAULT_LOAD_FACTOR
        if max_load_factor:
            self.__max_load_factor = max(
                max_load_factor, HashTableSeparateChaining.DEFAULT_LOAD_FACTOR)

        self.__capacity = HashTableSeparateChaining.DEFAULT_CAPACITY
        if capacity:
            self.__capacity = max(
                HashTableSeparateChaining.DEFAULT_CAPACITY, capacity)
        self.__threshold = int(self.__capacity * self.__max_load_factor)
        self.__table = [None] * self.__capacity
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __normalize_index(self, keyHash):
        return (keyHash & 0x7FFFFFFF) % self.__capacity

    def clear(self):
        self.table = [None] * self.__capacity
        self.size = 0

    def contains_key(self, key):
        return self.__has_key(key)

    def __has_key(self, key):
        bucket_idx = self.__normalize_index(hash(key))
        return self.__bucket_seek_entry(bucket_idx, key) is not None

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if key is None:
            raise ValueError('key cannot be None')
        entry = Entry(key, value)
        bucket_idx = self.__normalize_index(entry.hash_code)
        return self.__bucket_insert_entry(bucket_idx, entry)

    def get(self, key):
        if key is None:
            return None
        bucket_idx = self.__normalize_index(hash(key))
        entry = self.__bucket_seek_entry(bucket_idx, key)
        if entry:
            return entry.value
        return None

    def remove(self, key):
        if key is None:
            return None
        bucket_idx = self.__normalize_index(hash(key))
        return self.__bucket_remove_entry(bucket_idx, key)

    def __bucket_remove_entry(self, bucket_idx, key):
        entry = self.__bucket_seek_entry(bucket_idx, key)
        if entry:
            links = self.__table[bucket_idx]
            links.remove(entry)
            self.__size -= 1
            return entry
        return None

    def __bucket_insert_entry(self, bucket_idx, entry):
        bucket = self.__table[bucket_idx]
        if bucket is None:
            self.__table[bucket_idx] = bucket = []
        existent_entry = self.__bucket_seek_entry(bucket_idx, entry.key)
        if existent_entry is None:
            bucket.append(entry)
            self.__size += 1
            if self.__size > self.__threshold:
                self.__resize_table()
            return None
        else:
            old_val = existent_entry.value
            existent_entry.value = entry.value
            return old_val

    def __bucket_seek_entry(self, bucket_idx, key):
        if key is None:
            return None
        bucket = self.__table[bucket_idx]
        if bucket is None:
            return None
        for entry in bucket:
            if entry.key == key:
                return entry
        return None

    def __resize_table(self):
        self.__capacity *= 2
        self.__threshold = int(self.__capacity * self.__max_load_factor)
        new_table = [None] * self.__capacity
        for i in range(0, len(self.__table)):
            if self.__table[i]:
                for entry in self.__table[i]:
                    bucket_idx = self.__normalize_index(entry.hash_code)
                    bucket = new_table[bucket_idx]
                    if bucket is None:
                        new_table[bucket_idx] = bucket = []
                    bucket.append(entry)
                self.__table[i].clear()
                self.__table[i] = None
        self.__table = new_table

    def keys(self):
        keys = []
        for bucket in self.__table:
            if bucket:
                for entry in bucket:
                    keys.append(entry.key)
        return keys

    def values(self):
        values = []
        for bucket in self.__table:
            if bucket:
                for entry in bucket:
                    values.append(entry.value)
        return values

    def __repr__(self):
        st = ""
        st += "{ "
        for i in range(0, self.__capacity):
            if self.__table[i] is None:
                continue
            for entry in self.__table[i]:
                st += entry + ", "
        st += " }"
        return st
