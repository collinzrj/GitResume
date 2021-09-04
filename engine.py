import json
import os

header = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
% \usepackage[a4paper, total={6in, 8in}]{geometry}
\usepackage[left=0.5in,top=0.6in,right=0.5in,bottom=0.6in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
    pdftitle={Overleaf Example},
    pdfpagemode=FullScreen,
    }

\begin{document}
"""

title = """
\\begin{{center}}
{{\\huge \\textbf{{{}}}}}\par
{}
\end{{center}}
"""

education_header = r"""
\noindent
{\textbf{EDUCATION}}\newline
\rule{\textwidth}{1pt}\newline
"""

footer = r"\end{document}"

education_school = "{{\\textbf {{{}}}}}\\newline\n"
education_major = "\\emph {{{}}}.\\newline\n"
education_duration = "{{{}}}\\newline\n"

section_header = """
\\noindent
{{\\textbf{{{}}}}}\\newline
\\rule{{\\textwidth}}{{1pt}}\\newline"""

item_title = "{{\\textbf{{{}}}}}\\newline\n"
item_description = "\\emph{{{}}}\n"
item_bullets = """\\begin{{itemize}}[leftmargin=*]
{}
\end{{itemize}}"""

if __name__ == '__main__':
    with open('resume.json') as f:
        resume = json.load(f)
    print(resume)
    ## Title
    name = resume["title"]["name"]
    contacts = resume["title"]["contacts"]
    contacts_string = ""
    for contact in contacts:
        contacts_string += contact + "\\par"
    title = title.format(name, contacts_string[:-4])
    print(title)
    ## Education
    education = education_header
    for school in resume["education"]:
        name = school.get("school")
        if name is not None:
            name = education_school.format(name)
            education += name
        major = school.get("major")
        if major is not None:
            major = education_major.format(major)
            education += major
        duration = school.get("duration")
        if duration is not None:
            duration = education_duration.format(duration)
            education += duration
        education += r"\newline"
    output = header + title + education
    ## Sections
    for section in resume["sections"]:
        title = section["title"]
        section_string = section_header.format(title)
        for item in section["items"]:
            subtitle = item.get("title")
            description = item.get("description")
            bullets = item.get("bullets")
            bullets_string = ""
            for bullet in bullets:
                bullets_string += r"\item " + bullet + "\n"
            item_string = ""
            item_string += item_title.format(subtitle)
            if description is not None:
                item_string += item_description.format(description)
            item_string += item_bullets.format(bullets_string)
            section_string += item_string
        output += section_string
    ## Output
    output += footer
    os.makedirs('working_directory', exist_ok=True)
    with open('working_directory/resume.tex', 'w') as f:
        f.write(output)





    
