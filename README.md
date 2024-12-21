# advent-of-code-2024
### My advent of code solutions.
Written in python using procedural programming.

# Running

All programs by default run using my input for the solution. To change the input change the file name at the beginning of the program or edit the input.txt/inputs.txt text file in the directory.

Solutions will be printed to the console.

Each directory contains all the code for the named day.

Instructions for running part 1 and part 2 for each day:

| Day | Part 1                                                                                                                                         | Part 2                                                                                                 |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
|  1  | Run totalDistanceCalculator.py.                                                                                                                | Run similarityScoreCalculator.py.                                                                      |
|  2  | Run reportChecker.py with the ```PROBLEM_DAMPENER_ENABLED``` flag set to ```False```.                                                              | Run reportChecker.py with the ```PROBLEM_DAMPENER_ENABLED``` flag set to ```True```.                       |
|  3  | Comment out or remove the ```do``` and ```don't``` instructions from ```getInstructions()``` in ```memory.py``` and run multiplactionAdder.py. | Run multiplicationAdder.py (revert part 1 instrutions if done).                                        |
|  4  | Run wordSearchSolver.py with ```SELECTED_PUZZLE_TYPE``` set to ```PUZZLE_TYPES[0]``` (XMAS).                                                   | Run wordSearchSolver.py with ```SELECTED_PUZZLE_TYPE``` set to ```PUZZLE_TYPES[1]``` (X-MAS).          |
|  5  | Run updateValidator.py with ```SELECTED_MODE``` set to ```MODE[0]``` (GET VALID UPDATES).                                                      | Run updateValidator.py with ```SELECTED_MODE``` set to ```MODE[1]``` (CORRECT INVALID UPDATES).        |
|  6  | Run guardPredictor.py with ```SELECTED_MODE``` set to ```MODE[0]``` (COUNT).                                                                   | Run guardPredictor.py with ```SELECTED_MODE``` set to ```MODE[1]``` (LOOPS). Warning: takes a while.   |

# Rules I made for myself
1. All programs have to be written in python using the procedural programming paradigm.
2. To start a day, each day before it must be fully solved (to fit the story).
3. The solution to a part must be printed to the console and the only thing printed to the console.
4. Part 2 should not overwrite part 1, it should either extend on part 1 code or be written in a separate file.
5. All programs should allow for running both parts and there should be an easy way to switch parts if they are in the same file.