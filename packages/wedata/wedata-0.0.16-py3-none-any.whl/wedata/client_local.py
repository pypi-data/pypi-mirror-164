import os
import logging

import pandas as pd
import pyarrow.parquet as pq

from .client import BaseClient


def load_table(table: str, storage_dir: str, start_year: int, end_year: int):
    years = list(map(str, range(start_year, end_year+1)))
    file_list = [os.path.join(storage_dir, f'{table}_{year}.parquet') for year in years]
    if len(file_list) == 0:
        raise Exception(f"文件不存在，无法加载数据")
    for file in file_list:
        if not os.path.isfile(file):
            raise Exception(f"{file}文件不存在,无法加载全部数据")
    print("\n正在加载文件：")
    for file in file_list:
        print(f"    {file}")
    dataset = pq.ParquetDataset(file_list, use_legacy_dataset=True)
    print("加载数据完毕")
    df = dataset.read().to_pandas()
    return df


class LocalClient(BaseClient):
    def __init__(self, path):
        super().__init__()
        if not os.path.isdir(path):
            raise Exception(f"{path}该目录不存在")
        self.storage_path = path

    def extract_feature_exposure(self, param) -> pd.DataFrame:
        """直接取得特征暴露"""
        # todo 需要对参数校验
        table_name = "Features_Data"
        dir_name = "feature-exposure"
        storage_idr = os.path.join(self.storage_path, dir_name)
        if not os.path.isdir(storage_idr):
            raise Exception(f"{storage_idr}该目录不存在")
        try:
            factor_name = f"FACTOR_{param.get('class').split('_')[-1].upper()}"
            start_date = int(param.get("start_date"))
            end_date = int(param.get("end_date"))
            start_year = int(str(start_date)[0:4])
            end_year = int(str(end_date)[0:4])
        except Exception as e:
            raise Exception(e)

        df = load_table(table_name, storage_idr, start_year, end_year) # 加载数据
        df["TRADE_DT"] = pd.to_datetime(df['TRADE_DT'])
        # todo 增加筛选项
        try:
            res = df.query(f"TRADE_DT >= {start_date} and TRADE_DT <= {end_date}")[
                ["TRADE_DT", "STK_CODE", factor_name]]

            return res
        except Exception as e:
            raise Exception(e)

    def query(self, param):
        pass

    def extract(self, param):
        if param.get("domain") == "descriptor" and param.get("phylum") == "direct":
            return self.extract_feature_exposure(param)
        else:
            raise Exception("domain或phylum参数错误")
