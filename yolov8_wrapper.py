from ultralytics import YOLO

def train_yolov8(
        model_name='yolov8x.pt', 
        train_epoch = 5, 
        dataset_config="coco128.yaml",
        batch_size = 8,
    ):
    """
    Train yolov8 wrapper function
        Args:
            model_name: yolov8 model name
            train_epoch: train epoch
            dataset_config: dataset config file (coco-style)
    """
    # Load a model
    model = YOLO(model_name) 

    # Use the model
    model.train(
        data="./configs/dataset/AIHub.yaml",
        epochs=train_epoch,
        batch=batch_size,
    )
    metrics = model.val()  
    print(metrics)
    # save model 
    model.save('yolov8x.pt')