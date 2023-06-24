import sys
import os

# Some global variables for dealing with the buffer tuples
HEADING = 0
LEVEL = 1
CONTENT = 2
LINK = 3

def fix_link(link):
  bad_chars = [':', '(', ')', '.', '!', '?', '&', '_', ',',"'", '"']
  good_link = link.replace(' ', '-').lower()
  for c in bad_chars:
    good_link = good_link.replace(c,'')
  return good_link

class markdown_handler:
    def __init__(self, start_heading, heading_level=1, file=None, force_overwrite=False):
      # dict of heading to content
      self.encountered_dict = dict()
      self.BUFFER = list()
      self.current_heading = -1
      self.file = file
      self.start_heading(start_heading, heading_level)
      self.ordering = list()
      self.topmatter = None

      # Clear the file if it exists
      if file is not None:
        if os.path.exists(self.file):
          if not force_overwrite:
            val = input(f'WARNING: File {file} already exists. Is it alright to overwrite it? (y,n) ')
            if val.strip().lower() != 'y':
              print('terminating')
              sys.exit(1)
          with open(self.file, 'w') as append_file:
            append_file.write('')

    def start_heading(self, heading, level):
      if level <= 0 or level >= 6:
        print(f"ERROR cannot print heading level {level}")
        sys.exit(1)

      link = fix_link(heading)

      # print(f'Starting {link}')
      if link not in self.encountered_dict:
        self.encountered_dict[link] = 0
      self.encountered_dict[link] += 1

      if self.encountered_dict[link] > 1:
        # print(f'We encountered {link} twice, so we will use a special link for it')
        link = f'{link}-{self.encountered_dict[link] - 1}'


      self.BUFFER.append([heading, level, '', link])

    def add_whitespace(self):
      self.BUFFER[self.current_heading][CONTENT] += '  \n'

    def line(self, line):
      self.BUFFER[self.current_heading][CONTENT] += f'{line}'

    def paragraph(self, line):
      self.line(line)
      self.add_whitespace()

    def chart_row(self, fields):
      bookend = '|'
      str_fields = [str(x) for x in fields]
      middle = ' | '.join(str_fields)
      self.BUFFER[self.current_heading][CONTENT] += f'{bookend} {middle} {bookend}  \n'

    def chart_title(self, fields):
      self.add_whitespace()
      self.chart_row(fields)

      p = ' | '
      for i in range(len(fields)):
        p += '--------|'
      self.BUFFER[self.current_heading][CONTENT] += f'{p}\n'

    def heading_exists(self, heading):
      return True if get_heading_pos(heading) != -1 else False

    def get_heading_pos(self, heading):
      for i in range(len(self.BUFFER)):
        if self.BUFFER[i][HEADING] == heading:
          return i
      return -1

    def get_all_headings(self):
      headings = list()
      for heading, _, _, _ in self.BUFFER:
        headings.append(heading)
      return headings

    # DANGER: When called directly, does not remove heading from ordering on flush.
    def _write_section(self, heading, flush=True):
      heading_pos = self.get_heading_pos(heading)

      if heading_pos == -1:
        print(f'ERROR: Bad heading {heading}')
        sys.exit(1)

      md_heading = f""

      heading, level, content, link = self.BUFFER[heading_pos]

      section = f"  \n{'#' * level} {heading}\n{content}"

      if self.file is None:
        print(section)
      else:
        with open(self.file, 'a') as append_file:
          append_file.write(f'{section}\n')
      if flush:
        curr_len = len(self.BUFFER)
        if self.current_heading + 1 == curr_len:
          self.current_heading -= 1
        self.BUFFER.pop(heading_pos)

    def _write_topmatter(self):
      if self.topmatter is None:
        return

      with open(self.file, 'a') as append_file:
        for line in self.topmatter:
          append_file.write(f'{line}\n')
      self.topmatter = None

    def write_buffer(self, flush=True):
      keys = self.get_all_headings()

      if self.topmatter is not None:
        self._write_topmatter()

      if len(self.ordering) > 0:
        print('using ordering mode')
        for section in self.ordering:
          if section not in keys:
            print(f'ERROR: Ordering referenced bad section {section}')
            sys.exit(1)
          self._write_section(section, flush = False)
        if flush == True:
          for section in set(self.ordering):
            heading_pos = self.get_heading_pos(section)
            curr_len = len(self.BUFFER)
            if self.current_heading + 1 == curr_len:
              self.current_heading -= 1
            self.BUFFER.pop(heading_pos)
      else:
        for heading in keys:
          self._write_section(heading, flush)

    def order_next(self, section):
      self.ordering.append(section)


    def verify_empty_buffer(self):
      if len(self.BUFFER) > 0:
        print(f"ERROR: the following elements remained in the buffer. {self.BUFFER}")

    def find_nth(self, needle, n):
      haystack = self.BUFFER
      found = 0
      for val in haystack:
        if val[HEADING] == needle:
          found += 1
        if found == n:
          return val
      print(f'could not find the {n}th occurrence of {needle}')
      return None

    def write_toc(self, max_to_include=1000):
      keys = self.get_all_headings()
      toc_buffer = ''

      if len(self.ordering) == 0:
        it = keys
      else:
        it = self.ordering

      encountered_dict = dict()

      for key in it:
        if not key in encountered_dict:
          encountered_dict[key] = 0
        encountered_dict[key] += 1
        heading, level, content, link = self.find_nth(key, encountered_dict[key])

        if level > max_to_include:
          continue

        indent = f" {' '* (2*(level-1))}* "
        toc_buffer += f"{indent}[{heading}](#{link})  \n"



      if self.file is None:
        print(toc_buffer)
      else:
        with open(self.file, 'a') as append_file:
          append_file.write(f'{toc_buffer}\n')

    def slurp_markdown_lines(self, lines, explicit_ordering=False):
      for line in lines:
        # line = line.rstrip()
        if len(line.strip()) == 0:
          self.add_whitespace()
          self.add_whitespace()
        elif line.strip()[0] == '#':
          parts = line.split()
          level = len(parts[0])
          heading = ' '.join(parts[1:])
          self.start_heading(heading, level)
          if explicit_ordering:
            self.order_next(heading)
        else:
          self.line(line)


    def slurp_markdown_file(self, file, explicit_ordering=False):
      with open(file, 'r') as infile:
        lines = infile.readlines()

      self.slurp_markdown_lines(lines)

    def slurp_topmatter_file(self, file):
      with open(file, 'r') as infile:
        lines = infile.readlines()

      self.topmatter = lines


