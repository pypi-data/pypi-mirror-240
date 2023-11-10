# -*- coding: utf-8 -*-

"""

tests.test_fix_excel_files

Unit test the postleid.fix_excel_files module

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import json

from unittest import TestCase

# import polars

# from postleid import commons
from postleid import fix_excel_files
from postleid import presets


class CICoCoLo(TestCase):

    """Test country code lookup"""

    def test_lookup(self):
        """lookup country codes on the basis of an existing ISO-3166-1 file"""
        try:
            with open(
                "/usr/share/iso-codes/json/iso_3166-1.json",
                mode="r",
                encoding="utf-8",
            ) as iso_codes_file:
                iso_codes = json.load(iso_codes_file)
        except OSError as error:
            self.skipTest(f"Error opening ISO codes file: {error}")
            return
        #
        lookup = fix_excel_files.CICoCoLo.from_config(
            default=presets.DEFAULT_CC
        )
        known_ccs = set(lookup.values())
        for country_data in iso_codes["3166-1"]:
            names = [country_data["name"]]
            try:
                names.append(country_data["official_name"])
            except KeyError:
                pass
            #
            alpha_2 = country_data["alpha_2"].lower()
            name = country_data["name"]
            if alpha_2 not in known_ccs:
                with self.subTest(cc=alpha_2, expect_defined=False):
                    self.assertRaises(
                        KeyError,
                        lookup.__getitem__,
                        alpha_2,
                    )
                #
                with self.subTest(name=name, expect_defined=False):
                    self.assertRaises(
                        KeyError,
                        lookup.__getitem__,
                        name,
                    )
                #
                continue
            #
            with self.subTest(cc=alpha_2, expect_defined=True):
                self.assertEqual(
                    lookup[alpha_2],
                    alpha_2,
                )
            #
            with self.subTest(name=name, expected=alpha_2):
                self.assertEqual(
                    lookup[name],
                    alpha_2,
                )
            #
            # existing_cc = data_fixer.lookup_country_code(alpha_2)
            # if existing_cc == expected_cc:
            try:
                official_name = country_data["official_name"]
            except KeyError:
                continue
            #
            with self.subTest(official_name=official_name, expected=alpha_2):
                self.assertEqual(
                    lookup[official_name],
                    alpha_2,
                )
            #
        #


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
