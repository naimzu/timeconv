# timeconv

A simple Python package for converting between seconds, minutes, hours, and days.

## Features

This package provides the following conversions:

- seconds to minutes and seconds
- seconds to hours, minutes, and seconds
- seconds to days, hours, minutes, and seconds
- minutes to hours and minutes
- minutes to days, hours, and minutes
- minutes to seconds
- hours to minutes
- hours to seconds

## Notes

- Some functions display results in a breakdown format, such as hours, minutes, and seconds.
- Decimal values are rounded in the printed output.
- The package currently prints the conversion result directly instead of returning it.


# Installation

Clone the repository
```bash
git clone https://github.com/naimzu/timeconv.git
cd timeconv
python -m pip install -e .
```
## Example

```python
from timeconv import second_to_hour, minute_to_second

second_to_hour(3661)
# 1 hour(s) : 1 minute(s) : 1 second(s)

minute_to_second(1.5)
# 90.0 second(s).
```
