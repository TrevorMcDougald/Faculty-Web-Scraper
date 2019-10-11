from os import listdir
from os.path import isfile, join
from os import walk

path_to_pages = r'C:\Users\Trevor\Python\Faculty-Web-Scraper\Faculty-Web-Scraper\Faculty-Pages'

# faculty_html_pages = [file for files in listdir(path_to_pages)if isfile(join(path_to_pages, file))]
faculty_html_pages = []

for (file_names) in walk(path_to_pages):
    faculty_html_pages.extend(file_names)
    break
