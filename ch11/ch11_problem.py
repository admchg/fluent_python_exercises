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
        if len(data) != len(columns):
            raise RuntimeError("`data` and `columns` should be of the same length")

        self.column_val = dict(zip(columns, data))

    def __repr__(self):
        inside_text = [f"{col} : {val}" for col, val in self.column_val.items()]
        inside_string = ", ".join(inside_text)
        return f"Record[{inside_string}]"

    def __getitem__(self, column):
        return self.column_val[column]

    def __setitem__(self, column, value):
        self.column_val[column] = value

    def __delitem__(self, column):
        del self.column_val[column]

    # Add code


# Test 1.a
student = Record(
    columns=["Roll", "Name", "Subject", "Grade"],
    data=[1, "Hermoine", "Transformations", "A"],
)
assert student["Roll"] == 1
student["Grade"] = "B"
assert student["Grade"] == "B"
del student["Subject"]


# ---------------------------------
# What if we want to be able to retrieve the list of items in a Record
# 1.b Use Monkey Patching to make the following Test 1.b code work

# Add code

student.items = student.column_val.items

# Test 1.b
for column, value in student.items():
    print(f"{column}: {value}")

assert len(student.items()) == 3


# ---------------------------------
# 2. Since most of the operations we want to run on a Record match actions possible on a Mutable Mapping,
#    let's create a class 'RecordMapping' inheriting from collections.abc.MutableMapping


from collections.abc import MutableMapping


class RecordMapping(MutableMapping):
    def __init__(self, data, columns):
        if len(data) != len(columns):
            raise RuntimeError("`data` and `columns` should be of the same length")

        self.column_val = dict(zip(columns, data))

    def __repr__(self):
        inside_text = [f"{col} : {val}" for col, val in self.column_val.items()]
        inside_string = ", ".join(inside_text)
        return f"Record[{inside_string}]"

    def __getitem__(self, column):
        return self.column_val[column]

    def __setitem__(self, column, value):
        self.column_val[column] = value

    def __delitem__(self, column):
        del self.column_val[column]

    def __len__(self):
        return len(self.column_val)

    def __iter__(self):
        return iter(self.column_val)


# Test 2
student = RecordMapping(
    columns=["Roll", "Name", "Subject", "Grade"],
    data=[1, "Hermoine", "Transformations", "A"],
)
assert student["Roll"] == 1
student["Grade"] = "B"
assert student["Grade"] == "B"
del student["Subject"]

assert len(student.items()) == 3
