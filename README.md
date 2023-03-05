# PLD_project : Pedestrain Light Detection Project for visually impared person


## Introduction 

The PLD project is Pedestrain Light Detection Project for visually impared person.

I train light-weight object detection models 

## Pedestrian light datasets 

- AI-Hub street walking dataset

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

- Imvisible dataset

[Dataset_Download_Link](https://github.com/samuelyu2002/ImVisible). 

My download script is available in dataset_preparation/download_imvisible.py

*Caution: you need to install gdown first.*

    pip install gdown

Imvisible dataset has no bbox annotation.

Therefore, i made pseudo annotation using [yolo-v8x model](https://github.com/ultralytics/ultralytics).

The generated pseudo label(bounding-box) is available in 

**/label/ImVisible/bbox_original : classname, x1, y1, x2, y2** 

**/label/ImVisible/bbox_normalized : classname, x, y, w, h (normalized)**

class 0 : car traffic light

class 1 : pedestrain traffic light


**[2] Pedestrian traffic light and car traffic light classification model**

- data processing

There is no distinction between pedestrian traffic lights and vehicle traffic lights in AI-Hub street walking dataset

However, the required traffic light for visually impared is **only the pedestrian traffic light.**

Therefore, we are firstly train classification model on [Imsivible dataset](https://github.com/samuelyu2002/ImVisible) and [ETRI traffic light dataset](https://nanum.etri.re.kr/share/kimjy/etri_traffic_light?lang=ko_KR)


- model training 


## Training detection model

Now we have the pseudo labled traffic light dataset. 

I finetune the off-the-shelf lightweight object detection models on collected traffic light dataset.



## Citation 

If you find this repository helpful, please give us a citation.

    @article{Kim2023PLDproject,
        title={The PLD project: Pedestrian Light Detection project for visually impared person},
        author={Hyungmin Kim},
        journal={arXiv preprint},
        year={2023},
        publisher={arXiv}
    }