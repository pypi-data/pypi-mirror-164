# AUTOGENERATED! DO NOT EDIT! File to edit: 05_training_day_by_day_models.ipynb (unless otherwise specified).

__all__ = ['load_cfg', 'FINAL_CFG', 'DICT_FEATURES', 'prep_data', 'neptune', 'lgb_daily', 'cli_lgb_daily']

# Cell
#export
import os
import logging
import collections
import gc
import json
import time
import pickle
from itertools import chain
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import lightgbm as lgb
from lightgbm.callback import record_evaluation
from sklearn.model_selection import train_test_split
import neptune.new as neptune
from neptune.new.integrations.lightgbm import NeptuneCallback, create_booster_summary
from fastcore.script import call_parse, Param

from ..core import load_features, time_taken, load_file
from .fe import make_grid_df
from .metric import WRMSSE

# Cell
def load_cfg(path_cfg):
    if type(path_cfg) == str:
        with open(path_cfg, 'r') as f: return json.load(f)
    else: return  path_cfg

# Cell
FINAL_CFG = {'start_test': 1942,
 'start_train': 140,
 'days_to_predict': 'all',
 'fobj': 'mse',
 'fobj_weight_col': 'total_scaled_weight',
 'weight_hess': 1,
 'feval': 'mse',
 'feval_weight_col': 'scale',
 'weight_col': None,
 'lgb_params': {'boosting_type': 'gbdt',
  'objective': None,
  'metric': None,
  'subsample': 0.5,
  'subsample_freq': 1,
  'learning_rate': 0.03,
  'num_leaves': 255,
  'min_data_in_leaf': 255,
  'feature_fraction': 0.8,
  'n_estimators': 5000,
  'early_stopping_rounds': 50,
  'device_type': 'cpu',
  'seed': 42,
  'verbose': -1},
 'target': 'sales',
 'p_horizon': 28,
 'num_series': 30490,
 'features_json': 'pkl_final_features.json',
 'path_data_raw': 'data/raw',
 'path_features': 'data/features',
 'path_models': 'data/models',
 'use_neptune': 0,
 'neptune_project': 0,
 'neptune_api_token': None}

DICT_FEATURES = {
"fe_base.csv": [
"dept_id",
"store_id"
],
"fe_cal.csv": [
"event_name_1",
"tm_d",
"tm_w",
"tm_m",
"tm_dw",
"tm_w_end"
],
"fe_price.csv": [
"sell_price",
"price_min",
"price_max",
"price_median",
"price_mode",
"price_mean",
"price_std",
"price_norm_max",
"price_norm_mode",
"price_norm_mean",
"price_momentum",
"price_roll_momentum_4",
"price_roll_momentum_24",
"price_end_digits"
],
"fe_snap_event.csv": [
"snap_transform_1",
"snap_transform_2",
"next_event_type_1",
"last_event_type_1",
"days_since_event",
"days_until_event"
],
"shift_fe_dow_means_and_days_since_sale.csv": [
"mean_4_dow_0",
"mean_4_dow_1",
"mean_4_dow_2",
"mean_4_dow_3",
"mean_4_dow_4",
"mean_4_dow_5",
"mean_4_dow_6",
"mean_20_dow_0",
"mean_20_dow_1",
"mean_20_dow_2",
"mean_20_dow_3",
"mean_20_dow_4",
"mean_20_dow_5",
"mean_20_dow_6",
"days_since_sale"
],
"shift_fe_ipca_15_84.csv": [
"index",
"ipca_15_84_comp_1",
"ipca_15_84_comp_2",
"ipca_15_84_comp_3",
"ipca_15_84_comp_4",
"ipca_15_84_comp_5",
"ipca_15_84_comp_6",
"ipca_15_84_comp_7",
"ipca_15_84_comp_8",
"ipca_15_84_comp_9",
"ipca_15_84_comp_10",
"ipca_15_84_comp_11",
"ipca_15_84_comp_12",
"ipca_15_84_comp_13",
"ipca_15_84_comp_14"
],
"shift_fe_lags_1_14.csv": [
"lag_1",
"lag_2",
"lag_3",
"lag_4",
"lag_5",
"lag_6",
"lag_7",
"lag_8",
"lag_9",
"lag_10",
"lag_11",
"lag_12",
"lag_13",
"lag_14"
],
"shift_fe_rw_1.csv": [
"shift_1_rolling_nanmean_3",
"shift_1_rolling_mean_decay_3",
"shift_1_rolling_nanmean_7",
"shift_1_rolling_mean_decay_7",
"shift_1_rolling_nanstd_7"
],
"shift_fe_rw_2.csv": [
"shift_1_rolling_nanmean_14",
"shift_1_rolling_mean_decay_14",
"shift_1_rolling_diff_nanmean_14",
"shift_1_rolling_nanstd_14",
"shift_1_rolling_nanmean_30",
"shift_1_rolling_mean_decay_30"
],
"shift_fe_rw_3.csv": [
"shift_1_rolling_nanmean_60",
"shift_1_rolling_nanmedian_60",
"shift_1_rolling_mean_decay_60",
"shift_1_rolling_nanstd_60",
"shift_1_rolling_nanmean_140",
"shift_1_rolling_mean_decay_140",
"shift_1_rolling_nanstd_140"
],
"shift_fe_shifts_mom_1.csv": [
"shift_8_rolling_nanmean_7",
"momentum_7_rolling_nanmean_7",
"shift_8_rolling_mean_decay_7",
"momentum_7_rolling_mean_decay_7",
"momentum_7_rolling_diff_nanmean_7",
"shift_29_rolling_nanmean_7",
"momentum_28_rolling_nanmean_7",
"shift_29_rolling_mean_decay_7",
"momentum_28_rolling_mean_decay_7",
"shift_29_rolling_diff_nanmean_7",
"momentum_28_rolling_diff_nanmean_7"
],
"shift_fe_shifts_mom_2.csv": [
"shift_8_rolling_nanmean_30",
"momentum_7_rolling_nanmean_30",
"shift_8_rolling_mean_decay_30",
"shift_29_rolling_nanmean_30",
"momentum_28_rolling_nanmean_30",
"shift_29_rolling_mean_decay_30"
],
"shift_fe_shifts_mom_3.csv": [
"shift_29_rolling_nanmean_60",
"shift_91_rolling_nanmean_60",
"shift_91_rolling_mean_decay_60"
]
}

# Cell
def prep_data(cfg):
    df_stv = pd.read_csv(os.path.join(cfg['path_data_raw'], 'sales_train_evaluation.csv'))
    grid_df, _ = make_grid_df(df_stv)

    # Only use items with at least 68 days of sales
    first_sale = grid_df[grid_df.sales.notnull()].drop_duplicates('id')
    keep_id = first_sale[(cfg['start_test'] - first_sale.d) >= 68].id.tolist()
    df_stv_trunc = df_stv[df_stv.id.isin(keep_id)]
    grid_df = grid_df[grid_df.id.isin(keep_id)]

    #################### full valid and test sets ###################
    valid_days = [cfg['start_test'] + d - cfg['p_horizon'] for d in range(cfg['p_horizon'])]
    valid_actuals = df_stv_trunc[[f'd_{d}' for d in valid_days]].values
    e = WRMSSE(cfg['path_data_raw'], cfg['start_test'], df_stv_trunc=df_stv_trunc)
    if cfg['fobj_weight_col'] == 'total_scaled_weight': e.add_total_scaled_weight()
    if cfg['start_test'] != 1942: test_actuals = e.actuals.copy()
    prediction_df = df_stv_trunc[['id']]

    return grid_df, prediction_df, valid_actuals, e

# Cell
def neptune(cfg):
    """Not implemented"""
    if os.getenv('NEPTUNE_API_KEY'):
        pass

# Cell
def lgb_daily(path_cfg: str='cfg.json'):
    """Train 1 model for each day of prediction accoring to `path_cfg`."""

    if os.path.exists(path_cfg):
        cfg = load_cfg(path_cfg)
    else:
        cfg = FINAL_CFG
        path_cfg = 'final_cfg'
    full_grid_df, prediction_df, valid_actuals, e = prep_data(cfg)

    start_time = time.time()
    dict_eval_logs = [] # For experiment tracking
    ############### Day by day training and predicting #############
    if cfg['days_to_predict'] == "all": cfg['days_to_predict'] = range(28)
    for day_of_horizon in cfg['days_to_predict']:

        # Starting with full data and filtering for same day of week
        grid_df = full_grid_df.copy()
        test_day = cfg['start_test'] + day_of_horizon
        valid_day = test_day - 28
        same_day_of_week = [d for d in range(cfg['start_train'], test_day + 1) if d%7 == (test_day)%7]
        grid_df = grid_df[grid_df.d.isin(same_day_of_week)]

        if os.path.exists(path_cfg):
            with open(cfg['features_json'], 'r') as f:
                dict_features = json.load(f)
        else:
            dict_features = DICT_FEATURES

        index = grid_df.index
        grid_df = pd.concat([
                    grid_df,
                    load_features(cfg['path_features'], dict_features, reindex_with=index,
                                  shift_index=cfg['num_series'] * day_of_horizon)
                ], axis=1)

        remove_features = ['id', 'd', cfg['target']]
        feature_cols = [col for col in list(grid_df) if col not in remove_features]

        ################## test, train and valid set ####################
        valid_mask = (grid_df.d == valid_day)
        train_mask = (grid_df.d >= cfg['start_train']) & (grid_df.d < valid_day) & (grid_df[cfg['target']].notnull())
        test_mask = (grid_df.d == test_day)

        train_x, train_y = grid_df[train_mask][feature_cols], grid_df[train_mask][cfg['target']]
        valid_x, valid_y = grid_df[valid_mask][feature_cols], grid_df[valid_mask][cfg['target']]
        test_x, test_y = grid_df[test_mask][feature_cols], grid_df[test_mask][cfg['target']]

        ################## Fit custom objective and metric ##################
        w_12_train = e.w_12.reindex(grid_df[train_mask].id)
        w_12_eval = e.w_12.reindex(grid_df[valid_mask].id)
        w_12_test = e.w_12.reindex(grid_df[test_mask].id)

        if cfg['fobj']:
            get_fobj = getattr(e, f'get_weighted_{cfg["fobj"]}_fobj')
            fobj = get_fobj(w_12_train, cfg['fobj_weight_col'], cfg['weight_hess'])
        else:
            fobj = None

        if cfg['feval']:
            if cfg['feval'] == 'feval':
                feval = e.feval
            else:
                get_feval = getattr(e, f'get_weighted_{cfg["feval"]}_feval')
                feval = get_feval(w_12_eval, cfg['feval_weight_col'])
        else:
            feval = None

        # Set evaluator actuals to valid day for early stopping
        e.actuals = valid_actuals[:, day_of_horizon].reshape((-1,1))

        ############# lightgbm datasets for training #############
        if cfg['weight_col']:
            weight_train = w_12_train[cfg['weight_col']].values
            weight_eval = w_12_eval[cfg['weight_col']].values
            weight_test = w_12_test[cfg['weight_col']].values
        else:
            weight_train, weight_eval, weight_test = None, None, None
        train_data = lgb.Dataset(train_x, label=train_y, weight=weight_train)
        valid_data = lgb.Dataset(valid_x, label=valid_y, weight=weight_eval)
        test_data = lgb.Dataset(test_x, label=test_y, weight=weight_test)

        ####################### Training ##########################
        dict_eval_log = {}
        estimator = lgb.train(
            cfg['lgb_params'],
            train_set=train_data,
            valid_sets=[valid_data],
            valid_names=['valid'],
            fobj = fobj,
            feval = feval,
            callbacks=[record_evaluation(dict_eval_log)],
        )
        booster_summary = create_booster_summary(booster=estimator, max_num_features=25)
        cfg[f'bs_{day_of_horizon}'] = booster_summary
        dict_eval_logs.append(dict_eval_log)

        preds = estimator.predict(test_x)
        prediction_df.loc[:, f'F{day_of_horizon + 1}'] = preds
        gc.collect()

    # Saving predictions in submission ready format
    tmp = prediction_df.copy()
    prediction_df.id = prediction_df.id.str.replace('evaluation', 'validation')
    prediction_df = pd.concat([prediction_df, tmp])
    path = 'lgb_daily' + '_' + Path(path_cfg).stem + '_' + 'submission.csv'
    prediction_df.to_csv(path, index=False)

    neptune(cfg)
    time_taken(start_time)

@call_parse
def cli_lgb_daily(path_cfg: Param('path to the configuration json', str)='cfg.json'):
    lgb_daily(path_cfg)