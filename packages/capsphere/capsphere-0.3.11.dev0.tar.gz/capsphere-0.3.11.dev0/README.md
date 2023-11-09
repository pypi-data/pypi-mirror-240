# Capsphere

The `capsphere` package holds modules which help in the process of credit scoring for customers and institutions in Malaysia.

There are three packages in this project:

## common 

This module holds utility functions that aid the extraction of data from Malaysian bank statements, which might be in pdf or image format.

## domain

The data abstractions and classes related to a customer's transactions are contained in this module.

## recognition

For the moment, this is where all the logic for extracting pdf or image statements will be housed. We are exploring three separate methods:

### Amazon Textract

- TBC

### OCR using `pytesseract`

- TBC

### PDF libraries such as `pdfplumber`

- We have two functions in the `plumber` package which are `func_ambank` and `func_maybank`. These are both in the `converter.py` file and can be used to read AmBank and CIMB pdf bank statements.




There are some config and test files in this project as well. They  are found in the `resources` package.