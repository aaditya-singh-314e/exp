# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3.9.13 ('face')
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
import requests
from PIL import Image

# %%
Image.open(requests.get('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-cat-photos-1593441022.jpg?crop=0.669xw:1.00xh;0.166xw,0&resize=640:*', stream=True).raw)

# %%
# !ls ../merge_xls/output/Combined_Payers_with_IDs.csv

# %%
print(pd.read_csv('../merge_xls/output/Combined_Payers_with_IDs.csv'))


# %%
# I AM NOT DONE

# %%
def double_array(a):
    raise Exception('lol')
    return [x * 2 for x in a]
