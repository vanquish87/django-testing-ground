from typing import Any
from django.test import TestCase
from .utils import add_random_records, add_random_records_bulk
import time


class TestAddRandomRecords(TestCase):
    """To compare speed of different approaches of inserting into DB"""

    databases = {"default", "test_db"}

    def setUp(self):
        self.num_records = 20000
        self.batch_size = 100

    def test_add_random_records_time_taken(self):
        start_time = time.perf_counter()
        add_random_records(num_records=self.num_records)
        end_time = time.perf_counter()
        total_time = round((end_time - start_time), 3)
        print(f"Single Insert took {total_time} seconds")

    def test_add_random_records_bulk_time_taken(self):
        batch_timing = {}
        for i in range(1, self.batch_size + 1):
            start_time = time.perf_counter()
            add_random_records_bulk(num_records=self.num_records, batch_size=i)

            end_time = time.perf_counter()
            total_time = round((end_time - start_time), 3)

            batch_timing[i] = total_time

            print(f"Bulk Insert took {total_time} seconds with the batch_size of {i}")

        # Sort the dictionary by value in ascending order
        sorted_batch_timing = dict(sorted(batch_timing.items(), key=lambda item: item[1]))

        print("----------- TOP 3 TIMINGS FOR BULK INSERT AS FOLLOWS -----------")
        count = 0
        for key, value in sorted_batch_timing.items():
            print(f'batch_size : {key}, time taken : {value}')
            count += 1
            if count > 2:
                break

