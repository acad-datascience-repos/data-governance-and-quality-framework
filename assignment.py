import great_expectations as ge
import pandas as pd
import seaborn as sns

def validate_tips_dataset():
  """
  Loads the tips dataset and validates it using Great Expectations.

  Returns:
    A Great Expectations validation result object.
  """
  # Task 1: Load the tips dataset from seaborn
  # Hint: Use sns.load_dataset('tips')
  tips_df = None
  # Your code here

  # Task 2: Convert to a Great Expectations DataFrame
  # Hint: Use the pandas DataFrame directly - Great Expectations methods work on pandas DataFrames
  ge_df = None
  # Your code here

  # Task 3: Add expectations
  # Add expectation 1: total_bill should be between 3 and 51
  # Hint: Use tips_df['total_bill'].between(3, 51).all()
  # Your code here

  # Add expectation 2: tip should be between 1 and 11
  # Hint: Use tips_df['tip'].between(1, 11).all()
  # Your code here

  # Add expectation 3: day should only contain ['Thur', 'Fri', 'Sat', 'Sun']
  # Hint: Use tips_df['day'].isin(['Thur', 'Fri', 'Sat', 'Sun']).all()
  # Your code here

  # Task 4: Validate and return the results
  # Hint: Create a validation result object with success, results, and statistics
  validation_results = None
  # Your code here

  return validation_results