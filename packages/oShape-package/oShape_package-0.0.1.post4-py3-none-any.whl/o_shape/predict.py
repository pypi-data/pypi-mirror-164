import time 
import argparse
import torch
from PIL import Image
import torchvision.transforms.functional as TF
import torchvision.transforms as transforms
import cv2
import numpy as np
import os
from o_shape.segment import get_length
from pathlib import Path

from models import *

SRC_DIR = Path(__file__).resolve().parent.parent


def build_model(model_version, quantize, model_path, device) :
    if model_version == 1:
        if quantize:
            net = quantized_modelv1(pretrained=True, device=device).to(device)
        else:
            net = modelv1(pretrained=True, device=device).to(device)
    elif model_version == 2:
        if quantize:
            net = quantized_modelv2(pretrained=True, device=device).to(device)
        else:
            net = modelv2(pretrained=True, device=device).to(device)
    else:
        raise Exception('[!] Unexpected model version')

    net = load_model(net, model_path, device)
    return net


def load_model(net, model_path, device):
    if model_path:
        print(f'[*] Load Model from {model_path}')
        net.load_state_dict(torch.load(model_path, map_location=device)['state_dict'])

    return net

def gamma_correction(image, white):

    if white: 
        return TF.adjust_gamma(image, 1.1)

    transform = transforms.ToTensor()
    # convert the image to PyTorch Tensor
    imgTensor = transform(image)

    r, g, b = torch.mean(imgTensor, dim=[1, 2])

    
    avg = (r + g + b ) /3 
    # print("AVERAGE VALUE: ", avg)
    if avg < 0.45:
        image = TF.adjust_gamma(image, 0.5)
        print("UNDER EXPOSED, INCREASING LIGHT")
        return image
    elif avg >=0.55: 
        image = TF.adjust_gamma(image, 1.1)
        print("OVER EXPOSED, DECREASING LIGHT")
        return image
    else: 
        print("NORMAL, NO GAMMA")
        return image

def saveMultipleImage():
    '''args here'''
    # save_image(torch.cat([image, result, mask]), os.path.join(self.sample_dir, f"{step}.jpg"))
    # save_image(torch.cat([(image * result), image, result, mask]), os.path.join(self.sample_dir, f"{step}.jpg"))
    # save_image(torch.cat([resized]), os.path.join(args.result_path, "0.jpg"))

def calculate_hair_ratio(bald_patch, mask, start_time):
 
    whitePixel = 0
    for i in range(0,bald_patch.shape[0]):
        for j in range(0,bald_patch.shape[1]):
            if bald_patch[i,j] > 0: 
                # print(grayImage[i,j])
                whitePixel += 1
    hairArea = 0
    for i in range(0,mask.shape[0]):
        for j in range(0,mask.shape[1]):
            if mask[i,j] > 0: 
                # print(grayImage[i,j])
                hairArea += 1
    proportion = whitePixel / (hairArea) * 100
    print(f'ratio: {proportion:.2f}%')
    print(f'calculation: {time.time() - start_time}')
    return proportion

def plot_image(resized, bald_patch, mask):
    cv2.imshow("Image",resized)
    cv2.imshow("bald patch & mask", np.hstack([bald_patch, mask]))
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def preprocess(resized,image, device, net, white=False):
    # convert original image into gray scale
    resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    if white:
        image = gamma_correction(image, True)
    else:
        image = gamma_correction(image, False)

    # resize image to 224x224 and image normalization around mean
    image = TF.to_tensor(image).to(device)
    image = TF.resize(image, [224, 224])
    image = TF.normalize(image, [0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    # print('IMAGE TIMES BINARY MASK : ', image.shape)
    # print('IMAGE TIMES BINARY MASK : ', image.unsqueeze(0).shape)
    start = time.time()
    mask = net(image.unsqueeze(0))
    print(f'inference time: {time.time() - start}')
    mask = mask.argmax(dim=1)
    mask = TF.resize(mask, [224, 224]).squeeze()
    print(f'IMAGE shape: {image.shape} vs BINARY MASK : {mask.shape} ')

    # generate mask
    bald_patch = (image * mask)

    bald_patch =  bald_patch.permute(1, 2, 0).cpu().detach().numpy()
    mask =  mask.cpu().detach().numpy()
    bald_patch = cv2.cvtColor(bald_patch, cv2.COLOR_BGR2GRAY)

    return resized, image, mask, bald_patch

def predict_o_shape(loaded_image):
    from loguru import logger 
    logger.error("PREDICTING O SSHAPE")
    # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    device = "cpu"
    # WINDOWS
    # net = build_model(2, False, r"C:\Users\ferdy\Documents\ai_backend\machine_learning_O_shape_bald_patch_ratio\checkpoints\best.pth", device).to(device)
    # MAC / LINUX
    net = build_model(2, False, str(SRC_DIR / 'checkpoints/best.pth'), device).to(device)
    start = time.time()

    image = loaded_image.convert('RGB') 

    open_cv_image = np.array(image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 

    Original_resized = cv2.resize(open_cv_image, (224,224), interpolation = cv2.INTER_AREA)
    
    resized, _ , mask, bald_patch = preprocess(Original_resized, image, device, net, False)

    ratio = calculate_hair_ratio(bald_patch, mask, start)

    if ratio > 70: 
        resized, image, mask, bald_patch = preprocess(Original_resized, image, device, net, True)
        ratio = calculate_hair_ratio(bald_patch, mask,start)

    '''
    about to change, depend on what the caller expect, currently its plotting the result to windows using opencv
    '''
    return ratio # in percentage
    # plot_image(resized, bald_patch, mask)


'''
this is used for running python predict.py directly
'''
def predict_internal(args, device, net):
    start = time.time()

    image = Image.open(args.image_path)

    Original_resized = cv2.resize(cv2.imread(args.image_path), (224,224), interpolation = cv2.INTER_AREA)
    
    resized, _ , mask, bald_patch = preprocess(Original_resized, image, device, net, False)
    cv2.imshow("original", Original_resized)
    cv2.imshow("bald_patch", bald_patch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ratio = calculate_hair_ratio(bald_patch, mask, start)

    if ratio > 70: 
        resized, image, mask, bald_patch = preprocess(Original_resized, image, device, net, True)
        ratio = calculate_hair_ratio(bald_patch, mask,start)

    plot_image(resized, bald_patch, mask)

def predict_hair_part(original):

    hair_part_image = original.convert('RGB') 

    hair_part_image = np.array(hair_part_image) 
    # Convert RGB to BGR 
    hair_part_image = hair_part_image[:, :, ::-1].copy() 

    cv2.imwrite("hairpart_result.jpg", hair_part_image)

    device = torch.device("cuda:0" if torch.cuda.is_available() and not args.quantize else "cpu")

    net = build_model(2,False, str(SRC_DIR / 'checkpoints/best.pth'), device).to(device)

    Original_resized = cv2.resize(cv2.imread('hairpart_result.jpg'), (224,224), interpolation = cv2.INTER_AREA)
    
    resized, _ , mask, bald_patch = preprocess(Original_resized, original, device, net, False)
    cv2.imwrite("results_hairpart.jpg", bald_patch * 255)
    return get_length()

    # lines = cv2.HoughLinesP(blurred_bald_patch, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250)
    # for line in lines:
    #     x1, y1, x2, y2 = line[0]
    #     cv2.line(blurred_bald_patch, (x1, y1), (x2, y2), (255, 0, 0), 3)


    # # bald_patch = cv2.Canny(blurred_bald_patch, 50, 200)

    # plot_image(resized, blurred_bald_patch, mask)
    # plot_image(resized, blurred_bald_patch, mask)
    # ratio = calculate_hair_ratio(bald_patch, mask, start)

    # if ratio > 70: 
    #     resized, image, mask, bald_patch = preprocess(Original_resized, image, device, net, True)
    #     ratio = calculate_hair_ratio(bald_patch, mask,start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--model_version', type=int, default=2, help='MobileHairNet version')
    parser.add_argument('--quantize', nargs='?', const=True, default=False, help='load and train quantizable model')
    parser.add_argument('--model_path', type=str, default=None)
    parser.add_argument('-i', '--image_path', type=str, default=None, help='path of the image')
    parser.add_argument('-o', '--result_path', type=str, default=None, help='path of the image')

    args = parser.parse_args()


    # args.image_path = "./dataset_tophead/images/0.jpg"
    args.image_path = r'C:\Users\Public\hair_parting\severe\severe_0000070.jpg'
    args.model_path = "./checkpoints/best.pth"

    device = torch.device("cuda:0" if torch.cuda.is_available() and not args.quantize else "cpu")
    net = build_model(args.model_version, args.quantize, args.model_path, device).to(device)

    for image in os.listdir(r'C:\Users\Public\hair_parting\severe'):
        if image.endswith('.jpg'):
            print(r'C:\Users\Public\hair_parting\severe', image)
            hair_parting_width(args, device, net, os.path.join(r'C:\Users\Public\hair_parting\severe', image))
    hair_parting_width(args, device, net, os.path.join(r'C:\Users\Public\hair_parting\severe', "severe_0000000.jpg"))

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()

#     parser.add_argument('--model_version', type=int, default=2, help='MobileHairNet version')
#     parser.add_argument('--quantize', nargs='?', const=True, default=False, help='load and train quantizable model')
#     parser.add_argument('--model_path', type=str, default=None)
#     parser.add_argument('-i', '--image_path', type=str, default=None, help='path of the image')
#     parser.add_argument('-o', '--result_path', type=str, default=None, help='path of the image')

#     args = parser.parse_args()

#     # args.image_path = "./dataset_tophead/images/0.jpg"
#     args.image_path = r'C:\Users\Public\hair_parting\severe\severe_0000070.jpg'
#     img = Image.open(args.image_path)
#     print(predict(img))

