C:
del /Q C:\Users\isica\Desktop\predict\*.*
D:
cd D:\tensorflow-models-master-2018-5\research\deeplab

cd D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\train
del /Q *.*
cd D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\eval
del /Q *.*
cd D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\export
del /Q *.*
cd D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\vis
del /Q *.*
cd D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\vis\raw_segmentation_results
del /Q *.*
cd D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\vis\segmentation_results
del /Q *.*
cd D:\tensorflow-models-master-2018-5\research\deeplab

sh ./ISIC_run.sh
xcopy /s D:\tensorflow-models-master-2018-5\research\deeplab\datasets\pascal_voc_seg\exp\train_on_trainval_set\vis\segmentation_results C:\Users\isica\Desktop\predict
D:
cd D:\tensorflow-models-master-2018-5\research\deeplab\utils
python jaccard.py

