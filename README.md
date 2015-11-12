# delstat

## US Postal Service Delivery Statistics

* Delivery Statistics are available monthly, from the USPS
* Contains the number of types of deliveries for each Carrier Route in the US
* Each zip code contains several carrier routes
  * November 2015 statistics were collected for 663,532 carrier routes in 41,235 zip codes
* The output file contains summary statistics for each zip code in the input file
* Deliveries for each carrier route are totaled per zip code

### Extracting data from USPS Delivery Statistics (delstat) products

1. Download monthly data reports from the USPS Electronic Product Fulfillment Site: https://epf.usps.gov/ 
  * subscription and fee required
2. Unzip the data file (get the password from the USPS with your account info)
3. Save the unzipped text file (delstat.txt)
4. Run this script, using the path to that delstat.txt file as an argument
5. Results of this script will be a csv file saved in the same folder as the input file

### Using the extracted data

1. Join the output csv table to a Zip Codes spatial layer
2. Go to town on that
