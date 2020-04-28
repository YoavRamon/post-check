## Prerequisites
- Python 3.6 and above
- install requirements (use: `pip install -r requirements.txt`)
## Usage
For Basic usage just enter your package number:
```bash
python ./post-check.py -pn RH080789165GB
```
Should output:
```text
      Date                                                             Description    Postal Unit            City
23/04/2020                            Unclaimed and will be returned to the sender      Zemenhoff  Tel Aviv Yaffo
29/03/2020                              A second notice was left for the addressee      Zemenhoff  Tel Aviv Yaffo
23/03/2020                                     A notice was left for the addressee      Zemenhoff  Tel Aviv Yaffo
19/03/2020  Arrived at the postal unit for delivery to addressee (shelf no ג-3170)      Zemenhoff  Tel Aviv Yaffo
```
For extended usage see:
```text
usage: post-check.py [-h] -pn PACKAGE_NUMBER [-ih] [-pj] [-cf COOKIE_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -pn PACKAGE_NUMBER, --package-number PACKAGE_NUMBER
                        Package number
  -ih, --is-heb         Print in hebrew
  -pj, --print-json     Print json instead of table
  -cf COOKIE_FILE, --cookie-file COOKIE_FILE
                        Cookie file
```
This code can be automated with cron if you want to check your package status each day.

**Don't spam the post-il site!**

## TODO list
 * Check multiple packages in one command
 * Save cache of previous status of package and update only if that status changed
