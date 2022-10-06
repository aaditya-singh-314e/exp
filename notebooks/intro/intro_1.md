```python
import pandas as pd
```


```python
import requests
from PIL import Image
```


```python
image = Image.open(requests.get('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-cat-photos-1593441022.jpg?crop=0.669xw:1.00xh;0.166xw,0&resize=640:*', stream=True).raw)
```


```python
!ls ../merge_xls/output/Combined_Payers_with_IDs.csv
```

    ls: cannot access '../merge_xls/output/Combined_Payers_with_IDs.csv': No such file or directory



```python
df = pd.read_csv('../../../../314e/merge_xls/output/Combined_Payers_with_IDs.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Payer Name</th>
      <th>Payer ID</th>
      <th>Availity Payer ID</th>
      <th>Change HC Payer ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1199 NATIONAL BENEFIT FUND</td>
      <td>13162</td>
      <td>13162</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AARP UNITEDHEALTHCARE INSURANCE COMPANY</td>
      <td>36273</td>
      <td>36273</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABSOLUTE TOTAL CARE</td>
      <td>68069</td>
      <td>68069</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ABSOLUTE TOTAL CARE</td>
      <td>-</td>
      <td>-</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ACS BENEFIT SERVICES</td>
      <td>11009</td>
      <td>11009</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>4307</th>
      <th>4308</th>
      <th>4309</th>
      <th>4310</th>
      <th>4311</th>
      <th>4312</th>
      <th>4313</th>
      <th>4314</th>
      <th>4315</th>
      <th>4316</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Payer Name</th>
      <td>1199 NATIONAL BENEFIT FUND</td>
      <td>AARP UNITEDHEALTHCARE INSURANCE COMPANY</td>
      <td>ABSOLUTE TOTAL CARE</td>
      <td>ABSOLUTE TOTAL CARE</td>
      <td>ACS BENEFIT SERVICES</td>
      <td>ADMINISTRATIVE SERVICES INCORPORATED</td>
      <td>ADVANTRA FREEDOM</td>
      <td>AETNA</td>
      <td>AETNA BETTER HEALTH</td>
      <td>AETNA INSURANCE COMPANY</td>
      <td>...</td>
      <td>TriCare West Region</td>
      <td>Tricare (CHAMPUS)</td>
      <td>Tricare (CHAMPUS)</td>
      <td>Tricare East Region</td>
      <td>Tricare East Region</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>First Managed Care Options Inc.</td>
      <td>First Managed Care Options Inc.</td>
    </tr>
    <tr>
      <th>Payer ID</th>
      <td>13162</td>
      <td>36273</td>
      <td>68069</td>
      <td>-</td>
      <td>11009</td>
      <td>ASINC</td>
      <td>25152</td>
      <td>AETNA</td>
      <td>ABH01</td>
      <td>60054</td>
      <td>...</td>
      <td>TRICE</td>
      <td>80</td>
      <td>80</td>
      <td>TREST</td>
      <td>TREST</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40270</td>
      <td>40270</td>
    </tr>
    <tr>
      <th>Availity Payer ID</th>
      <td>13162</td>
      <td>36273</td>
      <td>68069</td>
      <td>-</td>
      <td>11009</td>
      <td>ASINC</td>
      <td>25152</td>
      <td>AETNA</td>
      <td>ABH01</td>
      <td>60054</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Change HC Payer ID</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>TRICE</td>
      <td>80</td>
      <td>80</td>
      <td>TREST</td>
      <td>TREST</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40270</td>
      <td>40270</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 4317 columns</p>
</div>




```python
df.shape
```




    (4317, 4)




```python
a = 2
```


```python
# I AM NOT DONE
```


```python
def double_array(a):
    raise Exception('lol')
    return [x * 2 for x in a]
```
