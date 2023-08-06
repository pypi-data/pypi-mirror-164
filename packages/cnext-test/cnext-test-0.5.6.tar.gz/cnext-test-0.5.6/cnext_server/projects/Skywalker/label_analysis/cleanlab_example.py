# !pip install torch
# !pip install scikit-learn
# !pip install cleanlab

import numpy as np
import torch
import warnings
import glob
import pandas as pd
from torch import nn
from sklearn.datasets import fetch_openml
from skorch import NeuralNetClassifier
from sklearn.model_selection import cross_val_predict
from cleanlab.filter import find_label_issues
 
SEED = 123
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
torch.cuda.manual_seed_all(SEED)
warnings.filterwarnings("ignore", "Lazy modules are a new feature.*")

mnist = fetch_openml("mnist_784")  # Fetch the MNIST dataset

X = mnist.data.astype("float32").to_numpy() # 2D array (images are flattened into 1D)
X /= 255.0  # Scale the features to the [0, 1] range
X = X.reshape(len(X), 1, 28, 28)  # reshape into [N, C, H, W] for PyTorch

y = mnist.target.astype("int64").to_numpy()  # 1D array of labels

class ClassifierModule(nn.Module):
    def __init__(self):
        super().__init__()

        self.cnn = nn.Sequential(
            nn.Conv2d(1, 6, 3),
            nn.ReLU(),
            nn.BatchNorm2d(6),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(6, 16, 3),
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.out = nn.Sequential(
            nn.Flatten(),
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.Linear(128, 10),
            nn.Softmax(dim=-1),
        )

    def forward(self, X):
        X = self.cnn(X)
        X = self.out(X)
        return X

model_skorch = NeuralNetClassifier(ClassifierModule)
num_crossval_folds = 3  # for efficiency; values like 5 or 10 will generally work better
pred_probs = cross_val_predict(
    model_skorch,
    X,
    y,
    cv=num_crossval_folds,
    method="predict_proba",
)

ranked_label_issues = find_label_issues(
    y,
    pred_probs,
    return_indices_ranked_by="self_confidence",
)

print(f"Cleanlab found {len(ranked_label_issues)} label issues.")
print(f"Top 15 most likely label errors: \n {ranked_label_issues[:15]}")

train_dir = "data/mnist_png/train/*/*"
val_dir = "data/mnist_png/valid/*/*"
train_files = glob.glob(train_dir)
val_files = glob.glob(val_dir)
img_files = {}
for fn in train_files:
    img_files[int(fn.split('/')[-1].split('.')[0])] = fn
for fn in val_files:
    img_files[60000+int(fn.split('/')[-1].split('.')[0])] = fn
top_label_issues = ranked_label_issues[range(100)]
 
data = {
    'error_rank': range(100),
    'data_id': top_label_issues,
    'label': [y[k] for k in top_label_issues],
    'image': [img_files[k] for k in top_label_issues]
}
df = pd.DataFrame(data=data)
df['image'] = df['image'].astype('file/png')
df.sort_values(by=['error_rank'], inplace=True)
