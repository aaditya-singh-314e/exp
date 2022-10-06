```python
import pandas as pd
```


```python
import requests
from PIL import Image
```


```python
Image.open(requests.get('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-cat-photos-1593441022.jpg?crop=0.669xw:1.00xh;0.166xw,0&resize=640:*', stream=True).raw)
```




    
![png](intro_1_files/intro_1_2_0.png)
    




```python
!ls ../merge_xls/output/Combined_Payers_with_IDs.csv
```

    ../merge_xls/output/Combined_Payers_with_IDs.csv



```python
print(pd.read_csv('../merge_xls/output/Combined_Payers_with_IDs.csv'))
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
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4312</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4313</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4314</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4315</th>
      <td>First Managed Care Options Inc.</td>
      <td>40270</td>
      <td>NaN</td>
      <td>40270</td>
    </tr>
    <tr>
      <th>4316</th>
      <td>First Managed Care Options Inc.</td>
      <td>40270</td>
      <td>NaN</td>
      <td>40270</td>
    </tr>
  </tbody>
</table>
<p>4317 rows × 4 columns</p>
</div>




```python
# I AM NOT DONE
```


```python
def double_array(a):
    raise Exception('lol')
    return [x * 2 for x in a]
```
