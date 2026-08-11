# Daily Log

## Day 1 - Repository Setup

### Completed
- Created the GitHub repository.
- Configured Git locally.
- Added README.
- Added .gitignore.
- Added requirements.txt.
- Created initial project structure.

### Learned
- Git init
- Git add
- Git commit
- Git push
- Basic repository structure

## Day 2

### Objective
Create the first functional version of the file organizer.

### Completed
- Created the application entry point.
- Validated the provided directory.
- Listed directory contents.

### Challenges
- Mistyped `iterdir()` as `interdir()`.
- Learned how to inspect methods from `pathlib.Path`.

### Learned
- pathlib.Path
- exists()
- iterdir()

### Next Steps
- Filter only files.
- Group files by extension.

## Day 3

### Objective

Refactor the file organizer to separate file discovery from the main program flow.

### Completed

- Created the `get_files()` helper function.
- Added file filtering using `Path.is_file()`.
- Updated the main program to use the new helper function.
- Tested the program with directories containing both files and subdirectories.

### Learned

- How to create and use helper functions in Python.
- How to iterate through directory contents using `Path.iterdir()`.
- The difference between files and directories using `Path.is_file()`.
- Basic separation of responsibilities between functions.

### Next Steps

- Refactor the main program flow.
- Improve handling of invalid paths.
- Begin categorizing files by extension.

## Day 4

### Objective

Improve directory validation and simplify the main program flow.

### Completed

- Refactored directory validation using early returns.
- Added validation to check whether the provided path exists.
- Added validation to check whether the provided path is a directory.
- Removed the large `if/else` block from the main program flow.
- Tested the application with valid directories, invalid paths, and file paths.

### Learned

- How early returns can simplify conditional logic.
- How to structure a function using guard clauses.
- The difference between validating a path and validating its type.

### Next Steps

- Improve user input handling.
- Start categorizing files by extension.
- Prepare the logic for creating destination folders.