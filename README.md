# Data Governance and Quality Assignment

## Problem Description

In this assignment, you will use the Great Expectations library to create a suite of data quality checks for a real dataset. You will be working with the "tips" dataset from seaborn, which contains information about restaurant tips.

## Learning Objectives

By completing this assignment, you will learn:
- How to use Great Expectations for data quality validation
- How to define and implement data quality expectations
- How to validate datasets against business rules
- Best practices for data governance and quality assurance

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas
   - seaborn
   - great-expectations
   - numpy

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `validate_tips_dataset()`.
3. Your tasks are to:
   *   **Task 1**: Load the "tips" dataset from the seaborn library into a pandas DataFrame.
   *   **Task 2**: Convert the pandas DataFrame into a Great Expectations DataFrame.
   *   **Task 3**: Add at least three expectations:
       *   The `total_bill` column should be between 3 and 51.
       *   The `tip` column should be between 1 and 11.
       *   The `day` column should only contain one of these values: ['Thur', 'Fri', 'Sat', 'Sun'].
   *   **Task 4**: Return the validation results.

## Hints

*   Use `seaborn.load_dataset('tips')` to get the data.
*   Use `ge.from_pandas()` to convert the DataFrame.
*   Use `expect_column_values_to_be_between()` and `expect_column_values_to_be_in_set()`.
*   The validation results can be obtained by calling `.validate()` on the Great Expectations DataFrame.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That your function returns the correct type of object
- That all expectations are properly added
- That the validation results have the expected structure
- That all expectations pass successfully

## Expected Output

Your function should return a Great Expectations validation result object that contains:
- `success`: Boolean indicating if all expectations passed
- `results`: List of individual expectation results
- `statistics`: Summary statistics about the validation

## Further Exploration (Optional)

*   Great Expectations can generate a full HTML report of the validation results. How would you save this "Data Docs" site?
*   Can you create a custom expectation? For example, could you write an expectation to check that the `tip` is always less than the `total_bill`?
*   How would you save an Expectation Suite to a JSON file so you can reuse it later?
*   What other types of expectations could you add for this dataset?

## Resources

- [Great Expectations Documentation](https://docs.greatexpectations.io/)
- [Seaborn Datasets](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
