# Ready Data Task

## Sources

Source 1 was located in Office of National Statistics (ONS).
<img width="1043" height="557" alt="image" src="https://github.com/user-attachments/assets/c4fcdce5-e638-4b89-bb83-57816493a314" />
See the properties of the dataset:
<br>
<img width="346" height="153" alt="image" src="https://github.com/user-attachments/assets/51485495-a541-4e93-8191-adafbbc513e1" />

<br>
Source 2 was located on Kaggle by the author "Utkarsh Singh".
<img width="712" height="427" alt="image" src="https://github.com/user-attachments/assets/65550409-ae61-4269-9adc-b0f642e43b49" />

See the properties of the dataset:
<br>
<img width="343" height="150" alt="image" src="https://github.com/user-attachments/assets/0d04b7ca-6911-45b0-aed8-c6e3a2291bfe" />

## Reliability

Source 1 was found on ONS which is a government funded resource for public statistics. The datasets in this website come under the OGL v3.0 which is a licence that is used for government information and verifies it as good source of data. This dataset uses a variety of headers to explain its use which includes age range and years. The only issues I found with this dataset is that it uses less fields but is quite big due to the extra analysis found in it. It is quite a detailed dataset that does not need any cleaning due to it being a government distributed dataset.

Source 2 was found on Kaggle under the author Utkarsh Singh who is a verified dataset author.

## Further Preparations

Source 2:
* Change the CSV format to Excel for more tools, easier editing and visualisations.
* Put the CSV file into power query as an alternative to get it ready for cleaning as it automatically assigns data types, highlights errors and allows automated methods of cleaning.
* Change the headers to be capitalised and easier to read. This also includes removing unnecessary columns to make the dataset simpler to read and analyse. One example of this would be removing the ID column as it is not necessary for numerical analysis.
* Cleaning the "gross_income" column would be helpful for numerical analysis as the current data includes text and numbers. For this we need to make bands that will act as an ID for each range. Either it can be changed from 0-7 or can be changed by finding the midpoint between all the ranges and leaving the above and under values as they are but just removing the text. The anomalies need to be switched to an outlier number so they can be easily noticed. 
* All the N/As in the number columns need to be changed to 0 for calculation to be done on them.
* The null values in the "type" column needs to be changed to "n/a" also for correct analysis.
* Any other column that does not comply with the analysis requirements should also be removed.
* Calculated KPI columns can also be added if they meet the requirements of analysis.
