# Autogenerated by nbdev

d = { 'settings': { 'allowed_cell_metadata_keys': '',
                'allowed_metadata_keys': '',
                'audience': 'Developers',
                'author': 'Chris Richard Miles',
                'author_email': 'chrisrichardmiles@gmail.com',
                'black_formatting': 'False',
                'branch': 'master',
                'clean_ids': 'True',
                'console_scripts': 'crm_mkdirs_data=chrisrichardmiles.core:cli_mkdirs_data\n'
                                   'crm_cp_tree=chrisrichardmiles.core:cp_tree\n'
                                   'crm_fe_dict=chrisrichardmiles.core:fe_dict\n'
                                   'crm_download_kaggle_data=chrisrichardmiles.core:cli_download_kaggle_data\n'
                                   'crm_m5_hello_world=chrisrichardmiles.m5.scripts:hello_world\n'
                                   '\n'
                                   'crm_m5_fe_base_features=chrisrichardmiles.m5.fe:fe_base_features\n'
                                   'crm_m5_fe_encodings=chrisrichardmiles.m5.fe:fe_encodings\n'
                                   'crm_m5_fe_lags=chrisrichardmiles.m5.fe:fe_lags\n'
                                   'crm_m5_fe_rw_stats=chrisrichardmiles.m5.fe:fe_rw_stats\n'
                                   'crm_m5_fe_shifts_momentum=chrisrichardmiles.m5.fe:fe_shifts_momentum\n'
                                   'crm_m5_fe_test=chrisrichardmiles.m5.fe:test\n'
                                   'crm_m5_fe_dow_means=chrisrichardmiles.m5.fe:fe_dow_means\n'
                                   'crm_m5_fe_ipca_lags=chrisrichardmiles.m5.fe:fe_ipca_lags\n'
                                   'crm_m5_fe=chrisrichardmiles.m5.fe:fe\n'
                                   '\n'
                                   'crm_m5_lgb_daily=chrisrichardmiles.m5.daily_models:cli_lgb_daily\n'
                                   '\n'
                                   'crm_m5_make_oos_data=chrisrichardmiles.m5.oos:make_oos_data',
                'copyright': 'Chris Richard Miles',
                'custom_sidebar': 'False',
                'description': 'Helpful tools for machine learning and coding.',
                'doc_baseurl': '/chrisrichardmiles/',
                'doc_host': 'https://chrisrichardmiles.github.io',
                'doc_path': 'docs',
                'git_url': 'https://github.com/chrisrichardmiles/chrisrichardmiles/tree/master/',
                'host': 'github',
                'jupyter_hooks': 'True',
                'keywords': 'machine learning coding',
                'language': 'English',
                'lib_name': 'chrisrichardmiles',
                'lib_path': 'chrisrichardmiles',
                'license': 'apache2',
                'min_python': '3.6',
                'nbs_path': '.',
                'readme_nb': 'index.ipynb',
                'recursive': 'True',
                'requirements': 'pandas matplotlib seaborn scipy psutil lightgbm neptune-client \\\nneptune-lightgbm psutil kaggle',
                'status': '2',
                'title': 'chrisrichardmiles',
                'tst_flags': 'no_test',
                'user': 'chrisrichardmiles',
                'version': '0.0.1'},
  'syms': { 'chrisrichardmiles.core': { 'chrisrichardmiles.core.cli_download_kaggle_data': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#cli_download_kaggle_data',
                                        'chrisrichardmiles.core.cli_mkdirs_data': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#cli_mkdirs_data',
                                        'chrisrichardmiles.core.cp_tree': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#cp_tree',
                                        'chrisrichardmiles.core.download_kaggle_data': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#download_kaggle_data',
                                        'chrisrichardmiles.core.fe_dict': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#fe_dict',
                                        'chrisrichardmiles.core.get_file_cols_dict': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#get_file_cols_dict',
                                        'chrisrichardmiles.core.get_memory_usage': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#get_memory_usage',
                                        'chrisrichardmiles.core.load_features': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#load_features',
                                        'chrisrichardmiles.core.load_file': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#load_file',
                                        'chrisrichardmiles.core.make_unique': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#make_unique',
                                        'chrisrichardmiles.core.make_unique_path': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#make_unique_path',
                                        'chrisrichardmiles.core.merge_by_concat': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#merge_by_concat',
                                        'chrisrichardmiles.core.mkdirs_data': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#mkdirs_data',
                                        'chrisrichardmiles.core.pool_func': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#pool_func',
                                        'chrisrichardmiles.core.reduce_mem_usage': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#reduce_mem_usage',
                                        'chrisrichardmiles.core.save_file': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#save_file',
                                        'chrisrichardmiles.core.sizeof_fmt': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#sizeof_fmt',
                                        'chrisrichardmiles.core.time_taken': 'https://chrisrichardmiles.github.io/chrisrichardmiles/core.html#time_taken'},
            'chrisrichardmiles.m5.daily_models': { 'chrisrichardmiles.m5.daily_models.cli_lgb_daily': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.daily_models.html#cli_lgb_daily',
                                                   'chrisrichardmiles.m5.daily_models.lgb_daily': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.daily_models.html#lgb_daily',
                                                   'chrisrichardmiles.m5.daily_models.load_cfg': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.daily_models.html#load_cfg',
                                                   'chrisrichardmiles.m5.daily_models.neptune': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.daily_models.html#neptune',
                                                   'chrisrichardmiles.m5.daily_models.prep_data': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.daily_models.html#prep_data'},
            'chrisrichardmiles.m5.fe': { 'chrisrichardmiles.m5.fe.add_base': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_base',
                                         'chrisrichardmiles.m5.fe.add_cal_fe': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_cal_fe',
                                         'chrisrichardmiles.m5.fe.add_dow_means': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_dow_means',
                                         'chrisrichardmiles.m5.fe.add_event_features': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_event_features',
                                         'chrisrichardmiles.m5.fe.add_lags': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_lags',
                                         'chrisrichardmiles.m5.fe.add_price_fe': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_price_fe',
                                         'chrisrichardmiles.m5.fe.add_rolling_cols': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_rolling_cols',
                                         'chrisrichardmiles.m5.fe.add_shift_cols': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_shift_cols',
                                         'chrisrichardmiles.m5.fe.add_snap_transform_1': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_snap_transform_1',
                                         'chrisrichardmiles.m5.fe.add_snap_transform_2': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#add_snap_transform_2',
                                         'chrisrichardmiles.m5.fe.create_price_fe': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#create_price_fe',
                                         'chrisrichardmiles.m5.fe.diff_mean': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#diff_mean',
                                         'chrisrichardmiles.m5.fe.diff_nanmean': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#diff_nanmean',
                                         'chrisrichardmiles.m5.fe.encode_target': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#encode_target',
                                         'chrisrichardmiles.m5.fe.fe': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe',
                                         'chrisrichardmiles.m5.fe.fe_base_features': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_base_features',
                                         'chrisrichardmiles.m5.fe.fe_dow_means': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_dow_means',
                                         'chrisrichardmiles.m5.fe.fe_encodings': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_encodings',
                                         'chrisrichardmiles.m5.fe.fe_ipca_lags': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_ipca_lags',
                                         'chrisrichardmiles.m5.fe.fe_lags': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_lags',
                                         'chrisrichardmiles.m5.fe.fe_rw_stats': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_rw_stats',
                                         'chrisrichardmiles.m5.fe.fe_shifts_momentum': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#fe_shifts_momentum',
                                         'chrisrichardmiles.m5.fe.get_days_since_sale': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#get_days_since_sale',
                                         'chrisrichardmiles.m5.fe.make_grid_df': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#make_grid_df',
                                         'chrisrichardmiles.m5.fe.make_lag_col': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#make_lag_col',
                                         'chrisrichardmiles.m5.fe.make_rolling_col': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#make_rolling_col',
                                         'chrisrichardmiles.m5.fe.mean_decay': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#mean_decay',
                                         'chrisrichardmiles.m5.fe.nan_leading_zeros': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#nan_leading_zeros',
                                         'chrisrichardmiles.m5.fe.rolling_window': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#rolling_window',
                                         'chrisrichardmiles.m5.fe.split_array': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.fe.html#split_array'},
            'chrisrichardmiles.m5.metric': { 'chrisrichardmiles.m5.metric.WRMSSE': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse',
                                             'chrisrichardmiles.m5.metric.WRMSSE.add_total_scaled_weight': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.add_total_scaled_weight',
                                             'chrisrichardmiles.m5.metric.WRMSSE.dump_scores': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.dump_scores',
                                             'chrisrichardmiles.m5.metric.WRMSSE.feval': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.feval',
                                             'chrisrichardmiles.m5.metric.WRMSSE.get_oos_scale': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.get_oos_scale',
                                             'chrisrichardmiles.m5.metric.WRMSSE.get_weighted_mae_feval': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.get_weighted_mae_feval',
                                             'chrisrichardmiles.m5.metric.WRMSSE.get_weighted_mae_fobj': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.get_weighted_mae_fobj',
                                             'chrisrichardmiles.m5.metric.WRMSSE.get_weighted_mse_feval': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.get_weighted_mse_feval',
                                             'chrisrichardmiles.m5.metric.WRMSSE.get_weighted_mse_fobj': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.get_weighted_mse_fobj',
                                             'chrisrichardmiles.m5.metric.WRMSSE.make_sub': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.make_sub',
                                             'chrisrichardmiles.m5.metric.WRMSSE.plot_scores': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.plot_scores',
                                             'chrisrichardmiles.m5.metric.WRMSSE.score': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#wrmsse.score',
                                             'chrisrichardmiles.m5.metric.append_df_unique_id': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#append_df_unique_id',
                                             'chrisrichardmiles.m5.metric.combine_cols': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#combine_cols',
                                             'chrisrichardmiles.m5.metric.get_agg': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#get_agg',
                                             'chrisrichardmiles.m5.metric.get_df_weights': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.metric.html#get_df_weights'},
            'chrisrichardmiles.m5.oos': { 'chrisrichardmiles.m5.oos.get_series_df': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.oos.html#get_series_df',
                                          'chrisrichardmiles.m5.oos.get_stats_df': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.oos.html#get_stats_df',
                                          'chrisrichardmiles.m5.oos.make_oos_data': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.oos.html#make_oos_data',
                                          'chrisrichardmiles.m5.oos.plot_all_item_series': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.oos.html#plot_all_item_series',
                                          'chrisrichardmiles.m5.oos.plot_item_series': 'https://chrisrichardmiles.github.io/chrisrichardmiles/m5.oos.html#plot_item_series'}}}