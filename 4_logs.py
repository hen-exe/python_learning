from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Data to include
data = [
    ["No.", "Activity Type", "From Time", "Hrs", "Project"],
    ["1", "Research", "09-24-2024 08:54:32", "6", "PROJ-0062 - Internship Data and AI"],
    ["2", "Reviewing", "09-24-2024 14:08:33", "1.30", "PROJ-0062 - Internship Data and AI"],
    ["3", "Programming", "09-24-2024 15:31:58", "3", "PROJ-0062 - Internship Data and AI"],
]

# Base document
pdf = SimpleDocTemplate("logs.pdf", pageSize = A4)

# stylesheet
styles = getSampleStyleSheet()

# heading
title_style = styles['Heading1']

# 0 - left | 1 - center | 2 - right
title_style.alignment = 1

# paragraph with style
title = Paragraph("Intern 37 Activity Log", title_style)

#create a table 
table_style = TableStyle(
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 4, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] 
)

# create table object
table = Table(data, style = table_style)

# create the pdf
pdf.build([title, table])