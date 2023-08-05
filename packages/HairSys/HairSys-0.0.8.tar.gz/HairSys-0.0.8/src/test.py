import time

import torch
import os
from tqdm import tqdm
from torchvision.utils import save_image
from utils.custom_transfrom import UnNormalize
from utils.util import AverageMeter, quantize_model
from loss.loss import iou_loss
from models import *
import numpy as np
import cv2 


class Tester:
    def __init__(self, config, dataloader):
        self.batch_size = config.batch_size
        self.config = config
        self.model_path = config.checkpoint_dir
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.data_loader = dataloader
        self.num_classes = config.num_classes
        self.num_test = config.num_test
        self.sample_dir = config.sample_dir
        self.checkpoint_dir = config.checkpoint_dir
        self.quantize = config.quantize
        self.model_version = config.model_version
        if self.quantize:
            self.device = torch.device('cpu')
        self.build_model()

    def build_model(self):
        if self.model_version == 1:
            if self.quantize:
                self.net = quantized_modelv1(device=self.device, pretrained=True).to(self.device)
            else:
                self.net = modelv1(device=self.device, pretrained=True).to(self.device)
        elif self.model_version == 2:
            if self.quantize:
                self.net = quantized_modelv2(device=self.device, pretrained=True).to(self.device)
            else:
                self.net = modelv2(device=self.device, pretrained=True).to(self.device)
        else:
            raise Exception('[!] Unexpected model version')
        self.load_model()
        
    def load_model(self):
        ckpt = f'{self.checkpoint_dir}/quantized.pth' if self.quantize else f'{self.checkpoint_dir}/best.pth'
        if not os.path.exists(ckpt):
            return
        print(f'[*] Load Model from {ckpt}')
        save_info = torch.load(ckpt, map_location=self.device)
        if self.quantize:
            self.net.quantize()
        self.net.load_state_dict(save_info['state_dict'])

    def test(self, net=None):
        if net:
            self.net = net
        self.net = self.net.eval()
        avg_meter = AverageMeter()
        inference_avg = AverageMeter()
        torch.save(self.net.state_dict(), "tmp.pth")
        model_size = "%.2f MB" % (os.path.getsize("tmp.pth") / 1e6)
        os.remove("tmp.pth")
        with torch.no_grad():
            # unnormal = UnNormalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
            pbar = tqdm(enumerate(self.data_loader), total=len(self.data_loader))
            for step, (image, mask) in pbar:
                image = image.to(self.device)
                # image = unnormal(image.to(self.device))
                cur = time.time()
                result = self.net(image)
                inference_avg.update(time.time() - cur)

                mask = mask.to(self.device)

                avg_meter.update(iou_loss(result, mask))
                pbar.set_description(f"IOU: {avg_meter.avg:.4f} | "
                                     f"Model Size: {model_size} | Infernece Speed: {inference_avg.avg:.4f}")

                mask = mask.repeat_interleave(3, 1)
                argmax = torch.argmax(result, dim=1).unsqueeze(dim=1)
                result = result[:, 1, :, :].unsqueeze(dim=1)
                result = result * argmax
                result = result.repeat_interleave(3, 1)
                torch.cat([image, result, mask])
                bald_patch = (image * result)
                bald_patch = bald_patch.view(-1, *bald_patch.size()[2:])
                mask = mask.view(-1, *mask.size()[2:])
                # apply thresholdin 
                bald_patch =  bald_patch.permute(1, 2, 0).cpu().detach().numpy()
                mask =  mask.permute(1, 2, 0).cpu().detach().numpy()
                # bald_patch = bald_patch.cpu().detach().numpy()
                bald_patch = cv2.cvtColor(bald_patch, cv2.COLOR_BGR2GRAY)
                mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
                # save_image(torch.cat([image, result, mask]), os.path.join(self.sample_dir, f"{step}.jpg"))
                # save_image(torch.cat([(image * result), image, result, mask]), os.path.join(self.sample_dir, f"{step}.jpg"))
                # save_image(blackAndWhiteImage, os.path.join(self.sample_dir, f"{step}.jpg"))
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
                image = image.view(-1, *image.size()[2:])
                # result = result.view(-1, *result.size()[2:])

                image =  image.permute(1, 2, 0).cpu().detach().numpy()
                # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                # result =  result.permute(1, 2, 0).cpu().detach().numpy()
                # cv2.putText(image, "g={}".format(proportion), (10, 30),
                #     cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                cv2.imshow("Image",image)
                cv2.imshow("bald patch & mask", np.hstack([bald_patch, mask]))
                cv2.waitKey(0)
                cv2.destroyAllWindows() 

