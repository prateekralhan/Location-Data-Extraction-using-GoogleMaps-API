# Location-Data-Extraction-using-GoogleMaps-API

Interested in Finding the location coordinates of anything you wish for? Let us use the GoogleMaps API here. 

## Installation and Usage:
i.Dependencies needed to execute the script:
1. xlsxwriter
2. pandas
3. beautifulsoup4
4. requests

Simply install the dependencies using : ***pip install package_name***

ii. Navigate to your [Google cloud Platform Console](https://console.cloud.google.com/home/dashboard?project=vqamajorproj&pli=1) [You must have a valid GCP account]. 
Under **the APIs and Services**, select **Dashboard**.

![image](https://user-images.githubusercontent.com/29462447/79219184-6a69a700-7e6f-11ea-885b-8892b60a4546.png)

iii. Select the **Enable APIs and Services** Tab as shown here:

![image](https://user-images.githubusercontent.com/29462447/79219195-735a7880-7e6f-11ea-800a-fd43d7b3720d.png)

iv. It will take you to the Google APIs Library. Simply search for the API by typing ***Google Places API*** and click on it. 

![image](https://user-images.githubusercontent.com/29462447/79219222-7d7c7700-7e6f-11ea-95ea-92e8a89f4df5.png)

v. Click **Enable** to enable the API. After enabling it, you should a similar case for the same as mine shown below:

![image](https://user-images.githubusercontent.com/29462447/79219244-866d4880-7e6f-11ea-8b25-889e98f2c74a.png)

vi. Now your API is enabled. Let us setup the credentials for you to access this API. Navigate to **Enable APIs and Services** Tab and select **Credentials**.

![image](https://user-images.githubusercontent.com/29462447/79219274-94bb6480-7e6f-11ea-946a-60d9be400b66.png)

vii. Select **Create Credentials** and select **API Key** from the dropdown list.

![image](https://user-images.githubusercontent.com/29462447/79219300-a00e9000-7e6f-11ea-8604-b5397d2ac3ff.png)

viii. Your API Key is now created under the section called ***API Keys***. You need to copy this Key from here and paste it in the python script provided in the repo.

ix. You can also put restrictions on your API Key so that it can be accessed only by this API to prevent any additional costs.

### NOTE: 
***NEVER SHARE YOUR API KEY WITH ANYONE!!*** :anger:

## Usage:
Simply execute the script using the command: ***python google_maps_search_query.py***. 
It will ask you to enter the name of the place which you want to search. Simply enter the name and press enter. An Excel spreadsheet will be generated with the Longitude-
Latitude and the details of the places associated with your searched keyword.
