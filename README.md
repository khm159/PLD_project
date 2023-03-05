# PLD_project : Pedestrain Light Detection Project for visually impared person


## Introduction 

The PLD project is Pedestrain Light Detection Project for visually impared person.

I train light-weight object detection models 

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

[x] [yolo_v8](https://github.com/ultralytics/ultralytics) [Wrapper](/yolov8_wrapper.py)

[ ] [yoloX](https://github.com/MegEngine/YOLOX) [Wrapper](/yolox_wrapper.py)

[ ] [yoloR](https://github.com/WongKinYiu/yolor) [Wrapper](/yolor_wrapper.py)

[ ] [yolo_v5](https://github.com/ultralytics/yolov5) [Wrapper](/yolov5_wrapper.py)


Please check train_exp.sh or train_exp.bat 


### Model Zoo 

### Results 


## Citation 

If you find this repository helpful, please give us a citation.

    @article{Kim2023PLDproject,
        title={The PLD project: Pedestrian Light Detection project for visually impared person},
        author={Hyungmin Kim},
        journal={arXiv preprint},
        year={2023},
        publisher={arXiv}
    }