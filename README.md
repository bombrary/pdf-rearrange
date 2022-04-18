# pdf-rearrange

Rearrange the pages of your PDF file. This is used for imposition e.g. glue bind and flat bind.

## Install 

```
pip install git+https://github.com/bombrary/pdf-rearrange
```

If you clone this repositry, you can install by

```
pip install -e .
```

## How to use

```
pdf_rearrange src.pdf dst.pdf 4 1 2 3
```

Then the page 1, 2, 3, 4, 5, 6, 7, 8, ... is rearranged to 4, 1, 2, 3, 8, 5, 6, 7, ...
