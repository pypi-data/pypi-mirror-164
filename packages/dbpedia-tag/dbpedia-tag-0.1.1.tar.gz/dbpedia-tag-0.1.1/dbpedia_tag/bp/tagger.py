
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable

from baseblock import Stopwatch
from baseblock import BaseObject
from baseblock import ServiceEventGenerator

from dbpedia_tag.svc import ExactMatchFinder
from dbpedia_ent.bp import Finder


class Tagger(BaseObject):
    """ Orchestrate Taxonomy Generation """

    def __init__(self):
        """ Change Log:

        Created:
            24-Aug-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._generate_event = ServiceEventGenerator().process

    def process(self,
                input_text: str):

        sw = Stopwatch()
        output_events = []

        d_canons = {}
        d_coords = {}

        input_text = input_text.strip()
        original_text = input_text
        entity_exists = Finder().exists

        for i in reversed(range(1, 4)):

            tokens = input_text.split()

            svc = ExactMatchFinder(gram_size=i,
                                   entity_exists=entity_exists)

            validated = svc.process(tokens)

            for item in validated:

                key = f"entity_{item.replace(' ', '_').lower()}"

                x = original_text.index(item)
                y = x + len(item)

                d_coords[key] = [x, y]
                d_canons[key] = item

                input_text = input_text.replace(item, key)

        output_events.append(self._generate_event(
            service_name=self.component_name(),
            event_name='tagger',
            stopwatch=sw,
            data={
                'input_text': original_text,
                'output_text': input_text,
                'canons': d_canons,
                'coords': d_coords,
            }))

        return {
            'text': input_text,
            'events': output_events
        }
