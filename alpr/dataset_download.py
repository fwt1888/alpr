import fiftyone as fo
import fiftyone.zoo as foz

# 载入quickstart数据集
# dataset = foz.load_zoo_dataset("quickstart")
# # 可视化数据集
# session = fo.launch_app(dataset)

dataset = foz.load_zoo_dataset(
    "open-images-v7",
    split="train",
    label_types=["detections"],  # 下载目标检测标注文件
    classes=["Vehicle registration plate"],  # 下载数据集中的某个类别
    max_samples=10,  # 下载图片数目
    only_matching=True,  # 只下载匹配到类别的图片
    dataset_dir="./test_data",  # 下载到当前目录
)


