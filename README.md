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

# Installation

Clone the repository
```bash
git clone https://github.com/naimzu/timeconv.git
cd timeconv
python -m pip install -e .
```
# Usage

```python
from timeconv import second_to_minute, hour_to_second, minute_to_hour

second_to_minute(90)   # 1.5
hour_to_second(2)      # 7200
minute_to_hour(1)      # 0.01667
```
