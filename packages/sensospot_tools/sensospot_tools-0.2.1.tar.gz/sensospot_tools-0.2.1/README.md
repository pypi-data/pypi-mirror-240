Sensospot Tools
===============

Some small tools for working with parsed Sensospot data.

## Selecting and spliting a pandas data frame

### select(data: DataFrame, column: str, value: Any) -> DataFrame

Selects rows of a dataframe based on a value in a column

Example:
```python

    from sensospot_tools import select

    print(data)
        category  value
    0      dog      1
    1      cat      2
    2    horse      3
    3      cat      4

    print(select(data, "category", "cat"))
          category  value
        1      cat      2
        3      cat      4
```


### split(data: DataFrame, *on: Any) -> Iterator[tuple[Any, ..., DataFrame]]

Splits a data frame on unique values in multiple columns

Returns a generator of tuples with at least two elements.
The _last_ element is the resulting partial data frame,
the element(s) before are the values used to split up the original data.

Example:
```python

    from sensospot_tools import split

    print(data)
        category  value
    0      dog      1
    1      cat      2
    2    horse      3
    3      cat      4

    result = dict( split(data, column="category") )

    print(result["dog"])
        category  value
    0      dog      1

    print(result["cat"])
        category  value
    1      cat      2
    3      cat      4

    print(result["horse"])
        category  value
    2    horse      3
```

## Working with data with multiple exposure times

### select_hdr_data(data: DataFrame, spot_id_columns: list[str], time_column: str, overflow_column: str) -> DataFrame:

Selects the data for increased dynamic measurement range.

To increase the dynamic range of a measurement, multiple exposures of one
microarray might be taken.

This function selects the data of only one exposure time per spot, based
on the information if the spot is in overflow. It starts with the weakest
signals (longest exposure time) first and chooses the next lower exposure
time, if the result in the `overflow_column` is `True`.

This is done for each spot, and therfore a spot needs a way to be
identified across multiple exposure times. Examples for this are:
    - for a single array:
    the spot id (e.g. "Pos.Id")
    - for multiple arrays:
    the array position and the spot id (e.g. "Well.Name" and "Pos.Id")
    - for multiple runs:
    the name of the run, array position and the spot id
    (e.g. "File.Name", "Well.Name" and "Pos.Id")

The function will raise a KeyError if any of the provided column names
is not present in the data frame

### normalize(data: DataFrame, normalized_time: Union[int, float], time_column: str, value_columns: list[str], template: str) -> DataFrame:

normalizes values to a normalized exposure time

Will raise a KeyError, if any column is not in the data frame;
raises ValueError if no template string was provided.


## Development

To install the development version of Sensospot Tools:

    git clone https://git.cpi.imtek.uni-freiburg.de/holgi/sensospot_tools.git

    # create a virtual environment and install all required dev dependencies
    cd sensospot_tools
    make devenv

To run the tests, use `make tests` or `make coverage` for a complete report.

To generate the documentation pages use `make docs` or `make serve-docs` for
starting a webserver with the generated documentation
