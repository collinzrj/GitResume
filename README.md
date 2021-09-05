# Version Control Your Resume
Now you can use git to version control your resumes. Keep track of your resume by json so that you can compare them easily, and convert it to pdf for sharing and submitting.

[Collin's Resume](resume.pdf)

## How to use it
- Fork the repository
- Edit the `resume.json`, you can use my example as a template
- run ```git config core.hooksPath .githooks``` in your terminal, this enables a script that generates the `.tex` and `.pdf` file each time you commit, you only need to run this once
- commit the edit to your `resume.json`

## Tips
- If you are familiar with git, you can take advantage of its ability of version control, e.g. create a new branch for a resume for a different company/industry, and you can keep track of the changes you made to your resume taking advantage of Github's file comparing function
