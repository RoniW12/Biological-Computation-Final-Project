# Biological-Computation-Final-Project
## Monotonic Boolean Function Calculation

This project develops a program to identify 18 monotonic Boolean functions related to gene regulation. It generates all possible Boolean functions based on activator and repressor states, then filters them to ensure monotonicity. The program confirms the functions' adherence to biological constraints and outputs the valid ones.

### Requirements

To run this program, you will need:

- Python 3.x

### How to Run the Program

1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the URL of your GitHub repository.

2. **Navigate to the Project Directory**:
   ```
   cd <repository-directory>
   ```
   Replace `<repository-directory>` with the directory name where your project is located.

3. **Run the Program**:
   ```
   python monotonic_functions.py
   ```
   This will execute the script and generate the output.
   
### Output

Upon running the program, the output will display the identified monotonic Boolean functions, detailing the conditions under which the gene is ON or OFF for each function. The program will also verify if all 18 expected functions are present.

### Output Format:
```
Monotonic Boolean functions:
Function 1:  NoRepressors and NoActivators -> OFF | NoRepressors and SomeActivators -> OFF | NoRepressors and AllActivators -> ON |  ...
Function 2:  NoRepressors and NoActivators -> OFF | NoRepressors and SomeActivators -> OFF | NoRepressors and AllActivators -> ON |  ...

...

Total number of monotonic functions: 18
All expected functions match the generated monotonic functions

```

This output confirms that the program successfully identified all 18 monotonic Boolean functions and verified them against the expected results.

**For a complete printout of the output and an explanation of the code, please refer to the Biological_Computation.pdf file.**


