# DataOrganizer
The organization works by using meta data saved in a meta data section of the measurement file. Parser "_backends_" for different types of measurement data can be implemented. Below an example backend for meta data stored in the header of a CSV file is shown.

## CSV header backend

The measurement metadata is encapsuled in a `BEGINMETA`-`ENDMETA` block. Each line depicts one parameter of the measurement.

```
# - BEGINMETA - 
# parameter1: value
# parameter2: value
...
# - ENDMETA -

# time, data
...
```
