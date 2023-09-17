"""
Test goes here

"""
from script import descript_stat
import polars as pl
import unittest

WP_data = pl.read_csv('world_population.csv')



#country's population in 2022, growth rate and area.

data = WP_data[['2022 Population','Growth Rate','Area (km²)']]

class TestDescriptiveStatistics(unittest.TestCase):
    def test_function_runs_without_errors(self):
        try:
            # Call your function here
            # Example: descript_stat(your_input_data)
            descript_stat(data)
        except Exception as e:
            self.fail(f"Function raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()