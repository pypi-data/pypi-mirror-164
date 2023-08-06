#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Sliding Window Extraction for Candidate Synonym Swapping """


from typing import Callable

from baseblock import Stopwatch
from baseblock import BaseObject

from dbpedia_tag.dmo import SlidingWindowExtract
from dbpedia_tag.dmo import SlidingWindowValidate


class ExactMatchFinder(BaseObject):
    """ Perform Sliding Window Extraction for Candidate Synonym Swapping """

    def __init__(self,
                 gram_size: int,
                 entity_exists: Callable):
        """
        Created:
            24-Aug-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._gram_size = gram_size
        self._entity_exists = entity_exists

    def _process(self,
                 tokens: list) -> list:

        candidates = SlidingWindowExtract(
            tokens=tokens,
            gram_size=self._gram_size).process()

        if not candidates or not len(candidates):
            return None

        candidates = SlidingWindowValidate(
            candidates=candidates,
            entity_exists=self._entity_exists).process()

        return candidates

    def process(self,
                tokens: list) -> list:
        sw = Stopwatch()

        results = self._process(tokens)

        if self.isEnabledForInfo:

            def total_results() -> int:
                if results:
                    return len(results)
                return 0

            if self.isEnabledForInfo:
                self.logger.info('\n'.join([
                    "Sliding Window Completed",
                    f"\tGram Size: {self._gram_size}",
                    f"\tTotal Results: {total_results()}",
                    f"\tTotal Time: {str(sw)}"]))

        return results
