import xml.dom.minidom

domtree = xml.dom.minidom.parse('sample_data.xml')
group = domtree.documentElement

countries = group.getElementsByTagName('country')

for country in countries:
    print('-----Country-----')
    if country.hasAttribute('name'):
        print('Country Name: {}'.format(country.getAttribute('name')))

    print('Rank: {}'.format(country.getElementsByTagName('rank')[0]
                            .childNodes[0].data))
    print('Year: {}'.format(country.getElementsByTagName('year')[0]
                            .childNodes[0].data))
    print('GDP PC: {}'.format(country.getElementsByTagName('gdppc')[0]
                              .childNodes[0].data))
    for neighbor in country.getElementsByTagName('neighbor'):
        print('Neighbor: {}'.format(neighbor.getAttribute('name')))

# Modify xml entries
countries[0].getElementsByTagName('gdppc')[0].childNodes[0].nodeValue = '77777'
countries[1].getElementsByTagName('neighbor')[0].setAttribute('name',
                                                              ('Malaysia '
                                                               'Truly Asia'))

# Add entry to xml
newCountry = domtree.createElement('country')
newCountry.setAttribute('name', 'Neitherlands')

rank = domtree.createElement('rank')
rank.appendChild(domtree.createTextNode('47'))

year = domtree.createElement('year')
year.appendChild(domtree.createTextNode('2020'))

gdppc = domtree.createElement('gdppc')
gdppc.appendChild(domtree.createTextNode('47313'))

neighbor_1 = domtree.createElement('neighbor')
neighbor_1.setAttribute('name', 'United Kingdom')
neighbor_1.setAttribute('direction', 'W')

neighbor_2 = domtree.createElement('neighbor')
neighbor_2.setAttribute('name', 'Germany')

newCountry.appendChild(rank)
newCountry.appendChild(year)
newCountry.appendChild(gdppc)
newCountry.appendChild(neighbor_1)
newCountry.appendChild(neighbor_2)

group.appendChild(newCountry)

# Write modified xml
with open('sample_data.xml', mode='w') as sXml:
    domtree.writexml(sXml)
