"""YOLOv3 PyTorch Hub models https://pytorch.org/hub/ultralytics_yolov3/

Usage:
    import torch
    model = torch.hub.load('ultralytics/yolov3', 'yolov3tiny')
"""

from pathlib import Path

import torch

from models.yolo import Model
from utils.general import check_requirements, set_logging
from utils.google_utils import attempt_download
from utils.torch_utils import select_device

dependencies = ['torch', 'yaml']
check_requirements(Path(__file__).parent / 'requirements.txt', exclude=('pycocotools', 'thop'))
set_logging()


def create(name, pretrained, channels, classes, autoshape):
    """Creates a specified YOLOv3 model

    Arguments:
        name (str): name of model, i.e. 'yolov3'
        pretrained (bool): load pretrained weights into the model
        channels (int): number of input channels
        classes (int): number of model classes

    Returns:
        pytorch model
    """
    try:
        cfg = list((Path(__file__).parent / 'models').rglob(f'{name}.yaml'))[0]  # model.yaml path
        model = Model(cfg, channels, classes)
        if pretrained:
            fname = f'{name}.pt'  # checkpoint filename
            attempt_download(fname)  # download if not found locally
            ckpt = torch.load(fname, map_location=torch.device('cpu'))  # load
            msd = model.state_dict()  # model state_dict
            csd = ckpt['model'].float().state_dict()  # checkpoint state_dict as FP32
            csd = {k: v for k, v in csd.items() if msd[k].shape == v.shape}  # filter
            model.load_state_dict(csd, strict=False)  # load
            if len(ckpt['model'].names) == classes:
                model.names = ckpt['model'].names  # set class names attribute
            if autoshape:
                model = model.autoshape()  # for file/URI/PIL/cv2/np inputs and NMS
        device = select_device('0' if torch.cuda.is_available() else 'cpu')  # default to GPU if available
        return model.to(device)

    except Exception as e:
        help_url = 'https://github.com/ultralytics/yolov5/issues/36'
        s = 'Cache maybe be out of date, try force_reload=True. See %s for help.' % help_url
        raise Exception(s) from e


def custom(path_or_model='path/to/model.pt', autoshape=True):
    """YOLOv3-custom model https://github.com/ultralytics/yolov3

    Arguments (3 options):
        path_or_model (str): 'path/to/model.pt'
        path_or_model (dict): torch.load('path/to/model.pt')
        path_or_model (nn.Module): torch.load('path/to/model.pt')['model']

    Returns:
        pytorch model
    """
    model = torch.load(path_or_model) if isinstance(path_or_model, str) else path_or_model  # load checkpoint
    if isinstance(model, dict):
        model = model['ema' if model.get('ema') else 'model']  # load model

    hub_model = Model(model.yaml).to(next(model.parameters()).device)  # create
    hub_model.load_state_dict(model.float().state_dict())  # load state_dict
    hub_model.names = model.names  # class names
    if autoshape:
        hub_model = hub_model.autoshape()  # for file/URI/PIL/cv2/np inputs and NMS
    device = select_device('0' if torch.cuda.is_available() else 'cpu')  # default to GPU if available
    return hub_model.to(device)


def yolov3(pretrained=True, channels=3, classes=80, autoshape=True):
    # YOLOv3 model https://github.com/ultralytics/yolov3
    return create('yolov3', pretrained, channels, classes, autoshape)


def yolov3_spp(pretrained=True, channels=3, classes=80, autoshape=True):
    # YOLOv3-SPP model https://github.com/ultralytics/yolov3
    return create('yolov3-spp', pretrained, channels, classes, autoshape)


def yolov3_tiny(pretrained=True, channels=3, classes=80, autoshape=True):
    # YOLOv3-tiny model https://github.com/ultralytics/yolov3
    return create('yolov3-tiny', pretrained, channels, classes, autoshape)


if __name__ == '__main__':
    model = create(name='yolov3', pretrained=True, channels=3, classes=80, autoshape=True)  # pretrained example
    # model = custom(path_or_model='path/to/model.pt')  # custom example

    # Verify inference
    import numpy as np
    from PIL import Image

    imgs = [Image.open('data/images/bus.jpg'),  # PIL
            'data/images/zidane.jpg',  # filename
            'https://github.com/ultralytics/yolov3/raw/master/data/images/bus.jpg',  # URI
            np.zeros((640, 480, 3))]  # numpy

    results = model(imgs)  # batched inference
    results.print()
    results.save()
