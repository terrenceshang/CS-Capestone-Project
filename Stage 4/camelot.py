import camelot
tables = camelot.read_pdf("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Area South.pdf")
tables

tables.export('C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
tables[0]

tables[0].parsing_report

tables[0].to_csv('C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
tables[0].df