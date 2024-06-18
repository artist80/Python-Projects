import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import time

# Data storage
cpu_usage = []
memory_usage = []
disk_usage = []
timestamps = []

# Data collection interval (seconds)
INTERVAL = 1

# Function to collect system data
def collect_data():
    while True:
        # Collect CPU, Memory, and Disk usage
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        timestamp = time.strftime('%H:%M:%S')

        # Store data
        cpu_usage.append(cpu)
        memory_usage.append(memory)
        disk_usage.append(disk)
        timestamps.append(timestamp)

        # Keep only the last 60 data points
        if len(cpu_usage) > 60:
            cpu_usage.pop(0)
            memory_usage.pop(0)
            disk_usage.pop(0)
            timestamps.pop(0)

        time.sleep(INTERVAL)

# Start data collection in a separate thread
data_thread = threading.Thread(target=collect_data)
data_thread.daemon = True
data_thread.start()

# Function to update the plot
def update_plot(frame):
    plt.clf()
    plt.subplot(3, 1, 1)
    plt.plot(timestamps, cpu_usage, label='CPU Usage (%)')
    plt.legend(loc='upper right')
    plt.subplot(3, 1, 2)
    plt.plot(timestamps, memory_usage, label='Memory Usage (%)', color='orange')
    plt.legend(loc='upper right')
    plt.subplot(3, 1, 3)
    plt.plot(timestamps, disk_usage, label='Disk Usage (%)', color='green')
    plt.legend(loc='upper right')
    plt.tight_layout()

# Set up the plot
fig = plt.figure(figsize=(10, 6))
ani = FuncAnimation(fig, update_plot, interval=1000)

# Show the plot
plt.show()
