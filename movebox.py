import numpy as np
import os
import pandas as pd
from layers import nms,iou
import nibabel as nib

dst="/share5/wangj46/318box/"
df=pd.read_csv("/share3/wangj46/final.csv")
s=set(df["share3_namepath"])

#d="76621363hehehe76621363slash20130228hehehe3slashxslashunknown_pbb.npy"

count=0
dirs=os.listdir("/share5/wangj46/DSB2017-1-master/bbox_result0")
for d in dirs:
    tmp=d.replace("slash","-").replace("star","*").replace("under","_").replace("dot",".")
    if(tmp.endswith("pbb.npy")):
        if(tmp[:-8] in s):
            count+=1
            img = np.load("/share5/wangj46/DSB2017-1-master/prep_result0/"+d.replace("pbb",'clean'))
            pbb = np.load("/share5/wangj46/DSB2017-1-master/bbox_result0/"+d)
            img=img.reshape(img.shape[1:])
            pbb = pbb[pbb[:,0]>-1]
            pbb = nms(pbb,0.05)
            
            mask=np.zeros(img.shape)
            for i in range(pbb.shape[0]):
                box = pbb[i].astype('int')[1:]
                mask[box[0]-box[3]:box[0]+box[3],box[1]-box[3]:box[1]+box[3],box[2]-box[3]:box[2]+box[3]]=1
            
            nii_img = nib.Nifti1Image(img, affine=np.eye(4))
            nii_mask = nib.Nifti1Image(mask, affine=np.eye(4))

            nib.save(nii_img, "/share5/wangj46/318box/img/"+tmp.replace("_pbb.npy",".nii.gz"))
            nib.save(nii_mask, "/share5/wangj46/318box/mask/"+tmp.replace("_pbb.npy",".nii.gz"))

#{'20509751935_20509751935-20101109hehehe20509751935_20509751935-20101109hehehe4-x-100MLOMNI350-x-100MLOMNI350'}
print(count)
