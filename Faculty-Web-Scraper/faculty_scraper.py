import os.path
import re
from config import *


for page in faculty_html_pages:
    info_file = os.path.basename(page)
    info_file = str(os.path.splitext(info_file)[0]) + ".txt"
    info_file_path = os.path.join(save_path, info_file)

    faculty_page = open(page, "r")
    page_contents = faculty_page.read()

    name = re.search(name_pattern, page_contents)
    education = re.search(education_pattern, page_contents)
    research = re.search(research_interest_pattern, page_contents)
    email = re.search(email_pattern, page_contents)
    webpage = re.search(webpage_pattern, page_contents)

    with open(info_file_path, "w+") as file:
        if name:
            file.write(name_prefix + name.group(1) + "\n")
        else:
            file.write(name_prefix + "None\n")

        if education:
            file.write(education_prefix + education.group(1) + "\n")
        else:
            file.write(education_prefix + "None\n")

        if research:
            file.write(research_prefix + research.group(1) + "\n")
        else:
            file.write(research_prefix + "None\n")

        if email:
            file.write(email_prefix + email.group(1) + "\n")
        else:
            file.write(email_prefix + "None\n")

        if webpage:
            file.write(webpage_prefix + webpage.group(1) + "\n")
        else:
            file.write(webpage_prefix + "None\n")
