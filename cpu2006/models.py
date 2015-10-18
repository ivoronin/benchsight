from django.db import models


class Result(models.Model):
    benchmark = models.CharField("Benchmark", max_length=255)
    hardware_vendor = models.CharField("Hardware Vendor", max_length=255)
    system = models.CharField("System", max_length=255)
    result = models.FloatField("Result")
    baseline = models.FloatField("Baseline")
    num_cores = models.IntegerField("# Cores")
    num_chips = models.IntegerField("# Chips")
    num_cores_per_chip = models.IntegerField("# Cores Per Chip")
    num_threads_per_core = models.IntegerField("# Threads Per Core")
    processor = models.CharField("Processor", max_length=255)
    processor_mhz = models.IntegerField("Processor MHz")
    processor_characteristics = models.CharField("Processor Characteristics", max_length=255)
    cpus_orderable = models.CharField("CPU(s) Orderable", max_length=255)
    auto_parallelization = models.BooleanField("Auto Parallelization")
    base_pointer_size = models.CharField("Base Pointer Size", max_length=255)
    peak_pointer_size = models.CharField("Peak Pointer Size", max_length=255)
    first_level_cache = models.CharField("1st Level Cache", max_length=255)
    second_level_cache = models.CharField("2nd Level Cache", max_length=255)
    third_level_cache = models.CharField("3rd Level Cache", max_length=255)
    other_cache = models.CharField("Other Cache", max_length=255)
    memory = models.CharField("Memory", max_length=255)
    operating_system = models.CharField("Operating System", max_length=255)
    file_system = models.CharField("File System", max_length=255)
    compiler = models.CharField("Compiler", max_length=255)
    hw_avail = models.DateField("HW Avail")
    sw_avail = models.DateField("SW Avail")
    license = models.IntegerField("License")
    tested_by = models.CharField("Tested By", max_length=255)
    test_sponsor = models.CharField("Test Sponsor", max_length=255)
    test_date = models.DateField("Test Date")
    published = models.DateField("Published")
    updated = models.DateField("Updated")

    @property
    def processor_ghz(self):
        return self.processor_mhz / 1000
