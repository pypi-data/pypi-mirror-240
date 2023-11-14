# Manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Business Source Licence: https://mariadb.com/bsl11
"""
file generator

"""
from itertools import chain
from copy import deepcopy

from manuscriptify.formatter import Formatter
from manuscriptify.constants import SPECIAL_PARTS
from manuscriptify.constants import WEBSITE_LINK


class Parser(list):

    started = False
    front_matter = []
    matter = []
    text_styles = []
    paragraph_styles = []
    header = []

    def __init__(self, **kwargs):
        if kwargs['type'] == 'manuscript':
            self._get_front_matter(**kwargs)
            self._get_matter(**kwargs) # this is here instead of after if because of self._start_here behaviour
            pos, _ = self._requestify(self.front_matter, 1)
        else:
            self._get_matter(**kwargs)
            pos = 124

        _, self.wc = self._requestify(self.matter, pos)

        title_page = [{'insertText': dict(**fm)}
                      for fm in self.front_matter]
        content = [{'insertText': dict(**m)}
                    for m in self.matter]
        style_updates = [{'updateTextStyle': dict(**s)}
                         for s in self.text_styles]
        ps_updates = [{'updateParagraphStyle': dict(**p)}
                      for p in self.paragraph_styles]

        self._get_header(**kwargs)

        requests = chain(title_page,
                         content,
                         style_updates,
                         ps_updates,
                         self.header)

        super().__init__(list(requests))

    def _get_front_matter(self, **kwargs):
        """compose the title page"""
        if kwargs['final']:
            fields = [
                kwargs['reply_to'],
                kwargs['street1'],
                kwargs['street2'],
                kwargs['phone'],
                kwargs['email']
            ]
        else:
            fields = [
                'This manuscript',
                'was compiled by',
                'Manuscriptify.',
                ' ',
                ' ',
            ]
        basic = Formatter.matter()
        st = Formatter.address()
        self.front_matter = [
            {
                'content': f'{field}\n',
                'textStyle': deepcopy(basic),
                'paragraphStyle': st
            }
            for field in fields
        ]
        if not kwargs['final']:
            self.front_matter[2]['textStyle'].update(WEBSITE_LINK)
        st = Formatter.title()
        title = {
            'content': f'{kwargs["title"].upper()}\n',
            'textStyle': basic,
            'paragraphStyle': st
        }
        st = Formatter.subtitle()
        author = {
            'content': f'{kwargs["pseudonym"]}\n',
            'textStyle': basic,
            'paragraphStyle': st
        }
        st = Formatter.section()
        cat = f'{kwargs["category"]}\n'
        category = {
            'content': cat,
            'textStyle': basic,
            'paragraphStyle': st
        }
        ge = f'{kwargs["genre"]}\n'
        genre = {
            'content': ge,
            'textStyle': basic,
            'paragraphStyle': st
        }
        self.front_matter += [
            title,
            author,
            category,
            genre
        ]

    def _get_matter(self, **kwargs):
        """compose the prose"""
        basic = Formatter.matter()
        ch_count = 1
        section_index = 1
        for i, c in enumerate(kwargs['content']):
            if 'sectionBreak' in c:
                if c['sectionBreak']['sectionStyle']['sectionType'] == 'CONTINUOUS':
                    if section_index > 1:
                        st = Formatter.section()
                        section = {
                            'content': '#\n',
                            'textStyle': basic,
                            'paragraphStyle': st
                        }
                        self.matter.append(section)
                    section_index += 1
                else:

                    # ignore page breaks
                    pass

            else:
                try:
                    ps = c['paragraph']['paragraphStyle']
                except KeyError:

                    # table of contents etc
                    continue

                style = ps['namedStyleType']
                for elem in c['paragraph']['elements']:
                    if self._looks_special(elem):
                        content = elem['textRun']['content']
                        big_c = content.strip().upper()
                        if big_c in SPECIAL_PARTS:
                            if ch_count == 1 and not self.started:
                                self._start_here()
                            st = Formatter.prologue()
                            prologue = {
                                'content': big_c,
                                'textStyle': basic
                            }
                            self.matter.append(prologue)
                        elif content == '\n':
                            continue
                        elif big_c.startswith('CHAPTER '):
                            if ch_count == 1 and not self.started:
                                self._start_here()
                            if ':' in content:

                                # normal scenario
                                ch_num, ch_name = [x.strip() for x in
                                                   content.split(':', 1)]
                                ch_num = ch_num.upper()
                                if ch_name.endswith('~~'):
                                    ch_num += " (cont'd)"
                                    ch_name = ch_name.strip('~')

                                # no chapters scenario
                                elif ch_name.endswith('%%'):
                                    ch_num = ch_name.strip('%').upper()
                                    ch_name = None
                            else:

                                # dogfooding scenario
                                next_c = kwargs['content'][i + 1]
                                next_style = next_c['paragraph']['paragraphStyle']
                                if ('alignment' in next_style and
                                    next_style['alignment'].lower() == 'center'):
                                    kwargs['content'].pop(i + 1)
                                    elem = next_c['paragraph']['elements'][0]
                                    ch_name = elem['textRun']['content'].strip()
                                else:

                                    # jon scenario
                                    ch_name = None

                            st = Formatter.heading()
                            heading = {
                                'content': f'{ch_num}\n',
                                'textStyle': basic,
                                'paragraphStyle': st
                            }
                            self.matter.append(heading)
                            if ch_name:
                                st = Formatter.subheading()
                                subheading = {
                                    'content': f'{ch_name}\n',
                                    'textStyle': basic
                                }
                                self.matter.append(subheading)
                            else:

                                # regardless of scenario, we need a nice
                                # gap between that chunk and what follows
                                del self.matter[-1]['paragraphStyle']
                                st.update(Formatter.subheading())

                            ch_count += 1
                        section_index = 1
                    else:
                        try:
                            t = elem['textRun']
                            t['content'] = t['content'].strip('\t')
                            if not t['content']:
                                raise KeyError
                        except KeyError:

                            # horizontal rule etc
                            ps = None
                            continue

                        if t['content'] == '\n':
                            continue
                        elif t['content'] == '#\n':

                            # avoid interpreting the default section break
                            # at the beginning of the newly created doc
                            if section_index > 1:

                                st = Formatter.section()
                                section = {
                                    'content': '#\n',
                                    'textStyle': basic
                                }
                                self.matter.append(section)
                            else:

                                # avoid fiddling with the style of the previous para
                                st = None

                            section_index += 1
                        else:
                            t['textStyle'].update(basic)
                            self.matter.append(t)
                            previous_style = None
                            j = 2
                            while not previous_style:
                                try:
                                    previous_style = self.matter[-j].get('paragraphStyle')
                                    j += 1
                                except IndexError:
                                    if len(self.matter) < 2:

                                        # novel didn't start with an identifiable chapter
                                        previous_style = {}
                                        break

                                    else:
                                        raise
                            if ('alignment' in previous_style and
                                previous_style['alignment'] == 'center'):
                                st = Formatter.first_paragraph()
                            else:
                                st = Formatter.paragraph()
                            if style != 'NORMAL_TEXT':
                                if ps:
                                    st = {
                                        k:v for k, v in ps.items()
                                        if k in [
                                            'namedStyleType',
                                            'alignment'
                                        ]
                                    }

                # apply paragraphStyle to any text element of the para
                if st:
                    self.matter[-1]['paragraphStyle'] = st

                # make sure the fragment ends with a EOL char
                if not self.matter[-1]['content'].endswith('\n'):
                    self.matter[-1]['content'] += '\n'

        if kwargs['final']:
            st = Formatter.ending()
            ending = {
                'content': 'THE END',
                'textStyle': basic,
                'paragraphStyle': st
            }
            self.matter.append(ending)

    def _requestify(self, stuff, pos):
        """transpose the stuff into batchUpdate-flavoured requests"""
        wc = 0
        for i, s in enumerate(stuff):
            try:
                text = stuff[i].pop('content')
                stuff[i]['text'] = text
                stuff[i]['location'] = {'index': pos}
                end_index = pos + len(text)
                if text != '#\n':
                    wc += len(text.split())
                range_ = {
                    'startIndex': pos,
                    'endIndex': end_index
                }
                if s['textStyle']:
                    style = stuff[i].pop('textStyle')
                    text_style = {
                        'range': range_,
                        'textStyle': style,
                        'fields': ','.join(style.keys())
                    }
                    self.text_styles.append(text_style)
                else:
                    del stuff[i]['textStyle']
            except KeyError:
                pass
            except AttributeError:
                pass
            if 'paragraphStyle' in s:
                style = stuff[i].pop('paragraphStyle')
                ps = {
                    'range': range_,
                    'paragraphStyle': style,
                    'fields': ','.join(style.keys())
                }
                self.paragraph_styles.append(ps)
            pos = end_index
        return pos, wc

    def _get_header(self, **kwargs):
        """add the headers"""
        author_surname = kwargs['pseudonym'].split()[-1]
        title = (kwargs['title'] if
                 len(kwargs['title'].split()) < 4
                 else kwargs['shortname'])
        end_index = len(author_surname + title) + 6
        self.header = [{
            'insertText': {
                'location': {
                    'segmentId': kwargs['header_id'],
                    'index': 0
                },
                'text': (f'{author_surname} / '
                         f'{title.upper()} / ')
            }
        }]
        range_ = {
            'startIndex': 0,
            'endIndex': end_index,
            'segmentId': kwargs['header_id']
        }
        ts = Formatter.matter()
        self.header.append({
            'updateTextStyle': {
                'range': range_,
                'textStyle': ts,
                'fields': ','.join(ts.keys())
            }
        })
        st = Formatter.right()
        self.header.append({
            'updateParagraphStyle': {
                'range': range_,
                'paragraphStyle': st,
                'fields': ','.join(st.keys())
            }
        })

    @staticmethod
    def _looks_special(elem):
        """determine if an element looks like a beginning"""
        try:
            content = elem['textRun']['content']
            big_c = content.strip().upper()
            return (big_c in SPECIAL_PARTS or
                    big_c.startswith('CHAPTER '))
        except KeyError:
            return False

    def _start_here(self):
        """start rendering from this point"""
        self.matter = []
        self.text_styles = []
        self.paragraph_styles = []
        self.started = True
