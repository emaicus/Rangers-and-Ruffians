import sys
import os

class markdown_handler:
    def __init__(self, start_heading, heading_level=1, file=None,):
      # dict of heading to content
      self.BUFFER = dict()
      self.current_heading = ''
      self.file = file
      self.start_heading(start_heading, heading_level)
      self.ordering = list()

      # Clear the file if it exists
      if file is not None:
        if os.path.exists(self.file):
          val = input(f'WARNING: File {file} already exists. Is it alright to overwrite it? (y,n) ')
          if val.strip().lower() != 'y':
            print('terminating')
            sys.exit(1)
          with open(self.file, 'w') as append_file:
            append_file.write('')

    def start_heading(self, heading, level):
      if level <= 0 or level >= 6:
        print("ERROR cannot print heading level {level}")
        sys.exit(1)
      
      self.BUFFER[heading] = {
        'level' : level,
        'content' : ''
      }
      self.current_heading = heading

    def add_whitespace(self):
      self.BUFFER[self.current_heading]['content'] += '  \n'

    def line(self, line):
      self.BUFFER[self.current_heading]['content'] += f'{line} '

    def paragraph(self, line):
      self.line(line)
      self.add_whitespace()

    def chart_row(self, fields):
      bookend = '|'
      str_fields = [str(x) for x in fields]
      middle = ' | '.join(str_fields)
      self.BUFFER[self.current_heading]['content'] += f'{bookend} {middle} {bookend}  \n'

    def chart_title(self, fields):
      self.add_whitespace()
      self.chart_row(fields)

      p = ' | '
      for i in range(len(fields)):
        p += '--------|'
      self.BUFFER[self.current_heading]['content'] += f'{p}\n'

    # DANGER: When called directly, does not remove heading from ordering on flush.
    def _write_section(self, heading, flush=True):
      if heading not in self.BUFFER:
        print(f'ERROR: Bad heading {heading}')
        sys.exit(1)
      
      md_heading = f""

      section = f"  \n{'#' * self.BUFFER[heading]['level']} {heading}\n {self.BUFFER[heading]['content']}"

      if self.file is None:
        print(section)
      else:
        with open(self.file, 'a') as append_file:
          append_file.write(f'{section}\n')
      if flush:
        del self.BUFFER[heading] #self.BUFFER[heading]['content'] = ''

    def write_buffer(self, flush=True):
      keys = list(self.BUFFER.keys())

      if len(self.ordering) > 0:
        for section in self.ordering:
          if section not in keys:
            print(f'ERROR: Ordering referenced bad section {section}')
            sys.exit(1)
          self._write_section(section, flush = False)
        if flush == True:
          for section in set(self.ordering):
            del self.BUFFER[section]
      else:
        for heading in keys:
          self._write_section(heading, flush)

    def order_next(self, section):
      self.ordering.append(section)


    def verify_empty_buffer(self):
      left = list(self.BUFFER.keys())
      if len(left) > 0:
        print(f"ERROR: the following elements remained in the buffer. {left}")
        sys.exit(1)

    def write_toc(self):
      keys = list(self.BUFFER.keys())
      toc_buffer = ''

      if len(self.ordering) == 0:
        for key in keys:
          toc_buffer += f'[{key}](#{key.replace(" ", "-").lower()})  \n'
      else:
        for key in self.ordering:
          toc_buffer += f'[{key}](#{key.replace(" ", "-").lower()})  \n'


      if self.file is None:
        print(toc_buffer)
      else:
        with open(self.file, 'a') as append_file:
          append_file.write(f'{toc_buffer}\n')