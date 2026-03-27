# timeconv

A simple Python package to convert between hours, minutes, and seconds.

## Features

This package provides the following conversions:

- seconds to minutes
- seconds to hours
- minutes to hours
- minutes to seconds
- hours to minutes
- hours to seconds

All results are rounded to 5 decimal places.

#Installation

Clone the repository
```bash
git clone https://github.com/naimzu/timeconv.git
cd timeconv
```
#Usage

```python
from timeconv import second_to_minute, hour_to_second

print(second_to_minute(90))   # 1.5
print(hour_to_second(2))      # 7200
print(minute_to_hour(1))       # 0.01667
```