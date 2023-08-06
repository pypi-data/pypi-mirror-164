#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" dbPedia Orchestrator for dbPedia Redirects """

import os

from baseblock import EnvIO
from baseblock import BaseObject

from dbpedia.redirects.svc import SearchRedirectsFile
from dbpedia.redirects.svc import GenerateRedirectsFile


class RedirectsOrchestrator(BaseObject):
    """ dbPedia Orchestrator for dbPedia Redirects """

    def __init__(self):
        """ Change Log

        Created:
            14-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/dbpedia/issues/1
        """
        BaseObject.__init__(self, __name__)

    def generate(self) -> dict:
        GenerateRedirectsFile().process()

    def search(self) -> dict:
        input_text = EnvIO.str_or_exception('REDIRECTS_SEARCH_TERM')
        SearchRedirectsFile().process(input_text)
