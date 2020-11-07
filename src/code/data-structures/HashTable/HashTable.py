""" This file will contains different hashtable implementations """

# HashTable separate chaining


from typing import Final, final
from abc import ABC, abstractmethod


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


""" Defining abstract class for all the open addressing technique """


class HashTableOpenAddressingBase(ABC):
    # Special marker token used to indicate the deletion of a key-value pair

    TOMBSTONE: Final = object()

    __DEFAULT_CAPACITY: Final = 7
    __DEFAULT_LOAD_FACTOR: Final = 0.65

    def __init__(self, capacity=None, load_factor=None):
        if capacity and capacity < 0:
            raise ValueError('Capacity cannot be less than 0')
        if load_factor and (load_factor <= 0 or load_factor == float('inf') or not isinstance(load_factor, (float))):
            raise ValueError('Invalid load_factor')
        self._load_factor = HashTableOpenAddressingBase.__DEFAULT_LOAD_FACTOR
        if load_factor:
            self._load_factor = max(
                load_factor, HashTableOpenAddressingBase.__DEFAULT_LOAD_FACTOR)
        self._capacity = HashTableOpenAddressingBase.__DEFAULT_CAPACITY
        if capacity:
            self._capacity = max(
                capacity, HashTableOpenAddressingBase.__DEFAULT_CAPACITY)
        self._adjust_capacity()
        self._threshold = int(self._capacity * self._load_factor)

        # These will be lists store the key-value pairs.
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity

        # '_used_buckets' counts the total number of used buckets inside the
        # hash-table (includes cells marked as deleted). While '_key_count'
        # tracks the number of unique keys currently inside the hash-table.
        self._used_buckets = 0
        self._key_count = 0
        self._modification_count = 0

    # These three methods are used to dictate how the probing is to actually
    # occur for whatever open addressing scheme you are implementing.

    @abstractmethod
    def _setup_probing(self, key):
        pass

    @abstractmethod
    def _probe(self, x):
        pass

    # Adjusts the capacity of the hash table after it's been made larger.
    # This is important to be able to override because the size of the hashtable
    # controls the functionality of the probing function.
    @abstractmethod
    def _adjust_capacity(self):
        pass

    # Increases the capacity of the hash table
    def _increase_capacity(self):
        self._capacity = (2 * self._capacity) + 1

    def clear(self):
        for i in range(0, self._capacity):
            self._keys[i] = None
            self._values[i] = None

        self._key_count = self._used_buckets = 0
        self._modification_count += 1

    # Returns the number of keys currently inside the hash-table
    def size(self):
        return self._key_count

    # Returns the capacity of the hashtable (used mostly for testing)
    def get_capacity(self):
        return self._capacity

    # Returns true/false depending on whether the hash-table is empty
    def is_empty(self):
        return self._key_count == 0

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    # Returns true/false on whether a given key exists within the hash-table.
    def contains_key(self, key):
        return self.has_key_(key)

    # Returns a list of keys found in the hash table
    def keys(self):
        hashtable_keys = []
        for i in range(0, self._capacity):
            if self._keys[i] and self._keys[i] != HashTableOpenAddressingBase.TOMBSTONE:
                hashtable_keys.append(self._keys[i])
        return hashtable_keys

    # Returns a list of non-unique values found in the hash table
    def values(self):
        hashtable_values = []
        for i in range(0, self._capacity):
            if self._keys[i] and self._keys[i] != HashTableOpenAddressingBase.TOMBSTONE:
                hashtable_values.append(self._values[i])
        return hashtable_values

    # Double the size of the hash table
    def _resize_table(self):
        self._increase_capacity()
        self._adjust_capacity()

        self._threshold = (self._capacity * self._load_factor)
        old_key_table = [None] * self._capacity
        old_value_table = [None] * self._capacity

        # Perform key table pointer swap
        key_table_tmp = self._keys
        self._keys = old_key_table
        old_key_table = key_table_tmp

        # Perform value table pointer swap
        value_table_tmp = self._values
        self._values = old_value_table
        old_value_table = value_table_tmp

        # Reset the key count and buckets used since we are about to
        # re-insert all the keys into the hash-table.
        self._key_count = self._used_buckets = 0

        for i in range(0, len(old_key_table)):
            if old_key_table[i] and old_key_table[i] != HashTableOpenAddressingBase.TOMBSTONE:
                self.insert(old_key_table[i], old_value_table[i])
                old_key_table[i] = None
                old_value_table[i] = None

    # Converts a hash value to an index. Essentially, this strips the
    # negative sign and places the hash value in the domain [0, capacity)
    @final
    def _normalize_index(self, key_hash):
        return (key_hash & 0x7FFFFFFF) % self._capacity

    @classmethod
    def _gcd(cls, a, b):
        if b == 0:
            return a
        return HashTableOpenAddressingBase._gcd(b, a % b)

    # Place a key-value pair into the hash-table. If the value already
    # exists inside the hash-table then the value is updated.
    def insert(self, key, val):
        if key is None:
            raise ValueError('key cannot be None')
        if self._used_buckets >= self._threshold:
            self._resize_table()

        self._setup_probing(key)
        offset: Final = self._normalize_index(hash(key))

        i = offset
        j = -1
        x = 1
        while True:
            if self._keys[i] == HashTableOpenAddressingBase.TOMBSTONE:
                if j == -1:
                    j = i
            # The current cell already contains a key
            elif self._keys[i] is not None:
                # The key we're trying to insert already exists in the hash-table,
                # so update its value with the most recent value
                if self._keys[i] == key:
                    old_value = self._values[i]
                    if j == -1:
                        self._values[i] = val
                    else:
                        self._keys[i] = HashTableOpenAddressingBase.TOMBSTONE
                        self._values[i] = None
                        self._keys[j] = key
                        self._values[j] = val
                    self._modification_count += 1
                    return old_value
            # Current cell is none so an insertion/update can occur
            else:
                # No previously encountered delete buckets
                if j == -1:
                    self._used_buckets += 1
                    self._key_count += 1
                    self._keys[i] = key
                    self._values[i] = val
                # Previously seen deleted bucket. Instead of inserting
                # the new element at i where the None element is insert
                # it where the deleted token was found.
                else:
                    self._key_count += 1
                    self._keys[j] = key
                    self._values[j] = val
                self._modification_count += 1
                return None
            x += 1
            i = self._normalize_index(offset + self._probe(x))

    #  Returns true/false on whether a given key exists within the hash-table
    def has_key_(self, key):
        if key is None:
            raise ValueError('key cannot be None')

        self._setup_probing(key)
        offset: Final = self._normalize_index(hash(key))
        # Start at the original hash value and probe until we find a spot where our key
        # is or hit a None element in which case our element does not exist.
        i = offset
        j = -1
        x = 1
        while True:
            # Ignore deleted cells, but record where the first index
            # of a deleted cell is found to perform lazy relocation later.
            if self._keys[i] == HashTableOpenAddressingBase.TOMBSTONE:
                if j == -1:
                    j = 1
            elif self._keys[i] is not None:
                if self._keys[i] == key:
                    # If j != -1 this means we previously encountered a deleted cell.
                    # We can perform an optimization by swapping the entries in cells
                    # i and j so that the next time we search for this key it will be
                    # found faster. This is called lazy deletion/relocation.
                    if j != -1:
                        # Swap the key-value pairs of positions i and j.
                        self._keys[j] = self._keys[i]
                        self._values[j] = self._values[i]
                        self._keys[i] = HashTableOpenAddressingBase.TOMBSTONE
                        self._values[i] = None
                    return True
                else:
                    return False
            x += 1
            i = self._normalize_index(offset + self._probe(x))

    #  Get the value associated with the input key.
    #  NOTE: returns None if the value is None AND also returns
    #  None if the key does not exists.
    def get(self, key):
        if key is None:
            raise ValueError('Key cannot be None')

        self._setup_probing(key)
        offset: Final = self._normalize_index(hash(key))
        # Start at the original hash value and probe until we find a spot where our key
        # is or we hit a null element in which case our element does not exist.
        i = offset
        j = -1
        x = 1
        while True:
            # Ignore deleted cells, but record where the first index
            # of a deleted cell is found to perform lazy relocation later.
            if self._keys[i] == HashTableOpenAddressingBase.TOMBSTONE:
                if j == -1:
                    j = i
            # We hit a non-null key, perhaps it's the one we're looking for.
            elif self._keys[i] is not None:
                # The key we want is in the hash-table!
                if self._keys[i] == key:
                    # If j != -1 this means we previously encountered a deleted cell.
                    # We can perform an optimization by swapping the entries in cells
                    # i and j so that the next time we search for this key it will be
                    # found faster. This is called lazy deletion/relocation.
                    if j != -1:
                        # Swap key-values pairs at indexes i and j
                        self._keys[j] = self._keys[i]
                        self._values[j] = self.values[j]
                        self._keys[i] = HashTableOpenAddressingBase.TOMBSTONE
                        self._values[i] = None
                        return self._values[j]
                    else:
                        return self._values[i]
            # Element was not found in the hash-table
            else:
                return None
            x += 1
            i = self._normalize_index(offset + self._probe(x))

    # Removes a key from the map and returns the value.
    # NOTE: returns null if the value is null AND also returns
    # null if the key does not exists.
    def remove(self, key):
        if key is None:
            raise ValueError('Key cannot be None')

        self._setup_probing(key)
        offset: Final = self._normalize_index(hash(key))

        # Starting at the original hash probe until we find a spot where our key is
        # or we hit a null element in which case our element does not exist.
        i = offset
        x = 1
        while True:
            x += 1
            i = self._normalize_index(offset + self._probe(x))

            # Ignore deleted cells
            if self._keys[i] == HashTableOpenAddressingBase.TOMBSTONE:
                continue

            # If key was not found in hash-table
            if self._keys[i] is None:
                return None

            # The key we want to remove is in the hash-table!
            if self._keys[i] == key:
                self._key_count -= 1
                self._modification_count += 1
                old_value = self._values[i]
                self._keys[i] = HashTableOpenAddressingBase.TOMBSTONE
                self._values[i] = None
                return old_value

    # Return a string view of this hash-table
    def __repr__(self):
        st = ""
        st += "{ "
        for i in range(0, self._capacity):
            if self._keys[i] is not None and self._keys[i] != HashTableOpenAddressingBase.TOMBSTONE:
                st += str(self._keys[i]) + "=>" + str(self._values[i]) + ", "
        st += " }"
        return st


# Linear Probing
class HashTableLinearProbing(HashTableOpenAddressingBase):
    # This is the linear constant used in the linear probing, it can be
    # any positive number. The table capacity will be adjusted so that
    # the GCD(capacity, LINEAR_CONSTANT) = 1 so that all buckets can be probed.
    LINEAR_CONSTANT: Final = 17

    def __init__(self, capacity, load_factor):
        super().__init__(capacity=capacity, load_factor=load_factor)

    def _setup_probing(self, key):
        pass

    def _probe(self, x):
        return HashTableLinearProbing.LINEAR_CONSTANT * x

    # Adjust the capacity so that the linear constant and
    # the table capacity are relatively prime.
    def _adjust_capacity(self):
        while HashTableLinearProbing._gcd(HashTableLinearProbing.LINEAR_CONSTANT, self._capacity) != 1:
            self._capacity += 1
