"""
10.6 Sort Big File

Imagine you have a 20 GB file with one string per line. Explain how you
would sort the file.
"""

"""
Solution

Since the size limit is 20 GB, we don't want to bring all the data into
memory and only bring part of the data instead. 

We'll divide the file into chunks, which are x megabytes each, where x
is the amount of memory we have available. Each chunk is sorted separately
and then saved back to the file system.

Once all the chunks are sorted, we merge the chunks, one by one. At the
end, we have a fully sorted file. 

This algorithm is known as external sort. 
"""