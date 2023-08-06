#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable

from baseblock import Enforcer
from baseblock import BaseObject


class DBPediaContentNormalizer(BaseObject):
    """ Normalize the DBPedia Content Section """

    def __init__(self,
                 segmenter: Callable):
        """ Change Log

        Created:
            14-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/dbpedia/issues/1
        """
        BaseObject.__init__(self, __name__)
        self._segmenter = segmenter

    def _process(self,
                 content: list) -> list:

        def _split() -> list:
            master = []

            for item in content:
                for line in item.split('\n'):
                    master.append(line)

            master = [line.strip() for line in master if line]
            master = [line for line in master if line and len(line)]

            return master

        def _sentencize(lines: list) -> list:

            master = []
            for line in lines:
                while '  ' in line:
                    line = line.replace('  ', ' ')

                [master.append(x)
                 for x in self._segmenter(input_text=line)]

            master = [line.strip() for line in master if line]
            master = [line for line in master if line and len(line)]

            return master

        return _sentencize(_split())

    def process(self,
                content: list) -> list:
        return self._process(content)
