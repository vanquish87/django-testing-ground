import random
from datetime import timedelta
from db_operation.models import RecordMapping

from django.utils import timezone

def add_random_records(num_records):
    for i in range(num_records):
        # Create a new record with random values
        record = RecordMapping(
            apn=f"apn{i}",
            country_id=random.randint(1, 100),
            total_incoming_bytes=random.randint(100000, 100000000),
            close_time_on=timezone.now() - timedelta(days=random.randint(0, 365)),
            ip_address=f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
            ipv6_address=f"{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}:{random.randint(0, 65535):04x}",
            ipv6_length=random.randint(1, 128),
            external_id=random.randint(1000000000, 9999999999),
            provider_id=random.randint(1, 10),
            start_time_on=timezone.now() - timedelta(days=random.randint(0, 365)),
            total_bytes=random.randint(100000, 100000000),
            total_outgoing_bytes=random.randint(100000, 100000000),
        )
        record.save()
