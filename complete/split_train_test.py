import os
import random
import shutil


def split_train_test(src,test_rate=0.2):
    images = [_ for _ in os.listdir(src) if _.endswith('jpg')]
    n_test= round(len(images)*test_rate)
    test_idx = random.sample(range(len(images)),n_test)
    train_idx = [_ for _ in range(len(images)) if _ not in test_idx]
    imtest = [images[i] for i in test_idx]
    imtrain = [images[i] for i in train_idx]
    traindst = os.path.join(src,'train')
    if not os.path.exists(traindst): os.mkdir(traindst)
    for im in imtrain:
        shutil.move(os.path.join(src,im),os.path.join(traindst,im))
    testdst = os.path.join(src,'test')
    if not os.path.exists(testdst): os.mkdir(testdst)
    for im in imtest:
        shutil.move(os.path.join(src,im),os.path.join(testdst,im))

if __name__ == "__main__":
    src = r'\\fatherserverdw\Saurabh\Saurabh\Pancreas_Ashley_Files\20x registered cropped region\tiles_of_slide1'
    split_train_test(src,0.2) #split 20% as test set
