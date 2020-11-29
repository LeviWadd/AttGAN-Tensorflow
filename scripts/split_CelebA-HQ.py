import math
import os
import random

# ==============================================================================
# =                                   param                                    =
# ==============================================================================

label_file = './data/CelebAMask-HQ/CelebAMask-HQ-attribute-anno.txt'
save_dir = './data/CelebAMask-HQ'


# ==============================================================================
# =                                    run                                     =
# ==============================================================================

with open(label_file, 'r') as f:
    lines = f.readlines()[2:]

random.seed(100)
random.shuffle(lines)

train_ratio = 0.95
val_ratio = 0.025
test_ratio = 0.025

dataset_len = len(lines)

lines_train = lines[:math.ceil(train_ratio*dataset_len)]
lines_val = lines[math.ceil(train_ratio*dataset_len):math.ceil((train_ratio + val_ratio)*dataset_len)]
lines_test = lines[math.ceil((train_ratio + val_ratio)*dataset_len):]

with open(os.path.join(save_dir, 'train_label.txt'), 'w') as f:
    f.writelines(lines_train)

with open(os.path.join(save_dir, 'val_label.txt'), 'w') as f:
    f.writelines(lines_val)

with open(os.path.join(save_dir, 'test_label.txt'), 'w') as f:
    f.writelines(lines_test)
