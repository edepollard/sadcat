#
# SadCat
#
# Author: Ed Pollard
# Purpose: Display an ASCII Art Sad Cat
# License: MIT
# ASCII Art Attribution: Artist: Unknown / Origin: Internet (Source unverified)
#
#

class SCTests():
    @property
    def sc(self):
        if '_sc' not in self.__dict__:
            self._sc = SadCat()
        return self._sc

    @property
    def tests(self):
        if '_tests' not in self.__dict__:
           self._tests = {
                            'all':None,
                            'list_tests':None,
                            'title':None,
                            'text':None,
                            'as_str': self.sc.as_str,
                            'as_str_w_title': self.sc.as_str_w_title,
                            'as_list': self.sc.as_list,
                            'as_list_w_title': self.sc.as_list_w_title,
                            'license': self.sc.license,
                            'license_text': self.sc.license_text,
                            'attribution': self.sc.attribution,
                            'height': self.sc.height,
                            'width': self.sc.width,
                         }
        return self._tests

    @property
    def all_tests_list(self):
        if '_all_tests_list' not in self.__dict__:
            self._all_tests_list = [t for t in self.tests\
                                      if t not in ['list_tests','title']]
        return self._all_tests_list

    @property
    def all_tests(self):
        if '_all_tests' not in self.__dict__:
            self._all_tests = [t for t in self.tests if self.tests[t]]
        return self._all_tests

    @classmethod
    def all_arguments(cls):
        return [t for t in cls().tests]

    def _pretty_print_list(self, tlist, indent=4):
        print("[")
        for l in tlist:
            print(f"{' '*indent}\"{l}\",")
        print("]")

    def run_tests(self, args):
        test = args['test']
        quiet = args['quiet']
        if test == 'list_tests':
            tests = ", ".join(self.all_tests_list)
            print(f"Available Tests: {tests}")
        elif test == 'all':
            for t in self.all_tests:
                if not quiet:
                    print(f"Test: {t}")
                if t in ['as_list','as_list_w_title']:
                    self._pretty_print_list(self.tests[t])
                else:
                    print(f"{self.tests[t]}\n\n")
        elif test == 'title':
            print(self.tests['as_str_w_title'])
        elif test == 'text':
            print(self.tests['as_str'])
        elif test in ['as_list','as_list_w_title']:
            self._pretty_print_list(self.tests[test])
        else:
            print(self.tests[test])



class SadCat:

    def __init__(self):
        sc = []
        sc.append("            ＿＿   ")
        sc.append("          /＞ 　`フ")
        sc.append("          | _   _l ")
        sc.append("       ／` ミ＿xノ ")
        sc.append("      /　　 　|    ")
        sc.append("     / ヽ　　 ﾉ    ")
        sc.append("    │　|　|　|     ")
        sc.append("／￣|　|　|　|     ")
        sc.append("| (￣ヽヽ_)'_)     ")
        self.sadcat = {
                        'cat' :sc,
                        'tail':"＼二つ             ",
                        'tail_title':"＼二つ  Sad Cat    ",
                        'attribution':"ASCII Art: Sad Cat\n"+\
                                      "Artist: Unknown / Origin: "+\
                                      "Internet (Source unverified)",
                        'license':"MIT (python source only, "+
                                  "no claim made for ASCII Art)",
                      }


    def __call__(self):
        return self.as_list

    def __str__(self):
        return "SadCat ASCII Art"

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    @property
    def attribution(self):
        return self.sadcat['attribution']

    @property
    def license(self):
        return self.sadcat['license']

    @property
    def as_list(self):
        return self.sadcat['cat']+[self.sadcat['tail']]

    @property
    def as_list_w_title(self):
        return self.sadcat['cat']+[self.sadcat['tail_title']]

    @property
    def as_str(self):
        return "\n".join(self.as_list)

    @property
    def as_str_w_title(self):
        return "\n".join(self.as_list_w_title)

    @property
    def height(self):
        return len(self.as_list)

    @property
    def width(self):
        return max([len(c) for c in self.as_list])

    @property
    def license_text(self):
        return """
MIT License

Copyright (c) 2026 Ed Pollard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


