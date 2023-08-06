# ESPN-Statsguru-Scraper


## Introduction

This repository contains the codebase, which can be used to scrape all-time cricket statistics from ESPN Cricinfo.


## Prerequisites

### Python requirements

* You need to install Python with version 3.0 or more. You can find the latest version of Python at https://www.python.org/downloads/

* Install the library as follows.

```
pip install espncricket
```

## How to run the code

```
import espncricket.espncricket as ecs

df = ecs.get_score()
print(df.head())
 
```

* After successful execution, pandas dataframe object is returned.


## License Information

Please refer "LICENSE" file to know the license details.
Before reusing the code, please take a written permission from me.
You can contact me at sanketpatole1994@outlook.com

