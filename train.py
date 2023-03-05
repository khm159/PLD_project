avail_model=[
    "yolov8x.pt", "yolov8l.pt", "yolov8m.pt", "yolov8s.pt", "yolov8n.pt",
    "yolov5x.pt", "yolov5l.pt", "yolov5m.pt", "yolov5s.pt", "yolov5n.pt",
]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name", 
        default="yolov8x.pt", 
        choices=avail_model
    )
    parser.add_argument(
        "--tune_epoch",
        default=5,
        type=int
    )
    parser.add_argument(
        "--dataset_config", 
        default="configs/dataset/AIHub.yaml"
    )
    parser.add_argument(
        "--batch_size",
        default=4,
        type=int
    )
    args = parser.parse_args()
    if "v8" in args.model_name:
        from yolov8_wrapper import train_yolov8
        train_yolov8(
            model_name=args.model_name, 
            train_epoch=args.tune_epoch,
            dataset_config=args.dataset_config,
            batch_size=args.batch_size
        )
    else:
        NotImplementedError
        
    

