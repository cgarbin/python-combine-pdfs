# python-combine-pdfs

Combine PDF files using  [PyPDF2](https://pythonhosted.org/PyPDF2/).

Usage:

    python-combinepdfs file1.pdf file2.pdf fileN.pdf -o output.pdf

Files are combined in the order they are given. Output is optional (defaults to combined.pdf).

### Note

This code is using the a [workaround for PyPDF2](https://stackoverflow.com/a/49927541/336802) for the "empty output file wiht Python 3" issue documented [here](https://github.com/mstamy2/PyPDF2/issues/293).

PyPDF2 is [looking for new maintainers](https://github.com/mstamy2/PyPDF2/issues/385). Once that issue is resolved and a new version is released, the code can be cleaned by removng the explicit context creation.
