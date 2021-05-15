from torchvision import transforms
from utils import *
from PIL import Image, ImageDraw, ImageFont
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input', required=True, help='path to input image'
)
parser.add_argument(
    '-t', '--threshold', default=0.45, type=float,
    help='minimum confidence score to consider a prediction'
)
args = vars(parser.parse_args())

# set the computation device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Load model checkpoint
checkpoint = 'checkpoints/checkpoint_ssd300.pth.tar'
checkpoint = torch.load(checkpoint)
start_epoch = checkpoint['epoch'] + 1
print('\nLoaded checkpoint from epoch %d.\n' % start_epoch)
model = checkpoint['model']
model = model.to(device)
model.eval()

# Transforms
resize = transforms.Resize((300, 300))
to_tensor = transforms.ToTensor()
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

def detect(original_image, min_score, max_overlap, top_k, suppress=None):
    """
    Detect objects in an image with a trained SSD300, and visualize the results.
    :param original_image: image, a PIL Image
    :param min_score: minimum threshold for a detected box to be considered a match for a certain class
    :param max_overlap: maximum overlap two boxes can have so that the one with the lower score is not suppressed via Non-Maximum Suppression (NMS)
    :param top_k: if there are a lot of resulting detection across all classes, keep only the top 'k'
    :param suppress: classes that you know for sure cannot be in the image or you do not want in the image, a list
    :return: annotated image, a PIL Image
    """
    # Transform
    image = normalize(to_tensor(resize(original_image)))
    # Move to default device
    image = image.to(device)
    # Forward prop.
    predicted_locs, predicted_scores = model(image.unsqueeze(0))
    # Detect objects in SSD output
    det_boxes, det_labels, det_scores = model.detect_objects(predicted_locs, predicted_scores, min_score=min_score,
                                                             max_overlap=max_overlap, top_k=top_k)
    # Move detections to the CPU
    det_boxes = det_boxes[0].to('cpu')
    # Transform to original image dimensions
    original_dims = torch.FloatTensor(
        [original_image.width, original_image.height, original_image.width, original_image.height]).unsqueeze(0)
    det_boxes = det_boxes * original_dims
    # Decode class integer labels
    det_labels = [rev_label_map[l] for l in det_labels[0].to('cpu').tolist()]
    # If no objects found, the detected labels will be set to ['0.'], i.e. ['background'] in SSD300.detect_objects() in model.py
    if det_labels == ['background']:
        # Just return original image
        return original_image
    # Annotate
    annotated_image = original_image
    draw = ImageDraw.Draw(annotated_image)
    font = ImageFont.truetype("./calibril.ttf", 15)
    # Suppress specific classes, if needed
    for i in range(det_boxes.size(0)):
        if suppress is not None:
            if det_labels[i] in suppress:
                continue
        # Boxes
        box_location = det_boxes[i].tolist()
        draw.rectangle(xy=box_location, outline=label_color_map[det_labels[i]])
        draw.rectangle(xy=[l + 1. for l in box_location], outline=label_color_map[
            det_labels[i]])
        # Text
        text_size = font.getsize(det_labels[i].upper())
        text_location = [box_location[0] + 2., box_location[1] - text_size[1]]
        textbox_location = [box_location[0], box_location[1] - text_size[1], box_location[0] + text_size[0] + 4.,
                            box_location[1]]
        draw.rectangle(xy=textbox_location, fill=label_color_map[det_labels[i]])
        draw.text(xy=text_location, text=det_labels[i].upper(), fill='white',
                  font=font)
    del draw
    return annotated_image

if __name__ == '__main__':
    img_path = args['input']
    # read as PIL image
    original_image = Image.open(img_path, mode='r')
    # conver to RGB color format
    original_image = original_image.convert('RGB')
    # get the output as PIL image
    pil_image_out = detect(original_image, min_score=args['threshold'], max_overlap=0.5, top_k=200)
    # conver to NumPy array format
    result_np = np.array(pil_image_out, dtype=np.uint8)
    # convert frm RGB to BGR format for OpenCV visualizations
    result_np = cv2.cvtColor(result_np, cv2.COLOR_RGB2BGR)
    # show the image with detected objects on screen
    cv2.imshow('Result', result_np)
    cv2.waitKey(0)
    # save the image to disk
    save_name = args['input'].split('/')[-1]
    cv2.imwrite(f"outputs/{save_name}", result_np)