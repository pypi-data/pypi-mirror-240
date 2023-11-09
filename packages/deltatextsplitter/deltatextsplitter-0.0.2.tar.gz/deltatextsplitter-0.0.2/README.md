# DeltaTextsplitter package

This package is meant for evaluating the text structure recognition capabilities of the package
[pdftextsplitter](https://pypi.org/project/pdftextsplitter/)
It is under development.

### Excel-parser

from deltattextsplitter import documentclass <br />
mydoc.splitter.set_documentname("mydocument") <br />
mydoc.splitter.set_documentpath("/path/to/document/") <br />
mydoc.splitter.set_outputpath("/path/for/writing/") <br />
mydoc.splitter.standard_params() <br />
mydoc.splitter.process() <br />
mydoc.outputpath = "/path/to/my/new/excel/" <br />
mydoc.export_outcomes() <br />
<br />
And then you have your output excel. You can also read an excel by:
mydoc.referencepath = "/path/to/my/new/excel/" <br />
mydoc.read_references() <br />
and then compare pandas dataframes mydoc.outcomes and mydoc.references
to calculate KPI's and other comparisons.
