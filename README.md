# Scribus Localize

## Overview
Scribus Localize is a simple script for automating text localization in Scribus documents. It loads a CSV file containing translations, finds text elements in the Scribus document by name, and replaces them with the corresponding localized text.

## Features
- Extracts text elements from Scribus pages.
- Loads translations from a CSV file.
- Updates text elements in the document with the corresponding localized text.
- Supports multiple languages using language codes as CSV headers.

## Installation
Ensure you have **Scribus** installed. Place the script in an accessible directory and make it executable if needed:
```sh
chmod +x scribus_localize.py
```

## Usage
1. Open a Scribus document.
2. Run the script from the **Scripts** menu or execute it manually in Scribus' script console.
3. Select a CSV file containing translations.
4. Enter the desired language code when prompted.
5. The script will replace text elements in the document with the translated versions.

## CSV Format
The CSV file should follow this structure:
| Element Name | en         | ru              | zh      |
|-------------|-----------|----------------|--------|
| title       | Title     | Заголовок       | 标题    |
| subtitle    | Subtitle  | Подзаголовок    | 副标题  |
| body_text   | Sample text | Пример текста | 示例文本 |

- The **first column** contains element names from the Scribus document.
- The **first row** contains language codes (e.g., `en`, `ru`, `zh`).
- Subsequent rows contain translations for the corresponding element names.

## Error Handling
- If no document is open, the script will display an error message.
- If the selected CSV file is invalid or does not contain the requested language, an error message will appear.
- Errors are logged in `scribus_debug.log` for debugging purposes.

## Credits
Based on **Translation Helper** ([Scribus Wiki](https://wiki.scribus.net/canvas/Translation_helper)).

## License
This script is licensed under the **GPL-2.0 or later**.
