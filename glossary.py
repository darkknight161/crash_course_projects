glossary = {
	'dictionary': "Defined with { }. a dictionary in Python is a "\
"collection of key-value pairs.  Each Key is connected to a Value, and you can"\
" use a key to access the value associated with that key.  A key's value can "\
"be a number, a string, a list, or even another dictionary.  You can use any "\
"object that you can create in Python as a value in a dictionary.",
'integers': 'Whole numbers, such as: 3 or 300',
'floating_point': 'Numbers with a decimal point: 2.3 or 4.6',
'strings': 'Ordered sequence of characters: "hello" or "Sammy"',
'lists': "Ordered squence of objects: [10, 'Sammy', 'candy']",
'tuples': "Ordered immutable sequence of objects: 910,'hello', 200.3)",
'sets': "Unordered collection of unique objects: ('a','b')",
'booleans': 'Logical value indicating True or False',
'variables': 'Defined with an "=".  A label for a value which can change.',
'.rstrip': 'Removes white space from the right side of a variable',
'.lstrip': 'Removes white space from the left side of a variable',
'.strip': 'Removes white space from both sides of a variable',
}

for term, definition in sorted(glossary.items()):
	print(f'\n{term.upper()}:')
	print(f'{definition}')