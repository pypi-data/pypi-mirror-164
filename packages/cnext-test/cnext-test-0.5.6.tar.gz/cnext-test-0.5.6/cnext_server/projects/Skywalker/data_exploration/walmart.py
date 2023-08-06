import pandas as pd
import random

img_urls = ['https://i5.walmartimages.com/asr/84835fa1-d3cd-4ca5-ba74-ad67d8b65812.4f2e48b02f23175e273bc1c9df42131d.jpeg',
            'https://i5.walmartimages.com/asr/3ea8e6f3-bff0-4195-a6bf-41f4e86dc73d_1.5e8cf62f3e0428161a2279ae13351afd.jpeg', 
            'https://i5.walmartimages.com/asr/6b8a7af8-0c49-46cd-893f-2f1138b83a8d.d015ca263d64ad5bd9bcbcbea1448314.jpeg']
data = {
    'pred': [random.randint(0,1) for i in range(len(img_urls))],
    'true': [random.randint(0,1) for i in range(len(img_urls))],
    'image': img_urls
}
df = pd.DataFrame(data=data)
df['image'] = df['image'].astype('url/png')