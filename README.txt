Qifei (Kaylee) Zhao

All files have .py version and .ipynb version.
Below are some additional explanations about the code. Thank you so much for reviewing.

Question A
File name Question_A.ipynb & Question_A.ipynb

Question B
Library file: compare_versions.ipynb or compare_versions.py
Example test file: compare_versions_test.ipynb or compare_versions_test.py
Test files implement unit test. 
To run, type "python -m unittest compare_versions_test.py" in command prompt.

Question C
File name: Geo_LRU.ipynb
Overall design and functionalities missing:

1. A doubly linked list and a disctionary is used to store the items in cache.

2. Assume cache size and expire time are input arguments.

3. Geolocation is considered when adding expire time to each newly created node. 
Time are calculated by utcnow() such that all time could be in the same time zone. 
However, the time converted according to time zone would cause some difference on time, 
because of the different longitude inside a timezone.

4. There is supposed to be a lock on the get and set method of the LRU cache.
Reader and Writer lock was intended to be used, considering the similar requirement of method get and set.

5. To achieve data consistency across regions and ability to handle network failure or crashes, 
the map of nodes could be maintained in a database such as MongoDB. 
Also, singleton design pattern could be implemented to ensure there is only one copy of map exists.
However, with the requirement of local reference, there could be several copies exist, one for each region.
It was supposed to be modified in the code to achieve updating all copies of map when there is a new element added.
 


