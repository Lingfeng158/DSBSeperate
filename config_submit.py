
config = {'datapath': '/home/local/VANDERBILT/lil18/Desktop/gg',
          'preprocess_result_path': '/home/local/VANDERBILT/lil18/Desktop/out',
          'bbox_result_path': '/home/local/VANDERBILT/lil18/Desktop/bbox',
	  'outputfile':'prediction.csv',
          #'feat_save_root': '/share3/gaor2/share5backup/data/NLST/featnpy',
          #'outputfile': '/share3/gaor2/share5backup/data/MCL227_kaggle_result.csv',
          #'prep_min': 70,
          #'prep_max': 100,

          'detector_model': 'net_detector',
          'detector_param': './model/detector.ckpt',
          'classifier_model': 'net_classifier',
          'classifier_param': './model/classifier.ckpt',
          'n_gpu': 1,
          'n_worker_preprocessing': 1,
          'use_exsiting_preprocessing': False,
          'skip_preprocessing': False,
          'skip_detect': True}


'''
## config for not spread folder

'''


'''

## test config

config = {'datapath': '/share5/gaor2/data/tmp',
          'preprocess_result_path': './prep_test/',
          'bbox_result_path': './bbox_test',
          'outputfile': 'test.csv',

          'detector_model': 'net_detector',
          'detector_param': './model/detector.ckpt',
          'classifier_model': 'net_classifier',
          'classifier_param': './model/classifier.ckpt',
          'n_gpu': 1,
          'n_worker_preprocessing': 1,
          'use_exsiting_preprocessing': True,
          'skip_preprocessing': False,
          'skip_detect': False}
'''
