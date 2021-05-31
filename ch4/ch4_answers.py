# # Chapter 4 Exercises
# By Tanmay

import locale
import chardet
import unicodedata
# ---------------------------------
# ## Problem 1
# a) Default Encoding: What's your system's default preferred encoding type? 
locale.getpreferredencoding()

# b) Chardet: Import chardet and run these exercises.

## 1. Consider two lines of a poem below. Use base .encode() without any arguments
## to encode them, then detect the encoding using chardet. 
## Do the encodings of the 2 lines differ? Why/why not?
## Now provide encoding UTF-8/UTF-16/CP1252 etc. as argument, is chardet 
## able to detect that correctly? What's the confidence?
line1 = 'Once upon a midnight dreary, while I pondered, weak and weary -'
line2 = 'Over many a quaint and curious volume of forgotten lore — '


print(chardet.detect(line1.encode()))
print(chardet.detect(line2.encode()))
print(chardet.detect(line2.encode(encoding = 'utf-8')))

# Learning - long dash isn't ascii; even after encoding utf8, chardet makes a mistake, though with less confidence

## 2. For the bytes provided below, make chardet guess the encoding.
b1 = b'\xff\xfe\x93\x03\xb5\x03\xb9\x03\xb1\x03 \x00\xc3\x03\xbf\x03\xc5\x03 \x00\xc0\x03\xce\x03\xc2\x03 \x00\xb5\x03\xaf\x03\xc3\x03\xb1\x03\xb9\x03;\x00' #Greek: Hey how are you doing?
b2 = b'Oh \xa4\xe4\xa4\xa2\xa1\xa2\xc4\xb4\xbb\xd2\xa4\xcf\xa4\xc9\xa4\xa6\xa4\xc7\xa4\xb9\xa4\xab\xa1\xa9' #Japanese: Oh hey how are you doing?
b3 = b'Oh \xe3\x82\x84\xe3\x81\x82\xe3\x80\x81\xe8\xaa\xbf\xe5\xad\x90\xe3\x81\xaf\xe3\x81\xa9\xe3\x81\x86\xe3\x81\xa7\xe3\x81\x99\xe3\x81\x8b\xef\xbc\x9f'

print(chardet.detect(b1)) # 
print(chardet.detect(b2)) # 'Oh やあ、調子はどうですか？'.encode('euc-jp')
print(chardet.detect(b3)) # 'Oh やあ、調子はどうですか？'.encode('utf-8')

print(b1.decode('utf-16'))
print(b2.decode('euc-jp'))
print(b3.decode('utf-8'))


# Try this: first 2 bytes of b2 are replaced by b3's. What does chardet detect?
b4 = b'Oh \xe3\x82\xa4\xa2\xa1\xa2\xc4\xb4\xbb\xd2\xa4\xcf\xa4\xc9\xa4\xa6\xa4\xc7\xa4\xb9\xa4\xab\xa1\xa9' #Japanese: Oh hey how are you doing?

# Try this: first 2 bytes of b3 are replaced by b2's. What does chardet detect?
b5 = b'Oh \xa4\xe4\x84\xe3\x81\x82\xe3\x80\x81\xe8\xaa\xbf\xe5\xad\x90\xe3\x81\xaf\xe3\x81\xa9\xe3\x81\x86\xe3\x81\xa7\xe3\x81\x99\xe3\x81\x8b\xef\xbc\x9f'

print(chardet.detect(b4)) # Cp1252
print(chardet.detect(b5)) # None


print(b4.decode('Cp1252'))
print(b5.decode())

# Learning - few byte changes maybe enough to screw up detection, maybe not; chardet bad at detecting languages (other recommended libs like lang_detect)
# Confirms what the text says - it's best to know encoding first-hand. Guessing is bad.

# ## Problem 2
# Unicode database
## Build a unicode meta database for the sample - print if each character is a 
## digit/numeric, it's unicode name, category name, and normalized form KD. (Refer Example 4-21)
## what do the various category and bidirectional codes stand for?

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285w\u0be7\u0bed\u0be8\u0bef'
for char in sample:
 print('U+%04x' % ord(char), 
 char.center(6), 
 'isdig' if char.isdigit() else '-', 
 'isnum' if char.isnumeric() else '-', 
 unicodedata.name(char), 
 unicodedata.category(char), 
 unicodedata.normalize('NFKD',char),
 unicodedata.bidirectional(char),
 sep='\t')


# ## Problem 3
# Brainstorm: The chapter showcased the use of text normalization (for 
# string comparison) and removal of diacritics for ASCII conversion. 
# When in our projects could these be useful?

# Code saving for Morocco

