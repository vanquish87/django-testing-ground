from typing import Any
from django.test import TestCase
from .utils import add_random_records, add_random_records_bulk
import time

class TestAddRandomRecords(TestCase):
    def setUp(self):
         self.num_records = 400000
         self.batch_size = 120
         

    def test_add_random_records_time_taken(self):
        start_time = time.perf_counter()
        add_random_records(num_records=self.num_records)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Single Insert took {total_time}')


    def test_add_random_records_bulk_time_taken(self):
        for i in range(1, self.batch_size + 1):
            start_time = time.perf_counter()
            add_random_records_bulk(num_records=self.num_records, batch_size=i)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f'Bulk Insert took {total_time} with the batch_size of {i}')