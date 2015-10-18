import csv
import os
from datetime import datetime
from time import sleep
from codecs import iterdecode
from urllib.request import urlopen
from django.db import transaction
from django.core.management.base import BaseCommand
from cpu2006.models import Result

CPU2006_DUMP_URL = "https://www.spec.org/cgi-bin/osgresults?conf=cpu2006;op=dump;format=csvdump"


class Command(BaseCommand):
    help = 'Imports SPECint CPU2006 results'

    def add_arguments(self, parser):
         parser.add_argument('--delay', type=float, help="Throttle for delay seconds before processing each row")

    def handle(self, *args, **options):
        delay = options['delay']
        rows = 0
        with urlopen(CPU2006_DUMP_URL) as data:
            reader = csv.reader(iterdecode(data, 'utf-8'))
            next(reader)  # Skip header
            with transaction.atomic():
                Result.objects.all().delete()
                for row in reader:
                    if delay:
                        sleep(delay)
                    rows += 1
                    if not rows % 1000:
                        print("%i rows processed" % rows)
                    res = Result()
                    res.benchmark = row[0]
                    res.hardware_vendor = row[1]
                    res.system = row[2]
                    res.result = float(row[3])
                    res.baseline = float(row[4])
                    res.num_cores = int(row[5])
                    res.num_chips = int(row[6])
                    res.num_cores_per_chip = int(row[7])
                    res.num_threads_per_core = int(row[8])
                    res.processor = row[9]
                    res.processor_mhz = int(row[10])
                    res.processor_characteristics = row[11]
                    res.cpus_orderable = row[12]
                    res.auto_parallelization = row[13]
                    res.base_pointer_size = row[14]
                    res.peak_pointer_size = row[15]
                    res.first_level_cache = row[16]
                    res.second_level_cache = row[17]
                    res.third_level_cache = row[18]
                    res.other_cache = row[19]
                    res.memory = row[20]
                    res.operating_system = row[21]
                    res.file_system = row[22]
                    res.compiler = row[23]
                    res.hw_avail = datetime.strptime(row[24], '%b-%Y')
                    res.sw_avail = datetime.strptime(row[25], '%b-%Y')
                    res.license = row[26]
                    res.tested_by = row[27]
                    res.test_sponsor = row[28]
                    res.test_date = datetime.strptime(row[29], '%b-%Y')
                    res.published = datetime.strptime(row[30], '%b-%Y')
                    res.updated = datetime.strptime(row[31], '%b-%Y')
                    res.save()
