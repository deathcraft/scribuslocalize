#!/usr/bin/env python
import scribus
import csv
import traceback

def write_log(msg):
    with open("scribus_debug.log", "a") as f:
        f.write(msg + "\n")

def find_language_index(csv_file, lang_code):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        header = next(reader, [])
        return header.index(lang_code) if lang_code in header else -1

def translate_text(csv_file):
    lang_code = scribus.valueDialog("Localization Language", "Enter the language code:", "Default")
    index = find_language_index(csv_file, lang_code)

    if index == -1:
        scribus.messageBox('Error', f'Language code "{lang_code}" not found in CSV.', icon=0, button1=1)
        return

    translations = {}

    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if len(row) > index:
                translations[row[0]] = row[index].strip()

    for page in range(1, scribus.pageCount() + 1):
        scribus.gotoPage(page)

        for item in scribus.getPageItems():
            item_name = item[0]
            if item_name in translations:
                # now follows the hack to retain text formatting
                translated_text = translations[item_name]
                l = scribus.getTextLength(item_name)

                if lang_code == "ru": # bookvica hack
                    scribus.insertText(translated_text[0], 0, item_name)
                    scribus.selectText(1,1,item_name)
                    scribus.deleteText(item_name)
                    scribus.insertText(translated_text[1:], 2, item_name)
                    scribus.selectText(1,1,item_name)
                    scribus.deleteText(item_name)
                    scribus.selectText(len(translated_text),l-2,item_name)
                    scribus.deleteText(item_name)
                else:
                    scribus.selectText(0, l, item_name)
                    scribus.deleteText(item_name)
                    scribus.insertText(translated_text, 0, item_name)


if scribus.haveDoc():
    csv_file = scribus.fileDialog('Open a translation CSV file', filter='CSV Files (*.csv);;All Files (*)')

    try:
        if not csv_file:
            raise ValueError("No file selected.")
        translate_text(csv_file)
    except Exception as e:
        scribus.messageBox('Error', traceback.format_exc(), icon=0, button1=1)
else:
    scribus.messageBox('Export Error', 'You need a Document open', icon=0, button1=1)
