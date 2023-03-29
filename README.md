# WebRL
WebRL is a tool for repairing broken UI test scripts automatically.
## Getting Started with WebRL
### Prerequisites
python3, Selenium, torch, Levenshtein, BeautifulSoup, torchvision, PIL

### Running WebRL
```
usage: python main.py [-t test_case] [-o old_url] [-n new_url] [-m strategy] [-c chromedriver_path]
- optional arguments:
  -t test_case          the name of a test script that needed in the directory webTestScript/
  -m strategy           the repair strategy to apply (Hyb, COLOR and CNN)
  -o old_url            
  -n new_url         
  -c chromedriver_path   
```
### Example
```
python main.py -t yahoo_search -o http://web.archive.org/web/20200107001908/https://www.yahoo.com/  -n http://web.archive.org/web/20220221000940/https://www.yahoo.com/ -m Hyb -c /Users/Desktop/chromedriver
```
The original yahoo_search.py can be found in webTestScript/, the repaired script can be found in WebRL_output/yahoo_search.
## Test scripts used in paper
In the webTestScript/ directory, you can find the test scripts used in the experiments, with the old_url and new_url included at the beginning of comment lines in each script.



