config = {'datapath': '/share2/gaor2/SPORE/combine_withDSB',
          'preprocess_result_path': '/share2/gaor2/SPORE/DSB_File/prep',
          'bbox_result_path': '/share2/gaor2/SPORE/DSB_File/bbox',
          'feat_save_root': '/share2/gaor2/SPORE/featnpy',
          

          'detector_model': 'net_detector',
          'detector_param': './model/detector.ckpt',
          'classifier_model': 'net_classifier',
          'classifier_param': './model/classifier.ckpt',
          'n_gpu': 1,
          'n_worker_preprocessing': 2,
          'use_exsiting_preprocessing': True,
          'skip_preprocessing': True,
          'skip_detect': True}