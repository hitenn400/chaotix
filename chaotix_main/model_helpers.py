class TextToImageAIMixin:
    def save(self, *args, **kwargs):
        # self.img_text = self.img_text.replace(" ","")
        # existing_text =self.__class__.objects.filter(
        #         img_text=self.img_text).exclude(id=self.id).exists()
        # print("existing_text: ",existing_text)
        # print("img_text: ",self.img_text)
        # if existing_text:
        #     raise Exception("Image with same Text already exists!")
        super(TextToImageAIMixin, self).save(*args, **kwargs)