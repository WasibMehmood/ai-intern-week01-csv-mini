# CSV Mini‑Project – Average Marks

This mini-project reads a CSV file named `students.csv`, which contains a list of student names along with their marks in three subjects: Math, English, and Science. The script processes this data and calculates the average marks obtained by each student across all subjects. Once the averages are computed, the results are saved in a separate file called `summary.csv`. This allows you to quickly review each student’s performance in a structured format.

### Features

* Automatically compute the average marks of Math, English, and Science for each student in the input file.
* Round the calculated average to 2 decimal places for clarity and consistency in reporting.
* Perform validation to ensure the CSV data is correctly formatted before processing.
* The project is fully unit tested using `pytest` to verify the accuracy of calculations and the reliability of the output.
* Easy to extend if you want to include additional subjects or different grading criteria.

### To Run

Make sure you have Python installed on your system.
Run the following command to generate the summary file:
`python summary.py`

### Check Test Cases

Use `pytest` to execute the test suite and confirm that all functions behave as expected:
`pytest`

This project demonstrates basic file handling, data processing, and automated testing in Python.
