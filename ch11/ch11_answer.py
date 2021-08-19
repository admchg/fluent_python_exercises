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
        self.cols = columns
        self.data = data
        
    def __getitem__(self, indic):
        if indic in self.cols:
            indic = self.cols.index(indic)
        return self.data[indic]
        
    def __setitem__(self, pos, val):
        self.data[self.cols.index(pos)] = val
        
    def __delitem__(self, pos):
        del self.data[self.cols.index(pos)]
        del self.cols[self.cols.index(pos)]
    
    def __iter__(self):
        return (i for i in (self.cols, self.data))
    
    def __len__(self):
        return len(self.cols)
    
    def __repr__(self):
        return "Record({})".format({self.cols[i]: self.data[i] for i in range(len(self.cols))})

# Test 1.a
student =  Record(columns=['Roll', 'Name', 'Subject', 'Grade'], data=[1, 'Hermoine', 'Transformations', 'A'])
student
assert(student['Roll'] == 1)
student['Grade'] = 'B'
assert(student['Grade'] == 'B')

del student['Subject']
student
    


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
        self.dict = {columns[i]: data[i] for i in range(len(columns))}
        
    def __getitem__(self, indic):
        return self.dict[indic]
        
    def __setitem__(self, pos, val):
        self.dict[pos] = val
        
    def __delitem__(self, pos):
        del self.dict[pos]
   
    def __iter__(self):
        return (i for i in (self.dict.keys(), self.dict.values()))
    
    def __len__(self):
        return len(self.dict)
    
    def __repr__(self):
        return "Record({})".format(self.dict)

	# Add code


# Test 2
student =  RecordMapping(columns=['Roll', 'Name', 'Subject', 'Grade'], data=[1, 'Hermoine', 'Transformations', 'A'])
assert(student['Roll'] == 1)
student['Grade'] = 'B'
assert(student['Grade'] == 'B')
del student['Subject']
student
assert(len(student.items()) == 3)

