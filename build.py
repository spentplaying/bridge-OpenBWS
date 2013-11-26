import markdown
import pdfkit

CONSTRUCTIVE_SYSTEM = ['constructive/opening.md']
DEFENSIVE_SYSTEM = ['defensive/opening_lead.md',
                    'defensive/defense_signal.md',
                    'defensive/rubens_overcall.md',
                    ]

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<link rel="stylesheet" href="bootstrap.min.css">
</head>
<body>
%s
</body>
</html>
"""

def markdown_to_html(md_string):
    return markdown.markdown(md_string, 
                             extensions=['extra'], 
                             output_format='html5')

def html_files_to_pdf(html_files, output_file):
    options = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': "UTF-8",
        'grayscale': None,
        'outline-depth':3,
        'footer-center':'[page]',
        'footer-line': None,
    }
    toc = {
        'xsl-style-sheet':'output/toc.xml',
    }
    pdfkit.from_file(html_files, output_file, options=options, toc=toc)

def mds_to_pdf(md_file_ary, output_file):
    html_files = []
    count = 0
    for md_file in md_file_ary:
        file = open(md_file)
        content = file.read()
        file.close()

        count = count + 1
        content = markdown_to_html(content)

        html_file = 'output/' + str(count) + '.html'
        file = open(html_file, 'w+')
        content = file.write(HTML_TEMPLATE % content)
        file.close()
        html_files.append(html_file)

    html_files_to_pdf(html_files, output_file)


if __name__ == '__main__':
    mds_to_pdf(CONSTRUCTIVE_SYSTEM, 'output/constr.pdf')
    mds_to_pdf(DEFENSIVE_SYSTEM, 'output/defense.pdf')

