import pandas as pd
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_file(path, dtype=None):
    if path.split('.')[-1] == 'csv':
        df = pd.read_csv(path, dtype=dtype)
    else:
        df = pd.read_excel(path, dtype=dtype)

    return df

def read_dir(path, variables, col_start=15, col_end=-1):
    df = pd.DataFrame()

    for file in os.listdir(path):
        temp = read_file(f'{path}/{file}', dtype=str)
        temp[variables] = temp[temp.columns[col_start:col_end]].apply(
            lambda x: ', '.join(
                f'{col}:{val}' for col, val in zip(x.index, x.values)
            ), axis=1
        )
        temp = temp[[*temp.columns[:col_start], temp.columns[col_end]]]

        df = pd.concat([df, temp])

    return df

def write_excel_width(df, var, dest):
    for i in df[var].unique():
        writer = pd.ExcelWriter(f'{dest}/Anomali_{i}.xlsx')
        df.loc[df[var]==i].to_excel(
            writer,
            sheet_name='Sheet1',
            index=False,
            freeze_panes=(1, 1),
            na_rep='NaN'
        )

        for column in df:
            column_length = max(
                df[column].astype(str).map(len).max(),
                len(column)
            )+5

            col_idx = df.columns.get_loc(column)
            writer.sheets['Sheet1'].set_column(col_idx, col_idx, column_length)

        writer.close()
        
def write_excel(df, var, dest):
    for i in df[var].unique():
        df.loc[df[var]==i].to_excel(f'{dest}/Anomali_{i}.xlsx')

def check_button(driver, xpath):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        button.click()

    except:
        pass