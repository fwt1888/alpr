# alpr
License plate target recognition based on pytorch-yolov4.

# 1.0  Environment setup

The following configuration has been tested to successfully run pytorch_yolov4, OIDv4_ToolKit, tensorflow and fiftyone in the same environment.

1. **anaconda**  virtual environment : python 3.9.18 (cuda: 11.6)
2. install **torch** : pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
3. install **opencv** : pip install opencv-python==3.4.14.51 -i https://mirrors.aliyun.com/pypi/simple
4. **numpy** version : 1.23.5
5. **tensorflow/tensorboard/tensorflow-gpu/tensorflow-intel** version : 2.10
6. **protobuf** version : 3.19.6

Test whether the environment is successfully established:

1. Download pre-trained weights, and put it under the `ALPR/pytorch-YOLOv4/weights`  folder

​	https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

2. Run the following code in the `pytorch-YOLOv4`  root directory

   `python demo.py -weightfile weights/yolov4.weights -imgfile data/dog.jpg` 

3. If the code does not produce an error and generates `predictions.jpg` in the root directory, the environment has been successfully configured.

# 2.0  Dataset download

Acquire the labeled images containing the license plate target in this step. This project uses the dataset downloaded from OIDv4_ToolKit for training (both the images and the annotations) and the data downloaded from fiftyone for model detection (using only the images). 

1. Download data from Open Images Dataset v7 via **fiftyone **: 

​	(a) `pip install fiftyone`

​	(b) run `ALPR/alpr/dataset_download.py`, modify the `max_samples` value to set the desired number of images

2. Download data from Open Images Dataset v4 via **OIDv4_ToolKit** :

   (a) `python ALPR/OIDv4_ToolKit/main.py downloader --classes Vehicle_registration_plate  --type_csv train --limit 500`

   (b) Modify `ALPR/OIDv4_ToolKit/classes.txt`, clear all contents and add `Vehicle registration plate`

   (c) `python ALPR/OIDv4_ToolKit/convert_annotations.py`

   ​	details of why can be found in this blog: [Create your own dataset for YOLOv4 object detection in 5 minutes ! | by Aditya Chakraborty | Analytics Vidhya | Medium](https://medium.com/analytics-vidhya/create-your-own-dataset-for-yolov4-object-detection-in-5-minutes-fdc988231088)

​       (d) Convert downloaded data to VOC format:

​	`python OIDv4_to_VOC.py --sourcepath "G:\Codes\ALPR\OIDv4_ToolKit\OID\Dataset\train\Vehicle registration plate" --dest_path "G:\Codes\ALPR\OIDv4_ToolKit\OID\Dataset\train\Annotation\Vehicle registration plate"` 

​	（e) Move all files in `OIDv4_ToolKit\OID\Dataset\train\Annotation\Vehicle registration plate` to `pytorch-YOLOv4\VOCdevkit\VOC2007\Annotations`

​		Store all images used for training in `pytorch-YOLOv4\VOCdevkit\VOC2007\JPEGImages`

​	**Note: The images and annotations placed in the above folders should match**

# 3.0  Model training

1. Place pre-trained model `yolov4.pth` in `ALPR/pytorch-YOLOv4/weights` dir (already in project)

2. Dataset segmentation : 

   run `ALPR/alpr/divide_dataset.py` 

​	run `ALPR/alpr/voc_annotation.py` -> Convert annotation generated by divide_dataset.py to voc format

3. Move the newly generated files in `pytorch-YOLOv4\VOCdevkit\VOC2007\ImageSets\Main` to `pytorch-YOLOv4\data`, and rename them to `test.txt`, `train.txt` and `val.txt`

4. Configure yolov4 : modify `pytorch-YOLOv4\cfg.py`

5. Run `pytorch-YOLOv4\train.py`

   The trained models (last 10 epochs) are stored in `pytorch-YOLOv4\checkpoints`

# 4.0  Model testing

1. Check figures of lr, ap, ar and loss

   run `tensorboard --logdir log --port 6008`

2. Target detection on test images

   template: 

   `python models.py <num_classes> <weightfile> <imgfile> <IN_IMAGE_W> <IN_IMAGE_H> <namefile(optional)>`

​	example:

​	`python models.py 1 checkpoints/Yolov4_epoch18.pth G:\Codes\ALPR\alpr\test_data\00071c51c8e92a68.jpg 768 768 data/custom.names` 	

​	**Note:**

​	 (1) Before run the above command, you should create `custom.names` in `pytorch-YOLOv4\data`, and add the content `vehicle registration plate`

​	(2) The height and width of the image have to satisfy the following constraints

```
height = 320 + 96 * n, n in {0, 1, 2, 3, ...}
width  = 320 + 96 * m, m in {0, 1, 2, 3, ...}
```
