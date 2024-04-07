import argparse
import os


def markdown_to_mediawiki(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # 转换加粗
            line = line.replace('**', "'''")
            # 转换标题
            if line.startswith('#'):
                level = line.count('#')
                stripped_line = line.lstrip('#').strip()
                mediawiki_heading = '=' * (level + 1) + stripped_line + '=' * (level + 1) + '\n'
                outfile.write(mediawiki_heading)
            # 转换无序列表
            elif line.strip().startswith('-'):
                mediawiki_list_item = line.replace('-', '*', 1)
                outfile.write(mediawiki_list_item)
            else:
                outfile.write(line)


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to MediaWiki format.")
    parser.add_argument('-i', '--input', required=True, help="Input Markdown file name.")
    parser.add_argument('-o', '--output', help="Output MediaWiki file name. Optional.")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else os.path.splitext(input_file)[0] + '.txt'

    markdown_to_mediawiki(input_file, output_file)
    print(f"Converted {input_file} to {output_file} successfully.")


if __name__ == "__main__":
    main()
