from django.test import TestCase
from .utils import add_random_records
import time

class TestAddRandomRecords(TestCase):

    def test_add_random_records_time(self):
        start_time = time.perf_counter()
        add_random_records(num_records=10000)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(total_time)
        self.assertLessEqual(total_time, 10.0, "Adding 10000 random records took more than 10 seconds")
