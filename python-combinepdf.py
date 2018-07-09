"""
Combines PDF files into one PDF file.

Sources for this code:

* https://automatetheboringstuff.com/chapter13/
* https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
* https://pythonhosted.org/PyPDF2/
* https://stackoverflow.com/a/49927541/336802

This program combines all specified PDF files into one PDF file. The
files are combined in the order they are given. Use '-o output.pdf' to
specify the output file name (defaults to combined.pdf if not specified).
"""

from argparse import ArgumentParser
import contextlib
import PyPDF2


def main():
    ap = ArgumentParser(
        description='Combines several PDF files into one file.')

    # The files to combine
    ap.add_argument('files', metavar='file1 file2 ...',
                    help='Files to combine', nargs='+')

    # The output file (defaults to combined.pdf if not specified)
    ap.add_argument('-o', '--output', nargs='?',
                    const='combined.pdf', default='combined.pdf',
                    help='Output file name (combined.pfd, if not specified)')

    args = ap.parse_args()

    # Workaround for PyPDF2 empty output file: keep input files open
    # See https://stackoverflow.com/a/49927541/336802
    with contextlib.ExitStack() as stack:
        pdfMerger = PyPDF2.PdfFileMerger()
        files = [stack.enter_context(open(pdf, 'rb')) for pdf in args.files]
        for f in files:
            pdfMerger.append(f)
        with open(args.output, 'wb') as f:
            pdfMerger.write(f)

if __name__ == '__main__':
    main()
