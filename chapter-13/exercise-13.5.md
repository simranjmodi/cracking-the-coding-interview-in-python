### 13.5 TreeMap, HashMap, LinkedHasMap

#### Explain the differences between TreeMap, HashMap, and LinkedHashMap. Provide an example of when each one would be best

**Solution**

All offer a key -> value map and a way to iterate through the keys. The most important
distinction between these classes is the time guarantees and the ordering of the keys.
- HashMap offers O(1) lookup and insertion. If you iterate through the keys, though,
the ordering of the keys is essentially arbitrary. It is implemented by an array of
liked lists. 
- TreeMap offers O(log N) lookup and insertion. Keys are ordered, so if you need to
iterate through the keys in sorted order, you can. This means that keys must implement
the Comparable interface. TreeMap is implemented by a Red-Black Tree. 
- LinkedHashMap offers O(1) lookup and insertion. Keys are ordered by their insertion
order. It is implemented by doubly-linked buckets. 

When might you need ordering in real life?
- Suppose you were creating a mapping of names to Person objects. You might want to
periodically output the people in alphabetical order by name. A TreeMap lets you do this.
- A TreeMap also offers a way to, given a name, output the next 10 people. This could also
be useful for a "More" function in many applications. 
- A LinkedHashMap is useful whenever you need the ordering of keys to match the ordering
of insertion. This might be useful in a caching situation, when you want to delete the oldest
item. 

Generally, unless there is a reason not to, you would use HashMap. That is, if you need to get
the keys back in insertion order, then use LinkedHashMap. If you need to get the keys back in 
their true/natural order, then use TreeMap. Otherwise, HashMap is probably best. It is typically
faster and requires less overhead. 