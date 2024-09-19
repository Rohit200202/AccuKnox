from django.db import transaction
from django.dispatch import Signal, receiver
from myapp.models import MyModel

# Custom signal
test_signal = Signal()

# Signal handler
@receiver(test_signal)
def signal_handler(sender, **kwargs):
    # Try to create a new instance of MyModel
    MyModel.objects.create(name="SignalHandler")

# Simulate signal sending within a transaction
try:
    with transaction.atomic():
        print("Transaction started")
        test_signal.send(sender=None)
        raise Exception("Error to rollback transaction")
except Exception as e:
    print(f"Transaction rolled back due to: {e}")

# Check if MyModel object was created
print(MyModel.objects.all())
