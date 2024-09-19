import time
from django.dispatch import Signal, receiver

# Custom signal
test_signal = Signal()

# Signal handler
@receiver(test_signal)
def signal_handler(sender, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a time-consuming task
    print("Signal handler finished")

# Simulate signal sending
start_time = time.time()
test_signal.send(sender=None)
end_time = time.time()

print(f"Total time taken: {end_time - start_time} seconds")
