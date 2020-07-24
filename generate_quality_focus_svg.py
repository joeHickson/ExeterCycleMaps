import re

style_block = re.compile("<style(\n?[^>]*)*>(\n?[^>]*)*></style>", flags=re.MULTILINE)

def main(replacement_css, source_svg, output_filename):
    output=""
    with open(output_filename, "w") as output_file:
        with open(replacement_css) as replacement_file:
            replacement_css = replacement_file.read()
            with open(source_svg) as source_svg_file:
                source_svg = source_svg_file.read()
                for match in style_block.finditer(source_svg):
                    output += source_svg[0:match.start()]
                    output += f"""<style
         id="style9347"><![CDATA[
    {replacement_css}
    ]]></style>"""
                    output += source_svg[match.end():]
                    output_file.write(output)



if __name__ == '__main__':
    main("quality_focus.css", "Exeter Cycle Tube Map.svg", "Exeter Cycle Map Quality.svg")