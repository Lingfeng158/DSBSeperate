
config = {'datapath': '/share2/gaor2/MCL/combine_withDSB',
          'preprocess_result_path': '/media/gaor2/8e7f6ccf-3585-4815-856e-80ce8754c5b5/data/TwoLungSet/second/DSB_File/prep',
          'bbox_result_path': '/media/gaor2/8e7f6ccf-3585-4815-856e-80ce8754c5b5/data/TwoLungSet/second/DSB_File/bbox',
          'outputfile': '/media/gaor2/8e7f6ccf-3585-4815-856e-80ce8754c5b5/data/TwoLungSet/second/kaggle_result.csv',
#           'prep_min': 0,
#           'prep_max': 116,

          'detector_model': 'net_detector',
          'detector_param': './model/detector.ckpt',
          'classifier_model': 'net_classifier',
          'classifier_param': './model/classifier.ckpt',
          'n_gpu': 1,
          'n_worker_preprocessing': 4,
          'use_exsiting_preprocessing': True,
          'skip_preprocessing': True,
          'skip_detect': True}



#118248time2001_pbb.npy not existed