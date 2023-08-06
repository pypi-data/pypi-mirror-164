#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd

from baseblock import EnvIO
from baseblock import Stopwatch
from baseblock import BaseObject


class DbPediaRedirectsLookup(BaseObject):
    """ Given a dbPedia title, lookup the list of dbPedia Redirects """

    def __init__(self):
        """ Change Log

        Created:
            14-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/dbpedia/issues/1
        """
        BaseObject.__init__(self, __name__)
        sw = Stopwatch()
        file_path = EnvIO.str_or_exception('REDIRECTS_FILE')
        self._df_redirects = pd.read_csv(file_path,
                                         sep="\t",
                                         encoding="utf-8")

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Finished Loading Redirects File",
                f"\tTotal Time: {str(sw)}"]))

    def _lookup(self,
                input_text: str) -> list:

        canon = input_text.lower().strip()
        if '_' in canon:
            canon = canon.replace('_', ' ')

        df = self._df_redirects
        df2 = df[df['Canon'] == canon]

        def _variants() -> list:
            if df2.empty:
                return []
            s = set(df2['Variant'].unique())
            s = [x for x in s if type(x) == str]
            return sorted(s)

        variants = _variants()
        variants = [x.replace('_', ' ') for x in variants
                    if '(' not in x]

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Located Variations",
                f"\tCanon: {canon}",
                f"\tTotal Variants: {len(variants)}",
                f"\tVariants: {variants}"]))

        return variants

    def process(self,
                input_text: str) -> list:
        return self._lookup(input_text)
