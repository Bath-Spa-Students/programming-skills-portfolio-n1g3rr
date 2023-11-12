# Glossary
programming_glossary = {
    'variable': 'A named storage location in computer memory that holds data.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.',
    'list': 'An ordered collection of items in Python.',
    'dictionary': 'A collection of key-value pairs in Python.'
}

# each word is printed with its meaninga and loop
for term, definition in programming_glossary.items():
    print(f"{term}:\n{definition}\n")


additional_terms = {
    'module': 'A file containing Python definitions and statements.',
    'class': 'A blueprint for creating objects in Python.',
    'method': 'A function that is associated with an object in Python.',
    'exception': 'An event that occurs during the execution of a program.',
    'syntax': 'The set of rules that dictate the combinations of symbols that are considered to be correctly structured programs in a given programming language.'
}


programming_glossary.update(additional_terms)

print("\nUpdated Glossary:")
for term, definition in programming_glossary.items():
    print(f"{term}:\n{definition}\n")
