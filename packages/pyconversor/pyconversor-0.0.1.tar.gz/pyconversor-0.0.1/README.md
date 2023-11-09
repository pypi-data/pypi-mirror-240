# pyconversor

Pypi link.

## Motivation

pyconversor is a lib developed with the aim of unifying all the conversion tools a dev might need during development in one place.

## Instructions

1. Install:

    ``` shell
        pip install pyconversor
    ```

2. Convert:

    **Example:**

    ``` python
    from pycorvert import pyconversor

    test = {
    
        "People":{
            "Name":"Alan",
            "Address":{
                "Street": "Of dumbs",
                "Number":0
            }
        }
    }
    string = pyconversor.convert_dict_to_xml(dictionary=test, raw_string=False)

    print(string)

    ```

## features and plans

- [x] Convert a dictionary to a XML (on a raw string or not)
- [ ] Convert a xml to a dictionary/.

## To upload your own project to pypi

Follow [this site](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-your-project-to-pypi)
