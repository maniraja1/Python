'''
    Abstract data type Associative arrays (ASA) defines how Hashtables/Maps/Dictionaries should behave
    ASA should be able to Add, remove, update and lookup a key value pair

Motivation for Hash table
    In an array if we know the index then insert and read operation can be performed in O(1) time complexity
    If we can hash a key and use that as an array index then every time we read we can do this with O(1) complexity
    you will have to address hash collisions by implementing
        chaining, use linked list
        open addressing.
            find the next open slot
            rehashing, hash the result again to find an open slot
            linear & quadratic probing
    You need to handle dynamic resizing as the array gets full.
    Load factor  is a term used to estimate how full the array is.
    LF of 0 means array is empty. LF of 1 means array is full.
    if the array is close to being full then there will be more collisions and insert operations will get slower.
    If the array has lot of empty slots the space complexity is compromised but time complexity is improved
    There will always be this trade off between space and time complexity when designing Hash tables.
    Java when LF is 0.75 array is dynamically resized
    python when LF is 0.67 array is dynamically resized
    when table is resized you cannot just copy values from one array to another. This is because hash value depends on
    array size. Resizing takes O(n) time complexity so its an expensive operation and may not be ideal for real
    world applications


Complexity
    insert = O(1)
    delete = O(1)
    lookup = O(1)
    Resizing = O(n)


'''