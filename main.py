from data_from_api import *
from functions import *
from constants import *

# Create a new Document
doc = Document()

# Add footer image
add_image_to_footer(doc,footer_img_path)
doc.add_picture(heading_img_path,width=Cm(4.63),height = Cm(1.05))  # Add heading image
profile_text_paragraph = doc.add_paragraph()
run = profile_text_paragraph.add_run()
inline_shape = run.add_picture(profile_img_path,width=Cm(4.61),height = Cm(4.61)) # Add profile photo
new_paragraph(obj=doc,text=f"{person_name}\n",boolean_bold=True,r=128,g=0,b=128)
new_paragraph(obj=doc,text=f"{designation},\n{company}\n\n{summary}")

# Add a new page
doc.add_page_break()

for table in doc.tables:
    format_table(table)

# Add profile photo for the second page

profile_picture = doc.add_picture(candidate_profile_img_path, width=Inches(2))

# Add the "Personal Data" header as a paragraph
new_paragraph(obj=doc,text="Personal Data:",boolean_bold=True,r=128,g=0,b=128)

# Add a table with three columns
table = doc.add_table(rows=0, cols=3)

# Add rows for personal data
personal_data = ["Date Of Birth","Nationality","Location","Languages"]
personal_data_api = [dob,nationality,location,language]
for i in range(len(personal_data)):
    add_row(table,personal_data[i],":",personal_data_api[i])

for cell in table.columns[2].cells:
    cell.width = Cm(11.0)

# Add Educational Data
new_paragraph(obj=doc,text="Educational Data:",text_size=12,boolean_bold=True,r=128,g=0,b=128)

# Add a table with three columns
table = doc.add_table(rows=0, cols=3)

# Add rows for educational data
add_educational_row(table, "1997", "Jamnalal Bajaj Institute of Management Studies, Mumbai", "Masters in Management Studies (Marketing)")
add_educational_row(table, "1992", "Narsee Monjee College of Commerce, Mumbai", "Bachelor of Commerce (Financial Accounting)")
for cell in table.columns[2].cells:
    cell.width = Cm(11.0)

# Add image
doc.add_picture(employee_data_img_path, width=Inches(7))

# Add "Company Profile:" text
company_profile_paragraph = new_paragraph(obj=doc,text="Company Profile:",text_size=11,boolean_bold=True,boolean_italic=True,r=128,g=0,b=128)
add_text_to_para(obj=company_profile_paragraph,text=f" {designation},{company}",text_size=10,boolean_italic=True)

new_paragraph(obj=doc,text="Key Responsibilities:",text_size=12,boolean_bold=True,boolean_italic=True,r=128,g=0,b=128)
add_bullet_points(key_responsibilities,doc)

new_paragraph(obj=doc,text="Key Achievements:",text_size=12,boolean_bold=True,boolean_italic=True,r=128,g=0,b=128)
add_bullet_points(key_achievements,doc)
# Add image
doc.add_picture(company_location_img_path, width=Inches(7))
# Add image
profile_picture = doc.add_picture(additional_data_img_path, width=Inches(2))

# Add a table with three columns
table = doc.add_table(rows=0, cols=3)

# Add rows for additional data with bullet points
add_row(table, "Location Preference", ":", pref_loc)
add_row(table, "CTC*", ":", ctc)
add_row(table, "Contact Details", ":", f"{email}, {phone_number}")
add_additional_row(table, "2019", ":","London Business School", "Leading for Results Program\nA Leadership Development Program focused on\n •  Strengthening market positions & accelerating growths\n •  Excelling in execution and creating a winning culture")
add_additional_row(table, "1992-1994", ":", "Indo-German Training Centre, Mumbai", "Diploma in Business Administration\n •  Sponsored by Bayer (India) Ltd, with 2/3rds of training being on the job.\n •  Course under the aegis of Indo-German Chamber of Commerce.\n•  Training content developed by Deutscher Industrie – und Handelsta (Association of German Chambers of Industry & Commerce).")
for cell in table.columns[2].cells:
    cell.width = Cm(11.0)

# Add a new page
doc.add_page_break()
doc.add_picture(background_image_path, width=Cm(20),height = Cm(23.14))
# Save the document
doc.save("main.docx")