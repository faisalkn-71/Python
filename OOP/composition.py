class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, ram_size) -> None:
        self.ram_size = ram_size

class SSD:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        

class Computer:
    def __init__(self, cores, ram_size, capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.ssd = SSD(capacity)
        