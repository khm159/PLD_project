# PLD_project : Pedestrain Light Detection Project for visually impared person


## Introduction 

The PLD project is Pedestrain Light Detection Project for visually impared person.

I train light-weight object detection models 

## TODO List

- [x] Add Yolo-v8 wrapper 
- [ ] Add Yolo-v5 wrapper
- [ ] Add YoloR wrapper 
- [ ] Add YoloX wrapper 
- [ ] Add EfficientDET wrapper 
- [ ] Add Demo notebook
- [ ] Add Demo python source code

## Pedestrian light datasets 

### AI-Hub street walking dataset

[Dataset_Download_Link](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=189)

You need to join and request to download AI-Hub street walking dataset.

However, in the AI-Hub dataset, there is no distinction between traffic lights for car and pedestrians.

Therefore, i made an pseudo label using aspect ratio of bounding box. 

If the bounding box is long left and right, it is classified as a car traffic light, and if it is long up and down, it is classified as a pedestrain light.

The generated pseudo label(classification) is available in 

**/label/AIHub/bbox_original : classname, x1, y1, x2, y2** 

**/label/AIHub/bbox_normalized : classname, x, y, w, h (normalized)**

class 0 : car traffic light

class 1 : pedestrain traffic light

There are no official split.

If you use our dataset split, Please refer to the split in the data/AIHub/labels/train and data/AIHub/labels/test in the directory and place the image files as follows.

```bash
├── data
│   ├── AIHub
│   |    ├── images
│   |    |    ├── train
│   |    |    |    ├──MP_KSC_000001.jpg
│   |    |    |    ├──...
│   |    |    ├── test
│   |    |    |    ├──ZED1_KSC_003163_L_P000008.jpg
│   |    |    |    ├──...
│   |    ├── labels
│   |    |    ├── train
│   |    |    |    ├──MP_KSC_000001.txt
│   |    |    |    ├──...
│   |    |    ├── test
│   |    |    |    ├──ZED1_KSC_003163_L_P000008.txt
│   |    |    |    ├──...
``` 

### Imvisible dataset

[Dataset_Download_Link](https://github.com/samuelyu2002/ImVisible). 

My download script is available in [dataset_preparation/download_imvisible.py](dataset_preparation/download_imvisible.py)

*Caution: you need to install gdown first.*

    pip install gdown

Imvisible dataset has no bbox annotation.

Therefore, i made pseudo annotation using [yolo-v8x model](https://github.com/ultralytics/ultralytics).

The generated pseudo label(bounding-box) is available in

**/label/ImVisible/bbox_original : classname, x1, y1, x2, y2** 

**/label/ImVisible/bbox_normalized : classname, x, y, w, h (normalized)**

class 0 : car traffic light

class 1 : pedestrain traffic light


## model training 

Now we have the pseudo labled traffic light dataset. 

I finetune the off-the-shelf lightweight object detection models on collected traffic light dataset.

### Model list

|Implemented|Model Name|Wrapper|
|------|----|----|
|:heavy_check_mark:|[yolo_v8](https://github.com/ultralytics/ultralytics)|[yolov8_wrapper](/yolov8_wrapper.py)|
|:white_check_mark:|[yoloX](https://github.com/MegEngine/YOLOX)|[yolox_wrapper](/yolox_wrapper.py)|
|:white_check_mark:|[yoloR](https://github.com/WongKinYiu/yolor)|[yolor_wrapper](/yolor_wrapper.py)|
|:white_check_mark:|[yolo_v5](https://github.com/ultralytics/yolov5)|[yolov5_wrapper](/yolov5_wrapper.py)|


Please check train_exp.sh or train_exp.bat 


### Model Zoo 

- AI-Hub train only

| Model  | size<br><sup>(pixels) | mAP<sup>test<br>50-95<br>10 epoch | mAP<sup>test<br>50-95<br>20 epoch | Speed<br><sup>RTX-3090ti<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ------------------ |
| YOLOv8n | 640 | [0.2538](results/yolov8n_AIHub_only_10epoch/RESULTS.MD) | [0.2818](results/yolov8n_AIHub_only_20epoch/RESULTS.MD)   |        | 3.2    | 8.7     |
| YOLOv8s | 640 | [0.2893](results/yolov8s_AIHub_only_10epoch/RESULTS.MD) | [0.3196](results/yolov8s_AIHub_only_20epoch/RESULTS.MD)   |        | 11.2   | 28.6    |
| YOLOv8m | 640 | [0.3167](results/yolov8m_AIHub_only_10epoch/RESULTS.MD) | [0.3597](results/yolov8m_AIHub_only_20epoch/RESULTS.MD)   |        | 25.9   | 78.9    |
| YOLOv8l | 640 | [0.3260](results/yolov8l_AIHub_only_10epoch/RESULTS.MD) | [0.3597](results/yolov8l_AIHub_only_20epoch/RESULTS.MD)   |        | 43.7   | 165.2   |
| YOLOv8x | 640 | [0.3357](results/yolov8x_AIHub_only_10epoch/RESULTS.MD) | [0.3640](results/yolov8x_AIHub_only_20epoch/RESULTS.MD)   |        | 68.2   | 257.8   |

- **mAP<sup>test</sup>** values are for single-model single-scale on [AIHub](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=189) dataset.


- AI-Hub + Imvisible train 

| Model  | size<br><sup>(pixels) | mAP<sup>test<br>50-95<br>10 epoch | mAP<sup>test<br>50-95<br>20 epoch | Speed<br><sup>RTX-3090ti<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ------------------ |
| YOLOv8n | 640                   |                 |    |                          | 3.2                | 8.7               |
| YOLOv8s | 640                   |                 |    |                          | 11.2               | 28.6              |
| YOLOv8m | 640                   |                 |    |                          | 25.9               | 78.9              |
| YOLOv8l | 640                   |                 |    |                          | 43.7               | 165.2             |
| YOLOv8x | 640                   |                 |    |                          | 68.2               | 257.8             |

- **mAP<sup>test</sup>** values are for single-model single-scale on [AIHub](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=189) dataset.

## Color Classification Module 

After detecting the pedestrain light, the color of pedestrain light should be classified. 



## Citation 

If you find this repository helpful, please give us a citation.

    @software{
        Hyungmin_PLD_porject_Pedestrain_2023,
        author = {Hyungmin, Kim},
        license = {GPL-3.0},
        month = {3},
        title = {{PLD porject: Pedestrain Light Detection project for visually impared person}},
        url = {https://github.com/khm159/PLD_project},
        version = {0.0},
        year = {2023}
    }
