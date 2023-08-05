# kdp-python-connector

## Prequisites
* Python version 3.8.5
* Install dependencies from main directory with:
```
pip3 install -r requirements.txt
```

## Examples

### Example 1: Ingest CSV File


See [./examples/ingest_csv.py](./examples/ingest_csv.py) for an example of how to ingest data from a csv file into KDP.


**Step 0**

Set System Variables to provide the values for the variables listed below:

Required
* EMAIL - KDP user's email address
* PASSWORD - KDP user's password 
* WORKSPACE_ID - KDP user's workspace id
* DATASET_ID - KDP user's dataset id

Optional
* KDP_URL - KDP url to connect to, default is https://api.app.koverse.com
* PATH_TO_CSV_FILE - location to the csv file to be ingested, default=['https://kdp4.s3-us-east-2.amazonaws.com/test-data/cars.csv']
* STARTING_RECORD_ID - Record to start reading, default=''
* PATH_TO_CA_FILE - When not provided will not verify ssl of request, default=''
* INPUT_FILE - File with data to ingest, default='../datafiles/actorfilms.csv'
* BATCH_SIZE - number of records in a batch, default=100000

**Step 1**

Install dependency

```
cd examples
pip3 install -r requirements.txt
```

**Step 2**

Execute the script

```
python3 ingest_csv.py
```

## Release

### Versioning

Before a better solution is implemented, `setup.py` file needs to be updated to increment the version number each time a new version is needed. Next version number can be determined from the current latest git tag and increment the minor version by one.
