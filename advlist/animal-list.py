#!/usr/bin/env python3

# create a list called list1
list1 = ["Fox", "Fly", "Ant"]
# create a list called list2
list2 = ["Bee", "Cod", "Cat", "Dog"]
# create a list called list3
list3 = ["Yak", "Cow", "Hen", "Koy"]
# create a list called list4
list4 = ["Hog", "Jay", "Kit"]
# use the append operation to append list1 by list3
list1.extend(list2)
list1.extend(list3)
list1.extend(list4)
# display list1
print(list1)
