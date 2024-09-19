import threading
from django.dispatch import Signal, receiver

# Custom signal
test_signal = Signal()

# Signal handler
@receiver(test_signal)
def signal_handler(sender, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Simulate signal sending
print(f"Main thread ID: {threading.get_ident()}")
test_signal.send(sender=None)
