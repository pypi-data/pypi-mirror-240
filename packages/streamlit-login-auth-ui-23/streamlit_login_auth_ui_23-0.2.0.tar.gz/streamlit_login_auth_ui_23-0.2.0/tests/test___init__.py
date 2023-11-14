# # test_sum_even_numbers.py

# import unittest
# from sum_even_numbers import sum_even_numbers

# class TestSumEvenNumbers(unittest.TestCase):
    
#     def test_sum_even_numbers_with_only_even_numbers(self):
#         result = sum_even_numbers([2, 4, 6, 8])
#         self.assertEqual(result, 20)
        
#     def test_sum_even_numbers_with_only_odd_numbers(self):
#         result = sum_even_numbers([1, 3, 5, 7])
#         self.assertEqual(result, 0)
        
#     def test_sum_even_numbers_with_mix_of_even_and_odd_numbers(self):
#         result = sum_even_numbers([1, 2, 3, 4, 5, 6])
#         self.assertEqual(result, 12)
        
#     def test_sum_even_numbers_with_empty_list(self):
#         result = sum_even_numbers([])
#         self.assertEqual(result, 0)
        
#     def test_sum_even_numbers_with_negative_numbers(self):
#         result = sum_even_numbers([-2, -4, -6, -8])
#         self.assertEqual(result, -20)
        
# if __name__ == '__main__':
#     unittest.main()