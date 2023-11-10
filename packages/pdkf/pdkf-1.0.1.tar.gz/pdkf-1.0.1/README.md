# PDKF
Python package for converting PBKF file to DataFrame (pandas) list.
# Example
It is simple example for using package. This code converts data from file.pdkf to dataframe_dict.
```
import pdkf

dataframe_dict = pdkf.read_pdkf('file.pdkf')
for key, dataframe in dataframe_dict.items():
    print(key)
    print(dataframe.info())
```
# PDKF structure
The file is a ZIP archive. For each dataframe, you need to add two files to the archive: 
* META file;
* CSV or JSON file.
The META file contains the Pandas data types for the dataframe. For example:
#### Service.csv
```
name,purchase_price,description,remainder
sofa_low,10000.00,description,8
armchair_rocking,8000.00,description,14
bed_double,18000.00,description,6
chair_computer, 12000.00,description,2
bed_children,16000.00,description,5
```
#### Service.meta
```
{
    "name":"object",
    "purchase_price":"float",
    "description":"object",
    "remainder":"int64"
}
```
#### ServiceCost.json
```
[
    {
        "sofa_low":[
            {
                "price":"21000.00",
                "date":"2021.01.16"
            },
            {
                "price":"19000.00",
                "date":"2021.02.21"
            }
        ]
    },
    {
        "armchair_rocking":[
            {
                "price":"15000.00",
                "date":"2021.01.16"
            }
        ]
    }
]
```
#### ServiceCost.meta
```
{
    "price":"float",
    "date":"datetime64[ns]"
}
```
