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
        self._dict = dict(zip(columns, data))
        
    def __repr__(self):
        return 'Record(' + ', '.join("'{}': {}".format(k, v) for k, v in self._dict.items()) + ')'
                           
    def __getitem__(self, column):
        return self._dict[column]

    def __setitem__(self, column, update):
        self._dict[column] = update
        
    def __delitem__(self, column):
        del self._dict[column]


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
def items_patch(row):
    return list(row._dict.items())
Record.items = items_patch

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
        
        self._items = dict(zip(columns, data))
        
    def __repr__(self):
        return 'Record(' + ', '.join("'{}': {}".format(k, v) for k, v in self._items.items()) + ')'
                           
    def __getitem__(self, column):
        return self._items[column]
    
    def __setitem__(self, column, update):
        self._items[column] = update
        
    def __delitem__(self, column):
        del self._items[column]
        
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)


# Test 2
student =  RecordMapping(columns=['Roll', 'Name', 'Subject', 'Grade'], data=[1, 'Hermoine', 'Transformations', 'A'])
assert(student['Roll'] == 1)
student['Grade'] = 'B'
assert(student['Grade'] == 'B')
del student['Subject']

assert(len(student.items()) == 3)

