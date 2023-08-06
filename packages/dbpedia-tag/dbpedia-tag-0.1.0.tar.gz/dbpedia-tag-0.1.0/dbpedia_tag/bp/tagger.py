
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable

from baseblock import BaseObject

from dbpedia_tag.svc import ExactMatchFinder


class Tagger(BaseObject):
    """ Orchestrate Taxonomy Generation """

    def __init__(self):
        """ Change Log:

        Created:
            24-Aug-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                input_text: str):

        tokens = input_text.split()

        svc = ExactMatchFinder(gram_size=2)
        svc.process(tokens)
