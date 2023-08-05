import torch.utils.model_zoo

from .modelv1 import *
from .modelv2 import *
from .quantization.modelv1 import *
from .quantization.modelv2 import *

url_map = {
    'hairmattenetv1': 'https://github.com/wonbeomjang/mobile-hair-segmentation-pytorch/releases/download/paramter/hairmattenet_v1.pth',
    'hairmattenetv2': 'https://github.com/wonbeomjang/mobile-hair-segmentation-pytorch/releases/download/paramter/hairmattenet_v2.pth',
    'quantized_hairmattenetv1': 'https://github.com/wonbeomjang/mobile-hair-segmentation-pytorch/releases/download/paramter/quantized_hairmattenet_v1.pth',
    'quantized_hairmattenetv2': 'https://github.com/wonbeomjang/mobile-hair-segmentation-pytorch/releases/download/paramter/quantized_hairmattenet_v2.pth'}

model_map = {'hairmattenetv1': MobileHairNet,
             'hairmattenetv2': MobileHairNetV2,
             'quantized_hairmattenetv1': QuantizableMobileHairNet,
             'quantized_hairmattenetv2': QuantizableMobileHairNetV2}


def _model(arch: str, pretrained: bool, device=None, quantize=False):
    print(f"[*] Load {arch}")
    device = device if device is not None else torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model: nn.Module = model_map[arch]()

    if pretrained:
        model = model.to(device)
        state_dict = torch.utils.model_zoo.load_url(url_map[arch], map_location=device)
        if quantize:
            model.quantize()
        model.load_state_dict(state_dict)

    return model


def modelv1(pretrained=False, device=None):
    return _model('hairmattenetv1', pretrained, device)


def modelv2(pretrained=False, device=None):
    return _model('hairmattenetv2', pretrained, device)


def quantized_modelv1(pretrained=False, device=None):
    return _model('quantized_hairmattenetv1', pretrained, device, True)


def quantized_modelv2(pretrained=False, device=None):
    return _model('quantized_hairmattenetv2', pretrained, device, True)
