
import torch
import torchvision

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    print("HELLO pytorch {}".format(torch.__version__))
    print("torchvision.version:", torchvision.__version__)
    print("torch.cuda.is_available? ", torch.cuda.is_available())

    x = torch.rand(3, 6)
    print(x)
