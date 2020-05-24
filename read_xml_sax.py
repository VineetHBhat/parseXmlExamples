import xml.sax
'''
XML.SAX provides methods to read xml data from a file. This can't be used to
modify the xml file.
'''


class SampleData(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        '''
        This method over-rides the startElement method of the
        xml.sax.ContentHandler class.
        '''
        self.current = name
        if self.current == 'country':
            print('-----Country-----')
            print('Country Name: {}'.format(attrs['name']))
        if self.current == 'neighbor':
            self.neighbor = attrs['name']

    def characters(self, content):
        '''
        This method over-rides the characters method of the
        xml.sax.ContentHandler class.
        '''
        if self.current == 'rank':
            self.rank = content
        elif self.current == 'year':
            self.year = content
        elif self.current == 'gdppc':
            self.gdppc = content

    def endElement(self, name):
        '''
        This method over-rides the endElement method of the
        xml.sax.ContentHandler class.
        '''
        if self.current == 'rank':
            print('Rank: {}'.format(self.rank))
        elif self.current == 'year':
            print('Year: {}'.format(self.year))
        elif self.current == 'gdppc':
            print('GDP PC: {}'.format(self.gdppc))
        elif self.current == 'neighbor':
            print('Neighbor: {}'.format(self.neighbor))

        self.current = ''


handler = SampleData()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('sample_data.xml')
