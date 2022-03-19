'''
TODO:
0. add function to create citation keys (and search if they already exist)
1. allow data grabbing from ISBN via isbnlib
2. add a function that takes database fields and treats FILE, FIELD/ALTFIELD and YEAR/DATE correctly
'''

import sys #for closing the program upon entry of KeyboardInterrupt
from datetime import datetime #for today's date

#bibliography file information

bib_folder = r"C:\localtexmf\bibtex\bib"
bib_file = r"C:\localtexmf\bibtex\bib\bibliography.bib"
#TODO add git rep and support

#list of all database fields, ordered by their appearance in the .bib file
database_fields = ["author", "bookauthor", "editor", "title", "booktitle", "maintitle", "journaltitle", "issuetitle", "publisher", "eventtitle", "eventdate", "reprinttitle", "volume", "volumes", "number", "part", "chapter", "issue", "edition", "version", "date", "year", "editora", "editorb", "editoc", "afterword", "annotator", "commentator", "forward", "introduction", "translator", "holder", "institution", "organization", "indextitle", "pubstate", "pages", "pagetotal", "(book)pagination", "urldate", "location", "venue", "url", "doi", "eid", "eprint", "eprinttype", "tyep", "entrysubtype", "addendum", "note", "howpublished", "language", "isan", "isbn", "ismn", "isrn", "issn", "iswc", "abstract", "annotation", "file", "library", "label", "shorthand", "shorthandintro", "execute", "keywords", "options", "ids", "related", "relatedtype", "relatedstring", "entryset", "crossref", "xref", "xdata", "langid", "langidopts", "gender", "presort", "sortkey", "sortname", "sortshorthand", "sorttitle", "indexsorttitle", "sortyear"]

#a dictionary of all entry types, each pointing to an array of its required fields
entry_types =  {
    "article" : ("author", "title", "journaltitle", "year/date"),
    "book" : ("author", "title", "year/date"),
    "mvbook" : ("author", "title", "year/date"),
    "inbook" : ("author", "title", "booktitle", "year/date"),
    "bookinbook" : ("author", "title", "booktitle", "year/date"),
    "suppbook" : (),
    "booklet" : ("author/editor", "title", "year/date"),
    "collection" : ("editor", "title", "year/date"),
    "mvcollection" : ("editor", "title", "year/date"),
    "incollection" : ("author", "title", "editor", "booktitle", "year/date"),
    "suppcollection" : (),
    "dataset" : ("author/editor", "title", "year/date"),
    "manual" : ("author/editor", "title", "year/date"),
    "misc" : ("author/editor", "title", "year/date"),
    "online" : ("author/editor", "title", "year/date", "doi/eprint/url"),
    "patent" : ("author", "title", "number", "year/date"),
    "periodical" : ("editor", "title", "year/date"),
    "suppperiodical" : (),
    "proceedings" : ("title", "year/date"),
    "mvproceedings" : ("title", "year/date"),
    "inproceedings" : ("author", "title", "booktitle", "year/date"),
    "reference" : ("editor", "title", "year/date"),
    "mvreference" : ("editor", "title", "year/date"),
    "inreference" : ("author", "title", "editor", "booktitle", "year/date"),
    "report" : ("author", "title", "type", "institution", "year/date"),
    "set" : (),
    "software" : (),
    "thesis" : ("author", "title", "type", "institution", "year/date"),
    "unpublished" : ("author", "title", "year/date"),
    "xdata" : ()
}

#displays help
def help(help_str):
    file = open("add_bib_help.txt", 'r')
    contents = file.read()
    print("\n" + contents + "\n")
    file.close()
        
#takes input from the user; calls help or terminates the program if necessary
def read_input(input_message):
    input_str = ""
    try:
        input_str = input(input_message)
    except KeyboardInterrupt:
        sys.exit(1)
    if(input_str.split(' ')[0] == "help"):
        help(input_str)
    else:
        return input_str

entry = {}

#taking entry type as input
while(True):
    entry["type"] = read_input("Enter entry type: ")
    
    if(entry["type"] == None):
        continue
    elif(entry["type"] not in entry_types):
        print("\n" + r"""Entry type doesn't exist. Please enter an existing entry type. For help type "help".""" + "\n")
        continue
    else:
        #type exists in the possible entry types
        break

#loop for adding required database fields
for field in entry_types[entry["type"]]:
    entry[field] = input("Enter " + field + ": ")

print("\n" + r"""Add optional fields by typing "<field name>: <value>". Type "end" to end input of optional fields.""" + "\n")

#loop for adding optional database fields
while(True):
    input_str = read_input("")
    
    if(input_str == None):
        continue
    elif(input_str == "end"):
        #end of input for optional database fields
        break;
    else:
        try:
            field_name, field_value = input_str.split(': ', 1) #splits input_str on the first instance of ": "
        except ValueError:
            print("\n" + r"""Database field should be entered as "<field name>: <value>". Type "end" to end input of optional fields.""" + "\n")
            continue
    
    #get here if input should be processed as database field
    if(field_name not in database_fields):
        print("\n" + r"""Entry type doesn't exist. Please enter an existing entry type. For help type "help".""" + "\n")
        continue
    elif(field_value == ""):
        print("\n" + "Cannot add an empty database field." + "\n")
        continue
    else:
        #input is added to the entry
        entry[field_name] = field_value

entry["dateadded"] = datetime.today().strftime('%Y-%m-%d')

#taking entry description
while(True):
    entry["description"] = read_input("Enter a short entry description: ")
    
    if(entry["description"] == None):
        continue
    else:
        #description entered
        break
    