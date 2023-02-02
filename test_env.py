import os
import torch

print('java -version')
os.system('java -version')

assert torch.cuda.is_available()
print(f'torch.cuda.is_available(): {torch.cuda.is_available()}')