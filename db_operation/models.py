from django.db import models

class RecordMapping(models.Model):
    apn = models.CharField(max_length=255, db_column='apn', verbose_name='apn')
    country_id = models.PositiveIntegerField(db_column='country_id', verbose_name='countryid')
    total_incoming_bytes = models.PositiveBigIntegerField(db_column='total_incoming_bytes', verbose_name='downbytes')
    close_time_on = models.DateTimeField(db_column='close_time_on', verbose_name='endtime', null=True, blank=True)
    ip_address = models.GenericIPAddressField(db_column='ip_address', verbose_name='ipaddress')
    ipv6_address = models.GenericIPAddressField(protocol='IPv6', db_column='ipv6_address', verbose_name='ipv6address')
    ipv6_length = models.PositiveIntegerField(db_column='ipv6_length', verbose_name='ipv6length')
    external_id = models.PositiveIntegerField(db_column='external_id', verbose_name='msisdn')
    provider_id = models.PositiveIntegerField(db_column='provider_id', verbose_name='provider_id')
    start_time_on = models.DateTimeField(db_column='start_time_on', verbose_name='starttime', null=True, blank=True)
    total_bytes = models.PositiveBigIntegerField(db_column='total_bytes', verbose_name='totalbytes')
    total_outgoing_bytes = models.PositiveBigIntegerField(db_column='total_outgoing_bytes', verbose_name='upbytes')

    class Meta:
        db_table = 'record_mapping_my'
