# Canadian Geopoli Data

This political science project automates gathering geographical data for federal and provincial electoral districts. The output is saved in .csv format and utilizes the Google Maps API & Google Distance Matrix API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this projects requirements.txt.

```bash
pip install requirements.txt
```

## Using the Data Project

```python
There are multiple steps to get this project up and running 

Create a Google Cloud Platform account, enable the needed APIs, and enable billing (note the distinctions between free and paid use)
Clean your .csv data sets before running through the APIs
To get your destination geocodes, use "batchcode.py".
For non-batch geocoding and distance coding use the "geocode.py" or "matrix.py".
Use the saved output .csv file to use with "distance_matrix.py" 
For directions use "directions.py"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)