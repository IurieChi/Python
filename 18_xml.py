#The xml.etree.ElementTree module implements a simple and efficient
#API for parsing and creating XML data.

import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate, ExpatError, errors
import xml.dom.minidom


tree = ET.parse('files/country_data.xml')
root = tree.getroot()
# As an Element, root has a tag and a dictionary of attributes:
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag, child.attrib)
    
# Element has some useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on). For example, Element.iter():
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
    
# Element.findall() finds only elements with a tag which are direct children of the current element. Element.find() finds the first child with a particular tag,
# and Element.text accesses the element’s text content. Element.get() accesses the element’s attributes:

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
    
# Modifying an XML File
# ElementTree provides a simple way to build XML documents and write them to files. The ElementTree.write() method serves this purpose.

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('files/output.xml')

# We can remove elements using Element.remove(). Let’s say we want to remove all countries with a rank higher than 50:
for country in root.findall('country'):
  
    # using root.findall() to avoid removal during traversal
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('files/output.xml')

xml_data = "<root>...</root>"
print(ET.canonicalize(xml_data))

with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
    ET.canonicalize(xml_data, out=out_file)
# root = ET.fromstring(country_data)

# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")


# ExpatError exceptions have a number of interesting attributes:
p = ParserCreate()
try:
    p.Parse('files/output.xml')
except ExpatError as err:
    print("Error:", [err.code])



# DOM Example
# This example program is a fairly realistic example of a simple program.
# In this particular case, we do not take much advantage of the flexibility of the DOM.


document = """
    <slideshow>
    <title>Demo slideshow</title>
    <slide><title>Slide title</title>
    <point>This is a demo</point>
    <point>Of a program for processing slides</point>
    </slide>

    <slide><title>Another demo slide</title>
    <point>It is important</point>
    <point>To have more than</point>
    <point>one slide</point>
    </slide>
    </slideshow>
"""

dom = xml.dom.minidom.parseString(document)

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print(f"<title>{getText(title.childNodes)}</title>")

def handleSlideTitle(title):
    print(f"<h2>{getText(title.childNodes)}</h2>")

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print(f"<li>{getText(point.childNodes)}</li>")

def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print(f"<p>{getText(title.childNodes)}</p>")

handleSlideshow(dom)
