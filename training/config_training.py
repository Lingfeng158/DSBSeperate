config = {'stage1_data_path':'NONE',
          'luna_raw':'/share5/huoy1/Luna16/raw/',
          'luna_segment':'/share5/huoy1/Luna16/seg-lungs-LUNA16/',
          
          'luna_data':'/share5/huoy1/Luna16/allset',
          'preprocess_result_path':'/share5/wangj46/DSB2017-1-master/preprocess/',       
          
          'luna_abbr':'./detector/labels/shorter.csv',
          'luna_label':'./detector/labels/lunaqualified.csv',
          'stage1_annos_path':['./detector/labels/label_job5.csv',
                './detector/labels/label_job4_2.csv',
                './detector/labels/label_job4_1.csv',
                './detector/labels/label_job0.csv',
                './detector/labels/label_qualified.csv'],
          'bbox_path':'../detector/results/res18/bbox/',
          'preprocessing_backend':'python'
         }
