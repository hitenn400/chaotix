
from django.dispatch import Signal, receiver
from .tasks import image_generator_task


image_generator_signal = Signal(
    providing_args=[
        "text_to_img_id",
    ]
)

@receiver(image_generator_signal)
def test_signal_celery_task(sender, **kwargs):
    print("image_generator_task Started")
    image_generator_task.apply_async(text_to_img_id=kwargs["text_to_img_id"])
    print("image_generator_task Completed")