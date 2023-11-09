import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# third-party software:
import os
import pandas

# import relevant parts from pdftextsplitter:
from pdftextsplitter import texttype
from pdftextsplitter import enum_type

# Imports from Source code:
sys.path.insert(1, '../../')
from Source.documentclass import documentclass
from Source.PandasParser import get_maintype
from Source.PandasParser import get_headlines_type
from Source.PandasParser import get_enumtype

# Definition of global variables:
Inputpath = "../Inputs/"
OutputPath = "../Calc_Outputs/"
ReferencePath = "../True_Outputs/"

# Definition of unit tests:
def pandasparsing_splitdoc() -> bool:
    """
    # Unit test for the pandasparsing-functionality of the documentclass:
    # Parameters: none; # Returns (bool): succes of the text.
    """

    # Generate the class:
    mydoc = documentclass()

    # Fill the splitter:
    mydoc.splitter.set_documentpath(Inputpath)
    mydoc.splitter.set_outputpath(OutputPath)
    mydoc.splitter.set_documentname("SplitDoc")
    mydoc.splitter.standard_params()
    mydoc.splitter.process()

    # Perform the pandas-parsing:
    mydoc.PandasParser()

    # Load the references:
    mydoc.outputpath = OutputPath
    mydoc.referencepath = ReferencePath
    mydoc.export_outcomes()
    mydoc.read_references()

    # Compare outcomes to references:
    Diff = mydoc.references.compare(mydoc.outcomes)

    # Perform the test:
    Answer = False
    if Diff.empty: Answer = True

    # print the differences if they exist:
    if not Answer:
        print(Diff.to_string())

    # Return the answer:
    return Answer

# Definition of unit tests:
def pandasparsing_opsomming() -> bool:
    """
    # Unit test for the pandasparsing-functionality of the documentclass:
    # Parameters: none; # Returns (bool): succes of the text.
    """

    # Generate the class:
    mydoc = documentclass()

    # Fill the splitter:
    mydoc.splitter.set_documentpath(Inputpath)
    mydoc.splitter.set_outputpath(OutputPath)
    mydoc.splitter.set_documentname("Opsomming")
    mydoc.splitter.standard_params()
    mydoc.splitter.process()

    # Perform the pandas-parsing:
    mydoc.PandasParser()

    # Load the references:
    mydoc.outputpath = OutputPath
    mydoc.referencepath = ReferencePath
    mydoc.export_outcomes()
    mydoc.read_references()

    # Compare outcomes to references:
    Diff = mydoc.references.compare(mydoc.outcomes)

    # Perform the test:
    Answer = False
    if Diff.empty: Answer = True

    # print the differences if they exist:
    if not Answer:
        print(Diff.to_string())

    # Return the answer:
    return Answer

# Definition of unit tests:
def pandasparsing_sixenums() -> bool:
    """
    # Unit test for the pandasparsing-functionality of the documentclass:
    # Parameters: none; # Returns (bool): succes of the text.
    """

    # Generate the class:
    mydoc = documentclass()

    # Fill the splitter:
    mydoc.splitter.set_documentpath(Inputpath)
    mydoc.splitter.set_outputpath(OutputPath)
    mydoc.splitter.set_documentname("Sixenums")
    mydoc.splitter.standard_params()
    mydoc.splitter.process()

    # Perform the pandas-parsing:
    mydoc.PandasParser()

    # Load the references:
    mydoc.outputpath = OutputPath
    mydoc.referencepath = ReferencePath
    mydoc.export_outcomes()
    mydoc.read_references()

    # Compare outcomes to references:
    Diff = mydoc.references.compare(mydoc.outcomes)

    # Perform the test:
    Answer = False
    if Diff.empty: Answer = True

    # print the differences if they exist:
    if not Answer:
        print(Diff.to_string())

    # Return the answer:
    return Answer

# Definition of unit tests:
def pandasparsing_noinput() -> bool:
    """
    # Unit test for the pandasparsing-functionality of the documentclass:
    # Parameters: none; # Returns (bool): succes of the text.
    """

    # Generate the class:
    mydoc = documentclass()

    # Do NOT Fill the splitter:

    # Perform the pandas-parsing:
    mydoc.PandasParser()

    # Verify that the outcomes are empty:
    Answer = False
    if mydoc.outcomes.empty: Answer = True

    # print the frame if its it not empty:
    if not Answer:
        print(self.outcomes.to_string())

    # Return the answer:
    return Answer

# Definition of unit tests:
def pandasparsing_humareadable() -> bool:
    """
    # Unit test for the pandasparsing-functionality of the documentclass:
    # Parameters: none; # Returns (bool): succes of the text.
    """

    # perform some tests:
    Answer = True

    # Do maintype:
    if not (get_maintype(texttype.TITLE)=="Title"): Answer = False
    if not (get_maintype(texttype.FOOTER)=="Header/Footer"): Answer = False
    if not (get_maintype(texttype.HEADLINES)=="Headline"): Answer = False
    if not (get_maintype(texttype.ENUMERATION)=="Enumeration"): Answer = False
    if not (get_maintype(texttype.BODY)=="Body"): Answer = False

    # Do chapter type:
    if not (get_headlines_type(0)=="Title"): Answer = False
    if not (get_headlines_type(1)=="Chapter"): Answer = False
    if not (get_headlines_type(2)=="Section"): Answer = False
    if not (get_headlines_type(3)=="Subsection"): Answer = False
    if not (get_headlines_type(4)=="Subsubsection"): Answer = False
    if not (get_headlines_type(5)=="Higher_Order"): Answer = False

    # Do enumeration type:
    if not (get_enumtype(enum_type.BIGROMAN)=="Bigroman"): Answer = False
    if not (get_enumtype(enum_type.SMALLROMAN)=="Smallroman"): Answer = False
    if not (get_enumtype(enum_type.BIGLETTER)=="Bigletter"): Answer = False
    if not (get_enumtype(enum_type.SMALLLETTER)=="Smallletter"): Answer = False
    if not (get_enumtype(enum_type.DIGIT)=="Digit"): Answer = False
    if not (get_enumtype(enum_type.SIGNMARK)=="Signmark"): Answer = False
    # Return the answer:
    return Answer
    
# Definition of collection:    
def pandasparsing_tests() -> bool:
    """
    # Collection-function of unit-tests.
    # Parameters: none; # Returns (bool): succes of the text.
    """
    
    # Define answer:
    Answer = True
    
    # Call the tests:

    if (pandasparsing_splitdoc()==False):
        Answer=False
        print('\n==> pandasparsing_splitdoc() failed!\n')

    if (pandasparsing_opsomming()==False):
        Answer=False
        print('\n==> pandasparsing_opsomming() failed!\n')

    if (pandasparsing_noinput()==False):
        Answer=False
        print('\n==> pandasparsing_noinput() failed!\n')

    if (pandasparsing_sixenums()==False):
        Answer=False
        print('\n==> pandasparsing_sixenums() failed!\n')

    if (pandasparsing_humareadable()==False):
        Answer=False
        print('\n==> pandasparsing_humareadable() failed!\n')

    # Return answer:
    return Answer

if __name__ == '__main__':
    if pandasparsing_tests():
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
