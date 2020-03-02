# regpy
regpy is a python module which will help to implement complex and basic regex in a simple way.

## Features
- Grab all alphabetic data
- Grab all valid mails id's.
- Grab or extract valid postal code.

## Installation
To install regpy use this pip command :
```bash
pip install regpy
```
## Functions

### text
To grab only alphabetic data you can use text function from regpy.
```python
import regpy
regpy.text(data)
```

### emails
To grab all valid mail id use emails function from regpy.
```python
import regpy
regpy.emails(data)
```

### ip
ip function to grab all ipv4 ip's from list.
```python
import regpy
regpy.ip(data)
```

### url
You can use this url function in web scraping to extract https url from data.
```python
import regpy
regpy.url(data)
```
