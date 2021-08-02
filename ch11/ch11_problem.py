# Chapter 11

# ---------------------------------
# 1.a. Create a class 'Record' meeting the following requirements:
#      Initialize new record using: new_record = Record(columns=[col1, col2 ..], data=[val1, val2 ..])
#      print(new_record) gives: Record[col 1: value 1, col 2: value 2 ..] 
#      Select a column value: new_record[<column name>] 
#      Update a column value: new_record[<column name>] = <new value>
#      Delete a column: del new_record[<column name>]


class Record:
    
    def __init__(self, data, columns):

    # Add code
    

# Test 1.a
student =  Record(columns=['Roll', 'Name', 'Subject', 'Grade'], data=[1, 'Hermoine', 'Transformations', 'A'])
assert(student['Roll'] == 1)
student['Grade'] = 'B'
assert(student['Grade'] == 'B')
del student['Subject']
    


# ---------------------------------
# What if we want to be able to retrieve the list of items in a Record
# 1.b Use Monkey Patching to make the following Test 1.b code work

# Add code


# Test 1.b
for column, value in student.items():
    print(f'{column}: {value}')

assert(len(student.items()) == 3)


# ---------------------------------
# 2. Since most of the operations we want to run on a Record match actions possible on a Mutable Mapping, 
#    let's create a class 'RecordMapping' inheriting from collections.abc.MutableMapping 


from collections.abc import MutableMapping

class RecordMapping(MutableMapping):

    def __init__(self, data, columns):

	# Add code


# Test 2
student =  RecordMapping(columns=['Roll', 'Name', 'Subject', 'Grade'], data=[1, 'Hermoine', 'Transformations', 'A'])
assert(student['Roll'] == 1)
student['Grade'] = 'B'
assert(student['Grade'] == 'B')
del student['Subject']

assert(len(student.items()) == 3)

