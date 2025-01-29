
    Vowel eater "vowel_eater"s
    Is year a common Year or Leap "check_year"
    
1. Factorial calculator using funtion 
2. ASCII Art Encoding
3. Converting Hexadecimal to Decimal
4. Find prime number
5. Send message receive it save in a list (exceptions)
6. File compression (Read file compress it and save it in new soller size file).
7. Fibonace using recursion
8. Book store using class 
9. Working with files on Python
10. Display file in directory
11. Create a forder
12. Count files on directory 
13. Work with PDF files
14. Move, rename,delte,copy File and directories
15. Json files
16. CSV Files
17. Rename photo
18. Read file and encript it
19. 



sys.argv - this variable is a list of command-line arguments passed to a python script
sys.path - this variable is a list of strings that specifies the search path for modules.
sys.version - is a string containing the Python version number and compiler information.
sys.version_info - is a named tuple containing the same information as integers
sys.platform - this variable provides information about the platform where Python is running
sys.stdin - is used for all interactive input
sys.stdout - is used for te output
sys.stderr - standar error streams


File and Directory Operations:
os.getcwd() - returns the current working directory as a string.
os.chdir(path) - changes the current working directory to the specified path.
os.listdir(path='.') - returns a list of the names of the files and directories in the specified directory.
os.mkdir(path) - creates a directory. 
os.remove(path) - removes a file.
os.rmdir(path) - removes an empty directory.
os.rename(src, dst) - renames a file or directory.

Path manipulation:
os.path.join(path1, path2, …) - joins one or more path components intelligently.
os.path.abspath(path) - returns the absolute path of a given path.
os.path.exists(path) - checks if a file or directory exists.
os.path.isfile(path) - checks if a path points to a file
os.path.isdir(path) -  checks if a path points to a directory.

Process Management:
os.system(command) - executes the command in a subshell (not recommended for security reasons).
os.spawnv(mode, path, args) - spawns a new process
os.kill(pid, sig) - ends a signal to the process identified by pid.

Environment Variables:
os.environ - a mapping object representing the environment variables. 
os.getenv(key, default=None) - gets the value of the environment variable key, or default if the variable is not found.

Other functions:
os.name() -  provides the name of the operating system dependent module imported. Typically 'posix' (Unix-like systems) or 'nt' (Windows).
os.getlogin() -  returns the name of the user logged in on the controlling terminal of the process.


    pathlib
Overview of the main classes and functions provided by the pathlib module:
Path class:
    The Path class represents a filesystem path. It provides various methods for working with paths, such as joining paths, resolving absolute paths, checking file existence, creating directories, and more.
Constructing Path objects:
    You can create a Path object using the Path() constructor and passing the path as a string, or by using Path literals (introduced in Python 3.6).
Accessing path components:
    The Path object provides attributes and methods for accessing different components of the path, such as the file name, parent directory, file suffix, and more.
Path manipulation:
    The Path object provides methods for manipulating paths, such as joining paths (Path.joinpath()), resolving absolute paths (Path.resolve()), getting the parent directory (Path.parent), getting the file name (Path.name), and more.
File and directory operations:
    The Path object provides methods for performing file and directory operations, such as checking existence (Path.exists()), checking whether it's a file or directory (Path.is_file(), Path.is_dir()), creating directories (Path.mkdir()), and more.


In Python, the CSV (Comma-Separated Values) module provides functionality for working with CSV files. CSV files are commonly used for storing tabular data, where each row represents a record and each column represents a field or attribute.
CSV functions:
    csv.reader - return a reader object that will process lines from the given csvfile. A csvfile must be an iterable of strings, each in the reader’s defined csv format.
    csv.writer - return a writer object responsible for converting the user’s data into delimited strings on the given file-like object. csvfile can be any object with a write() method
    class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds) - create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
    class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds) - create an object which operates like a regular writer but maps dictionaries onto output rows.

json
In Python, you can work with JSON using the json module, which provides functions for encoding Python objects into JSON strings and decoding JSON strings into Python objects.

Basic overview example of how to work with JSON in Python using the json module:
Encoding Python objects into JSON: 
json.dump - serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.
json.dumps - serialize obj to a JSON formatted str using this conversion table. The arguments have the same meaning as in dump().

Decoding Python objects into JSON: 
json.load - deserialize fp (a .read()-supporting text file or binary file containing a JSON document) to a  Python object using this conversion table.
json.loads - deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python  object using this conversion table.

    xml
Python’s interfaces for processing XML are grouped in the xml package.
Warning: The XML modules are not secure against erroneous or maliciously constructed data. If you need to parse untrusted or unauthenticated data see the XML vulnerabilities and The defusedxml Package sections.
    It is important to note that modules in the xml package require that there be at least one SAX-compliant XML parser available. The Expat parser is included with Python, so the xml.parsers.expat module will always be available.
xml.etree.ElementTree - the ElementTree API, a simple and lightweight XML processor
xml.dom - the DOM API definition
xml.dom.minidom: a minimal DOM implementation
xml.dom.pulldom - support for building partial DOM trees
xml.sax - SAX2 base classes and convenience functions
xml.parsers.expat - the Expat parser binding

datetime
The datetime module supplies classes for manipulating dates and times.
While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.

Available types:
datetime.date - an idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Attributes: year, month, and day.
datetime.time - an idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. (There is no notion of “leap seconds” here.) Attributes: hour, minute, second, microsecond, and tzinfo.
datetime.datetime - a combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo. 
datetime.timedelta -  a duration expressing the difference between two datetime or date instances to microsecond resolution.




time
This module provides various time-related functions. In Python, you can work with time-related functions using the time module. This module provides functions for working with time expressed in seconds since the epoch.
The time module also provides additional functionality for working with struct_time objects, converting between time formats, and more, allowing you to perform various operations involving time in your Python programs.
Functions:
time.sleep(secs) - suspend execution of the calling thread for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.
time.strptime(string[, format]) - parse a string representing a time according to a format. The return value is a struct_time as returned by gmtime() or localtime().
time.strftime(format[, t]) - convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
time.time() -> float  - return the time in seconds since the epoch as a floating point number.
time.asctime([t])   - convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string of the following form: 'Sun Jun 20 23:21:05 1993'. 
time.clock_gettime(clk_id) → float  - return the time of the specified clock clk_id. Refer to Clock ID Constants for a list of accepted values for clk_id.


re
The re module provides support for working with regular expressions, which are powerful tools for matching and  manipulating text patterns. Regular expressions are used to search, extract, and manipulate strings based on patterns. 
Regular expressions can be concatenated to form new regular expressions;
re.search(pattern, string, flags=0)- scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding Match.
re.match(pattern, string, flags=0) - if zero or more characters at the beginning of string match the regular expression pattern, return a corresponding Match. 
re.fullmatch(pattern, string, flags=0) - if the whole string matches the regular expression pattern, return a corresponding Match. 
re.split(pattern, string, maxsplit=0, flags=0) - Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. 


math
This module provides access to the mathematical functions defined by the C standard. These functions cannot be used with complex numbers; use the functions of the same name from the cmath module if you require support for complex numbers. 
math.ceil(x) - return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x.__ceil__, which should return an Integral value.
math.comb(n, k) - return the number of ways to choose k items from n items without repetition and without order.
math.copysign(x, y) - return a float with the magnitude (absolute value) of x but the sign of y. On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.
math.floor(x)- return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__, which should return an Integral value.


random 
In Python, the random module provides functions for generating pseudo-random numbers. These functions are  useful for tasks such as generating random numbers, shuffling sequences, and selecting random elements from sequences. 
random.seed() - initialize the random number generator.
random.getstate() - return an object capturing the current internal state of the generator. This object can be passed to setstate() to restore the state.
random.setstate(state) - state should have been obtained from a previous call to getstate(), and setstate() restores the internal state of the generator to what it was at the time getstate() was called.
random.random() - return the next random floating point number in the range 0.0 <= X < 1.0

Iterators
This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method using the next() built-in function;


Generators and generator functions
Generator functions is a function or method which uses the yield statement.
Generator iterator is an iterator object created by a generator function.
Generator expression is an expression that returns an iterator.
Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).



