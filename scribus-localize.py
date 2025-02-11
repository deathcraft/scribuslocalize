 #!/usr/bin/env python
import scribus
import csv
import traceback

def write_log(msg):
    with open("scribus_debug.log", "a") as f:
        f.write(msg + "\n")

def find_language_index(csvFile, langCode):
    with open(csvFile, newline='') as f:
        reader = csv.reader(f)
        header = next(reader, [])
        return header.index(langCode) if langCode in header else -1

def translateText(csvFile):
    langCode = scribus.valueDialog("Localization Language", "Enter the language code:", "Default")
    index = find_language_index(csvFile, langCode)
    translations = {}
    with open(csvFile, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            translations[row[0]] = row[index] if len(row) >= 2 else ''
    page = 1
    pagenum = scribus.pageCount()

    while (page <= pagenum):
        scribus.gotoPage(page)
        pageItems = scribus.getPageItems()

        for item in pageItems:
            # the name of the elment is the translation key
            contents = item[0]
            translation = translations[contents].strip()
            scribus.setText(translation, item[0])
        page += 1

if scribus.haveDoc():
    csvFile = scribus.fileDialog('Open a translation CSV file', filter='CSV Files (*.csv);;All Files (*)')
    try:
        if csvFile == '':
            raise Exception
        translateText(csvFile)
    except Exception:
        scribus.messageBox('Error', traceback.format_exc(), icon=0, button1=1)
else:
    scribus.messageBox('Export Error', 'You need a Document open', icon=0, button1=1)

