# Anomalies Scraper

This Python script was intended to scrape anomaly from Statistics Indonesia SQL lab from a list in an Excel file. 

## Features

- Download all the anomalies listed in the excel
- Merge it all into a single file
- Create a directory containing anomalies for each Supervisor

## Prerequisites

- Python 3.6 or higher
- pandas
- openpyxl
- selenium

## Installation

1. Clone this repository.
2. Install the required packages:

```bash
pip install pandas openpyxl selenium
```

3. Download chromedriver from:

```
https://storage.googleapis.com/chrome-for-testing-public/VERSION/win64/chromedriver-win64.zip
```

change the VERSION with your chrome version. Exctract into the same directory as the repository.

## Usage

1. Open anomali_bps.ipynb in your favorite notebook environment

2. Change the INPUT into the path of your excel file containing list of anomalies and SPV into the path of supervisor data:

   ```
   LIST = 'sqllab_untitled_query_1_20240821T043054.csv'
   SPV = 'wilayah_tugas_sak_82024.xlsx'
   ```

3. Make sure every tab in SQL lab was closed 

4. Run the script.

5. Please do a manual login on the instructed part

6. Run the rest of the code

7. The script will create a directory containing all the downloaded anomalies, a directory containing anomalies for each Supervisor, and an excel file which contains all the anomalies combined into one.

8. (Optional) RUn the script to add status and last modified using input from STS path structure on [Data Structure](#status-data).

## Input Data Structure

### List of anomalies

| kode | keterangan | link |
| --- | --- | --- |
| ... | ... | ... |


### Supervisor data

For Supervisor data it should have the following columns.

| idbs | pcl | pml |
| --- | --- | --- |
| ... | ... | ... |

### Status data

The data containing status and last modified should have the following columns.

| idbs | DSRT | status | last_modified |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Directory Structure

```ascii
/anomali_petugas
/chromedriver-win64
/download
anomali_bps.ipynb
```

## Notes

- This script was designed to help collect data from Statistic Indonesia's SQL lab.
- The script assumes certain column names and structures. Modify as needed for different data formats.
- This script relies on chromedriver which differ for every chrome version, please [download](https://googlechromelabs.github.io/chrome-for-testing/) the one which match with your chrome version.
- Since the Author is a lazy bum, please login manually on the specified part.

## Contributing

Feel free to fork this repository and submit pull requests with any improvements or bug fixes.

## Author

- **Terry Devara Tri Saadi**
- Email: <devatrisa@gmail.com>

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
