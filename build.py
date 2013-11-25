import markdown
import pdfkit

CONSTRUCTIVE_SYSTEM = ['constructive/opening.md']
DEFENSIVE_SYSTEM = ['defensive/opening_lead.md']

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<body>
%(body)s
</body>
</html>
"""

# def concatenate_file_path_array_to_string(file_path_ary):
#     content = ''
#     for file_name in file_path_ary:
#         file = open(file_name)
#         content += file.read() + '\n'
#     return content

def markdown_to_html(md_string):
    return markdown.markdown(md_string, 
                             extensions=['extra'], 
                             output_format='html5')

def html_to_pdf(html_ary, output_file):
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdfkit.from_string(html_ary, output_file, options=options, toc={})

def mds_to_pdf(md_file_ary, output_file):
    htmls = []
    for md_file in md_file_ary:
        file = open(md_file)
        content = file.read()
        file.close()
        htmls.append(markdown_to_html(content))

    html_to_pdf(htmls, output_file)


if __name__ == '__main__':
    mds_to_pdf(CONSTRUCTIVE_SYSTEM, 'constr.pdf')
    mds_to_pdf(DEFENSIVE_SYSTEM, 'defense.pdf')

