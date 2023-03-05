import os

ids = [
    "1JDXCwaFHJG3Uh_xHyMHJHImO6UiP-Yc2",
    "13bTo9IO7aYXKtEpzyhsNd6csJpVhA8lE"
]
for id in ids:
    os.system("gdown https://drive.google.com/uc?id={}".format(id))