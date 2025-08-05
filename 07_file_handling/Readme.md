# File Handling in Python

File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

## Why do we need File Handling

- To store data permanently, even after the program ends.
- To access external files like .txt, .csv, .json, etc.
- To process large files efficiently without using much memory.
- To automate tasks like reading configs or saving outputs.
- To handle input/output in real-world applications and tools.

## Opening a File in Python

file = open('filename.txt', 'mode')

- filename.txt: name (or path) of the file to be opened.
- mode: mode in which we want to open the file (read, write, append, etc.).

Note: If we don’t specify the mode, Python uses 'r' (read mode) by default.

## Closing a File

It's important to close the file after you're done using it. file.close() method closes the file and releases the system resources ensuring that changes are saved properly (in case of writing)

```python
file.close()
```

## Checking File Properties

Once the file is open, we can check some of its properties:

```python
f = open("demo.txt", "r")

print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)
```

## File Modes in Python

When working with files in Python, the file mode tells Python what kind of operations (read, write, etc.) you want to perform on the file. You specify the mode as the second argument to the open() function.

### Different File Mode in Python

- ‘r’ : Read-only. Raises I/O error if file doesn't exist.
- w’ : Write-only. Overwrites file if it exists, else creates a new one.
- ‘a’ : Append-only. Adds data to end. Creates file if it doesn't exist.
- 'b' : binary mode. Used for non-text files like images or audio. Always combined with 'r', 'w', or 'a
- 'r+' : Opens the file for both reading and writing. Starts at the beginning of the file. Raises FileNotFoundError if the file doesn’t exist.
- 'w+' : This mode allows you to open a file for both reading and writing. If the file already exists, it will truncate the file to zero length. If the file does not exist, it will create a new file.
- 't' : text mode . By default it is text mode

## Reading a File

Reading a file can be achieved by file.read() which reads the entire content of the file. After reading the file we can close the file using file.close() which closes the file after reading it, which is necessary to free up system resources.

```python
file = open("geeks.txt", "r")
content = file.read()
print(content)

file.close()
```

### Using with Statement

Instead of manually opening and closing the file, you can use the with statement, which automatically handles closing. This reduces the risk of file corruption and resource leakage.

```python
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

```

### Handling Exceptions When Closing a File

```python
try:
    file = open("demo.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
```

## Writing to a file

```python
f=open('demo.txt','w')
f.write("this is some text") # this overwrites the entire content of the file

```

using append mode

```python
f=open('demo.txt','a')
f.write("\nthis text will be added to the end of the file") # this is addes
```

## Deleting a file

Using the OS module

module is a file written by another programmer that generally has a funtion we can use

```python
 import os
 os.remove(filenme)
```

## Notes

### Cursor

In Python file handling, the "cursor" (also known as the "file pointer" or "file handle") refers to the current position within an open file where the next read or write operation will occur.

#### Key aspects of the file cursor:

- Tracking Position:
  The cursor keeps track of where you are in the file. When you open a file, the cursor is initially at the beginning (position 0).

- Read/Write Operations:
  When you read from a file, the cursor moves forward by the number of characters or bytes read. Similarly, when you write to a file, the cursor moves forward as data is written.

- seek() method:
  This method allows you to explicitly move the cursor to a specific position within the file. You can specify an offset and a reference point (beginning, current position, or end of the file).

- tell() method:
  This method returns the current position of the cursor (in bytes) from the beginning of the file.

````python
# Open a file in read mode
with open("example.txt", "r") as f:
    print(f"Initial cursor position: {f.tell()}")  # Output: 0

    # Read a few characters
    content = f.read(5)
    print(f"Content read: {content}")
    print(f"Cursor position after reading: {f.tell()}")

    # Move the cursor to a specific position
    f.seek(0)
    print(f"Cursor position after seeking to beginning: {f.tell()}")

    # Read again from the beginning
    content_again = f.read(5)
    print(f"Content read again: {content_again}")

    ```
````
