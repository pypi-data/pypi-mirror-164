#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os

from baseblock import BaseObject

from dbpedia.redirects.dmo import DBpediaRedirectsParser


class GenerateRedirectsFile(BaseObject):
    """ Generate Entity Variations (Synonyms for Entities) """

    def __init__(self):
        """ Change Log

        Created:
            14-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/dbpedia/issues/1
        """
        BaseObject.__init__(self, __name__)

    def _generate(self,
                  input_file: str,
                  output_file: str):

        dmo = DBpediaRedirectsParser(input_file)
        df_redirects = dmo.process()

        df_redirects.to_csv(output_file,
                            sep="\t",
                            index=False,
                            encoding="utf-8")

    def process(self) -> None:

        input_file = os.environ["REDIRECTS_INFILE"]

        if not os.path.exists(input_file):
            self.logger.error('\n'.join([
                "Redirects Input File Not Found",
                f"\tPath: {input_file}"]))
            raise ValueError

        output_file = os.path.join(os.environ["PROJECT_BASE"],
                                   os.environ["REDIRECTS_OUTFILE"])

        if os.path.exists(output_file) and self.isEnabledForWarning:
            self.logger.warning('\n'.join([
                "Replacing Existing File",
                f"\tPath: {output_file}"]))

        self._generate(input_file=input_file,
                       output_file=output_file)
