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

def concatenate_file_path_array_to_string(file_path_ary):
    content = ''
    for file_name in file_path_ary:
        file = open(file_name)
        content += file.read() + '\n'
    return content

def markdown_to_html(md_string):
    return markdown.markdown(md_string, 
                             extensions=['extra'], 
                             output_format='html5')

def html_to_pdf(html_string, output_file):
    pdfkit.from_string(html_string, output_file)

if __name__ == '__main__':
    content = concatenate_file_path_array_to_string(CONSTRUCTIVE_SYSTEM)
    body = markdown_to_html(content)
    html_content = HTML_TEMPLATE % {'body': body}
    html_to_pdf(html_content, 'constructive_bidding_system.pdf')
    # file = open('constructive_bidding_system.html', 'w')
    # file.write(html_content)
