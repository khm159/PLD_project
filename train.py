from ultralytics import YOLO


def train_yolov8(model_name='yolov8x.pt', train_epoch = 5):

    # Load a model
    model = YOLO(model_name) 

    # Use the model
    model.train(
        data="./configs/dataset/AIHub.yaml",
        epochs=train_epoch
    )
    metrics = model.val()  
    print(metrics)
    # save model 
    model.save('yolov8x.pt')

if __name__ == "__main__":
    train_yolov8()

