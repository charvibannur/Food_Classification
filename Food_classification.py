from collections import Counter
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


if __name__ == "__main__":

    # load model
    model = load_model(r"model_trained.h5")

    # image path
    img_path = r'image.jpg'

    # load a single image
    new_image = load_image(img_path)

    # plot image
    image = Image.open(img_path)
    image.show()

    # check prediction
    pred = model.predict(new_image)
    percentage = (pred * 100).astype('int64')
    for i in percentage:
        per={}
        per.update({'Biryani': i[0]})
        per.update({'BisibeleBath':i[1]})
        per.update({'Butternaan':i[2]})
        per.update({'Chaat': i[3]})
        per.update({'Chappati': i[4]})
        per.update({'Dhokla': i[5]})
        per.update({'Dosa': i[6]})
        per.update({'Gulab Jamun': i[7]})
        per.update({'halwa': i[8]})
        per.update({'Idly': i[9]})
        per.update({'Kaati roll': i[10]})
        per.update({'Meduvadai': i[11]})
        per.update({'Noodles': i[12]})
        per.update({'Paaniyaram': i[13]})
        per.update({'Poori': i[14]})
        per.update({'Samosa': i[15]})
        per.update({'Tandoori Chicken': i[16]})
        per.update({'Upma': i[17]})
        per.update({'Vadapav': i[18]})
        per.update({'Pongal': i[19]})


    # To display the three most probable classes

    k= Counter(per)
    high = k.most_common(3)
    for i in high:
        print(i[0]," :",i[1],"%")
