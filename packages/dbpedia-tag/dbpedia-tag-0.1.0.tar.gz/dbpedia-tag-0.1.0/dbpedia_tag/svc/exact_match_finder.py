#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Perform Sliding Window Extraction for Candidate Synonym Swapping """


from baseblock import EnvIO
from baseblock import Stopwatch
from baseblock import BaseObject

# from deepnlu.datablock import FindBlacklist

from dbpedia_tag.dmo import SlidingWindowExtract
# from deepnlu.services.mutato.dmo.exact import SlidingWindowExtract
# from deepnlu.services.mutato.dmo.exact import SlidingWindowBlacklist
# from deepnlu.services.mutato.dmo.exact import SlidingWindowLookup


class ExactMatchFinder(BaseObject):
    """ Perform Sliding Window Extraction for Candidate Synonym Swapping """

    def __init__(self,
                 gram_size: int):
        """
        Created:
            24-Aug-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)
        self._gram_size = gram_size
        

    def _process(self,
                 tokens: list) -> list:

        # # if there are no valid synonyms or entities at this gram size level
        # if self._gram_size not in self._d_lookup:
        #     return None  # ... then there is no point in proceeding any further

        candidates = SlidingWindowExtract(
            tokens=tokens,
            gram_size=self._gram_size).process()

        print(candidates)

        # if not candidates or not len(candidates):
        #     return None

        # if self._gram_size == 1:
        #     candidates = [x for x in candidates if len(
        #         [token for token in x if not 'swaps' in token])]

        # if EnvIO.is_true('SLIDING_WINDOW_BLACKLIST'):  # optional step; defaults to False
        #     if self._gram_size in self._d_candidate_synonym_blacklist:
        #         blacklist = self._d_candidate_synonym_blacklist[self._gram_size]

        #         candidates = SlidingWindowBlacklist(
        #             candidates=candidates,
        #             blacklist=blacklist,
        #             gram_size=self._gram_size).process()

        #         if not candidates or not len(candidates):
        #             return None

        # candidates = SlidingWindowLookup(
        #     candidates=candidates,
        #     gram_size=self._gram_size,
        #     d_runtime_kb=self._d_lookup).process()

        # if not candidates or not len(candidates):
        #     return None

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
