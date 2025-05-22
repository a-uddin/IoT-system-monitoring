import psutil
import time

def get_laptop_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    stats = {
        'cpu_percent': cpu_percent,
        'memory_used': round(memory.used / (1024 ** 3), 2),  # in GB
        'memory_total': round(memory.total / (1024 ** 3), 2),
        'memory_percent': memory.percent,
        'disk_used': round(disk.used / (1024 ** 3), 2),
        'disk_total': round(disk.total / (1024 ** 3), 2),
        'disk_percent': disk.percent,
        'bytes_sent_MB': round(net.bytes_sent / (1024 ** 2), 2),
        'bytes_recv_MB': round(net.bytes_recv / (1024 ** 2), 2)
    }

    return stats

while True:
    data = get_laptop_stats()
    print(data)
    time.sleep(5)  # refresh every 5 seconds
