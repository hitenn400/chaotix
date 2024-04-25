from django.dispatch import Signal, receiver
from .tasks import image_generator_task

image_generator_signal = Signal()


@receiver(image_generator_signal)
def image_generator_task_signal(sender, **kwargs):
    print("image_generator_task_signal Started")
    print("kwarg: ", kwargs["text_to_img_id"])
    image_generator_task.apply_async(args=[kwargs["text_to_img_id"]])
    print("image_generator_task_signal Completed")
