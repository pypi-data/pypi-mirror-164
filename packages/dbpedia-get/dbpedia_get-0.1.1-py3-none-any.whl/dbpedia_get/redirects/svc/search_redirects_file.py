#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Search Redirects file for a given Term """

import os

from baseblock import BaseObject

from dbpedia.redirects.dmo import DbPediaRedirectsLookup


class SearchRedirectsFile(BaseObject):
    """ Search Redirects file for a given Term """

    def __init__(self):
        """ Change Log

        Created:
            14-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/dbpedia/issues/1
        """
        BaseObject.__init__(self, __name__)
        self._lookup = DbPediaRedirectsLookup()

    def process(self,
                input_text: str) -> None:

        self._lookup.process(input_text)
