# Location-Data-Extraction-using-GoogleMaps-API

Interested in Finding the location coordinates of anything you wish for? Let us use the GoogleMaps API here. 

## Installation and Usage:
i.Dependencies needed to execute the script:
1. xlsxwriter
2. pandas
3. beautifulsoup4
4. requests

Simply install the dependencies using : ***pip install package_name***

ii. Navigate to your [Google cloud Platform Console](https://console.cloud.google.com/home/dashboard?project=vqamajorproj&pli=1). 
Under **the APIs and Services**, select **Dashboard**.


iii. Select the **Enable APIs and Services** Tab as shown here:

iv. It will take you to the Google APIs Library. Simply search for the API by typing ***Google Places API*** and click on it. 

v. Click **Enable** to enable the API. After enabling it, you should a similar case for the same as mine shown below:

vi. Now your API is enabled. Let us setup the credentials for you to access this API. Navigate to **Enable APIs and Services** Tab and select **Credentials**

vii. Select **Create Credentials** and select **API Key** from the dropdown list.

viii. Your API Key is now created under the section called ***API Keys***. You need to copy this Key from here and paste it in the python script provided in the repo.

ix. You can also put restrictions on your API Key to be used ONLY by this API to provide any additional costs.

### NOTE: 
***NEVER SHARE YOUR API KEY WITH ANYONE!!*** :anger:

## Usage:
Simply execute the script using the command: ***python google_maps_search_query.py***. 
It will ask you to enter the name of the place which you want to search. Simply enter the name and press enter. An Excel spreadsheet will be generated with the Longitude-
Latitude and the details of the places associated with your searched keyword.
