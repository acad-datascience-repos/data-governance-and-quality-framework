import unittest
from assignment import validate_tips_dataset
import great_expectations as ge
import pandas as pd
import seaborn as sns

class TestDataGovernance(unittest.TestCase):
    def test_validate_tips_dataset_returns_validation_result(self):
        """Test that the function returns a validation result object"""
        validation_results = validate_tips_dataset()
        self.assertIsInstance(validation_results, dict)
    
    def test_validation_results_structure(self):
        """Test that validation results have the expected structure"""
        validation_results = validate_tips_dataset()
        
        # Check if the validation was successful
        self.assertTrue(validation_results['success'])
        
        # Check that results contain the expected keys
        expected_keys = ['success', 'statistics', 'results']
        for key in expected_keys:
            self.assertIn(key, validation_results)
    
    def test_expectations_were_added(self):
        """Test that the expected number of expectations were added"""
        validation_results = validate_tips_dataset()
        
        # Should have 3 expectations (total_bill, tip, day)
        self.assertEqual(len(validation_results['results']), 3)
        
        # Check that all expectations passed
        for result in validation_results['results']:
            self.assertTrue(result['success'], f"Expectation {result['expectation_config']['expectation_type']} failed")
    
    def test_data_loading(self):
        """Test that the tips dataset is loaded correctly"""
        # This test ensures the student actually loaded the data
        tips_df = sns.load_dataset('tips')
        self.assertIsInstance(tips_df, pd.DataFrame)
        self.assertGreater(len(tips_df), 0)
        self.assertIn('total_bill', tips_df.columns)
        self.assertIn('tip', tips_df.columns)
        self.assertIn('day', tips_df.columns)

if __name__ == '__main__':
    unittest.main()
