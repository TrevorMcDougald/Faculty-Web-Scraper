import glob2

path_to_pages = r"C:\Users\Trevor\Python\Faculty-Web-Scraper\Faculty-Web-Scraper\Faculty-Pages\*.html"
faculty_html_pages = glob2.glob(path_to_pages)

name_prefix = "Name: "
education_prefix = "Education: "
research_prefix = "Research Interest: "
email_prefix = "Email: "
webpage_prefix = "Webpage: "

information_list = ['name', 'education', 'research', 'email', 'webpage']
information_patterns = ["((Mr\.|Dr\.)\s(.+))</title>", "Education</h3>\s.+\s.+<p>(.+?)</p>", "Research Interests</h3>\s.+\s.+<p>(.+?)</p>",
                        'email\s(.+?)"', r"(https?:\/\/(.+?))\">Homepage"]


name_pattern = "((Mr\.|Dr\.)\s(.+))</title>"
education_pattern = "Education</h3>\s.+\s.+<p>(.+?)</p>"
research_interest_pattern = "Research Interests</h3>\s.+\s.+<p>(.+?)</p>"
email_pattern = 'email\s(.+?)"'
webpage_pattern = r"(https?:\/\/(.+?))\">Homepage"

save_path = r"C:/Users/Trevor/Python/Faculty-Web-Scraper/Faculty-Web-Scraper/Faculty-Information"
info_file = []