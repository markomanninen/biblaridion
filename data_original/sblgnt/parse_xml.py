#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: parse_xml.py

# use file to convert .xml file to uniform .csv file with other greek bible manuscripts

import xml.etree.ElementTree as etree

booknames = {
	"40N": "ΚΑΤΑ ΜΑΘΘΑΙΟΝ",
	"41N": "ΚΑΤΑ ΜΑΡΚΟΝ",
	"42N": "ΚΑΤΑ ΛΟΥΚΑΝ",
	"43N": "ΚΑΤΑ ΙΩΑΝΝΗΝ",
	"44N": "ΠΡΑΞΕΙΣ ΑΠΟΣΤΟΛΩΝ",
	"45N": "ΠΡΟΣ ΡΩΜΑΙΟΥΣ",
	"46N": "ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Α",
	"47N": "ΠΡΟΣ ΚΟΡΙΝΘΙΟΥΣ Β",
	"48N": "ΠΡΟΣ ΓΑΛΑΤΑΣ",
	"49N": "ΠΡΟΣ ΕΦΕΣΙΟΥΣ",
	"50N": "ΠΡΟΣ ΦΙΛΙΠΠΗΣΙΟΥΣ",
	"51N": "ΠΡΟΣ ΚΟΛΟΣΣΑΕΙΣ",
	"52N": "ΠΡΟΣ ΘΕΣΣΑΛΟΝΙΚΕΙΣ Α",
	"53N": "ΠΡΟΣ ΘΕΣΣΑΛΟΝΙΚΕΙΣ Β",
	"54N": "ΠΡΟΣ ΤΙΜΟΘΕΟΝ Α",
	"55N": "ΠΡΟΣ ΤΙΜΟΘΕΟΝ Β",
	"56N": "ΠΡΟΣ ΤΙΤΟΝ",
	"57N": "ΠΡΟΣ ΦΙΛΗΜΟΝΑ",
	"58N": "ΠΡΟΣ ΕΒΡΑΙΟΥΣ",
	"59N": "ΙΑΚΩΒΟΥ",
	"60N": "ΠΕΤΡΟΥ Α",
	"61N": "ΠΕΤΡΟΥ Β",
	"62N": "ΙΩΑΝΝΟΥ Α",
	"63N": "ΙΩΑΝΝΟΥ Β",
	"64N": "ΙΩΑΝΝΟΥ Γ",
	"65N": "ΙΟΥΔΑ",
	"66N": "ΑΠΟΚΑΛΥΨΙΣ ΙΩΑΝΝΟΥ"
}

order_by = 10

content = ""

root = etree.parse('sblgnt.xml').getroot()

for book in root.findall('book'):
    title = book.find('title').text
    orig_book_index = [k for k, v in booknames.items() if title == v][0]
    for verse in book.findall('p'):
        for e in verse:
            first = e.tag == 'verse-number'
            break
        for e in verse:
            if e.tag == 'verse-number':
                content = content.strip()+"\r\n"
                numbering = e.text.split(':')
                if len(numbering) == 2:
                    orig_chapter, orig_verse = int(numbering[0]), int(numbering[1])
                else:
                    orig_verse = int(numbering[0])
                content += "%s\t%s\t%s\t%s\t%s\t" % (orig_book_index, orig_chapter, orig_verse, "", order_by)
                order_by += 10
            if e.tag == 'w':
                content += e.text + " "
    if first:
        content = content.strip()+"\r\n"

content = "orig_book_index\torig_chapter\torig_verse\torig_subverse\torder_by\ttext\r\n" + content.strip()

with open('sblgnt.csv', 'w') as f:
    f.write(content)
