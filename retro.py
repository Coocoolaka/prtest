#Created on 2010-06-15
#@author: Kelum Peiris (kelum86@gmail.com)

from parsers.CSVParser import CSVParser
from utils.SQL import SQL

class Group(object):
    # Represent a group of data
    # Groups can be compared to eachother
    # Groups try to combine common data stores in more than 1 data file

    _headings = []
    _headingsType = []
    _currRow = 0

    def __init__(self, name, fileTypes):
        self._name = name
        self._fileTypes = fileTypes


    # @param filenameList: List of filenames that contains data.
    # @summary:
    #    Uses the file parsers to parse each data file and combine common data
    def createGroup(self, filenameList):

        # Get all the possible headers in the files
        for filename in filenameList:
            if filename.endswith('.csv'):
                self._parser = CSVParser(filename)

            self._parser.parse()
            for heading in self._parser.getHeadings():
                if self._headings.count(heading) == 0:
                    self._headings.append(heading)
                    self._headingsType.append(self._parser.getHeadingType(heading))


        db = SQL("C:\\PerGraph\\" + self._name + ".db")
        db.connect()
        db.createTable("data",self._headings, self._headingsType)
        db.commit()
    db.close()







def sort(self, heading):
    print 'BEFORE'
        for item in self._allData:
            print item

    try:
        idx = self._headings.index(heading)
            self._allData.sort(lambda x, y: cmp(x[idx], y[idx]))
        except ValueError:
            print 'Header %s does not exist' % heading

print 'AFTER'
    for item in self._allData:
        print item









#Created on 2010-06-15
#@author: Kelum Peiris (kelum86@gmail.com)

import csv, os
from stat import ST_SIZE

class CSVParser(object):
    # Parses CSV files

    # @param filename: File to be parse
    # @return: None
    def __init__(self, filename):
        self._filename = filename

    # @return: None
    # @summary:
    #     Parse and grab the headings of this CSV file
    #     Only parsing the headings because putting everything in the file into memory can be dangerous
    #     if the file is very large. Moreover, the user might not use all the data.
    #     The user can request data using the getDataByHeading function with a specific heading
    def parse(self):
        # Parse Data in the csv file
        try:
            self.csvFile = open(self._filename, "rb")
        except IOError:
            raise Exception, 'file: %s does not exist' % (self._filename)

        # Check if the file has headings
        fileSize = os.stat(self._filename)[ST_SIZE]
        header = csv.Sniffer().has_header(self.csvFile.read(fileSize))
        self.csvFile.seek(0)

        # Raise an exception if it does not have headings
        if header == False:
            print 'No Heading in the file: %s, TODO: ask the user thru gui (row 1 is the header for now)' % (self._filename)

        # Grab the headings
        reader = csv.reader(self.csvFile)
        self._headings = reader.next()

        # Remove empty strings
        while True:
            try:
                self._headings.remove('')
            except ValueError:
                break

        # Grab the first row of data to figure out if the data is alpha or numeric
        self._headingType = []
        data = reader.next()
        for item in data:
            if item.isdigit() == True:
                self._headingType.append("LONG")
            else:
                self._headingType.append("TEXT")

    self.csvFile.seek(0)

# @param heading: Used to grab the data relevant to the heading
# @return: Returns the data correspoding to the parameter 'heading'
def getDataByHeading(self, heading):
    data = []

        try:
            idx = self._headings.index(heading)
    except ValueError:
        return False;

        reader = csv.reader(self.csvFile)
        reader.next() # skip the heading

        for row in reader:
            data.append(row[idx])

        self.csvFile.seek(0) # Point to the beginning


        return data

    # @param None
    # @return: Returns the number of lines in the file
    def getNumEntries(self):

        count = 0;
        reader = csv.reader(self.csvFile)
        reader.next() # skip the heading

        for row in enumerate(reader):
            count += 1

        self.csvFile.seek(0) # Point to the beginning

        return count





