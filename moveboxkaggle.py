import numpy as np
import os
import pandas as pd
from layers import nms,iou
import nibabel as nib

df=pd.read_csv("/share5/wangj46/stage1_labels.csv")
s=set(df["id"])

#d='11616de262f844e6542d3c65d9238b6e_pbb.npy'

count=0
dirs=os.listdir("/share5/wangj46/DSB2017-1-master/bbox_result")
for d in dirs:
    tmp=d
    if(tmp.endswith("pbb.npy")):
        if(tmp[:-8] in s):
            count+=1
            img = np.load("/share5/wangj46/DSB2017-1-master/prep_result/"+d.replace("pbb",'clean'))
            pbb = np.load("/share5/wangj46/DSB2017-1-master/bbox_result/"+d)
            img=img.reshape(img.shape[1:])
            pbb = pbb[pbb[:,0]>-1]
            pbb = nms(pbb,0.05)
            
            mask=np.zeros(img.shape)
            for i in range(pbb.shape[0]):
                box = pbb[i].astype('int')[1:]
                mask[box[0]-box[3]:box[0]+box[3],box[1]-box[3]:box[1]+box[3],box[2]-box[3]:box[2]+box[3]]=1
            
            nii_img = nib.Nifti1Image(img, affine=np.eye(4))
            nii_mask = nib.Nifti1Image(mask, affine=np.eye(4))

            nib.save(nii_img, "/media/masi/DATA/kagglebox/img/"+tmp.replace("_pbb.npy",".nii.gz"))
            nib.save(nii_mask, "/media/masi/DATA/kagglebox/mask/"+tmp.replace("_pbb.npy",".nii.gz"))
            print(tmp)
            
print(count)
