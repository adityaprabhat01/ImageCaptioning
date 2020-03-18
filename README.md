# ImageCaptioning
Generated captions for the input image.
>Integrated beam search algorithm but needs improvement.
involves the intersection of computer vision and natural language processing. I used Flickr8k dataset which has 8000 images each of them described in five sentences. Along with that I also used Glove200d word embeddings to convert each of the description into
vectors. After that, I used Bidirectional LSTM to produce the encoded form of the text description data. The model utilized heavy transfer learning for encoding the images. I preferably used inceptionV3 (which was pretrained on the ImageNet dataset) because it has relatively a smaller number of parameters compared to other models such as VGG16 or AlexNet. Also, I used Dropout in both text and image encoding to prevent overfitting. After I got the encoded form of image as well as text, I combined both of them just by adding together (According to Andrej Karparthy paper) which is a very simple and linear transformation. Then Backpropagated through the whole network, freezing the embedding layer.
