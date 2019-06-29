#!/usr/bin/env python3

import os
import subprocess
from typing import Dict
import unittest

from parameterized import parameterized

from constants import ROOT_DIR


PROBLEMS_DIR = os.path.join(ROOT_DIR, 'problems')
TEXTS_DIR = os.path.join(ROOT_DIR, 'problems', 'texts')


class TestProblems(unittest.TestCase):

    texts: Dict[str, str] = {}

    def setUp(self):
        for file_name in os.listdir(TEXTS_DIR):
            number = file_name[:3]
            self.texts[number] = file_name

    @parameterized.expand([
        ('001', 233168),
        ('002', 4613732),
        ('003', 6857),
        ('004', 906609),
        ('005', 232792560),
        ('006', 25164150),
        ('007', 104743),
        ('008', 23514624000),
        ('009', 31875000),
        ('010', 142913828922),
        ('011', 70600674),
        ('012', 76576500),
        ('013', 5537376230),
        ('014', 837799),
        ('015', 137846528820),
        ('016', 1366),
        ('017', 21124),
        ('018', 1074),
        ('019', 171),
        ('020', 648),
        ('021', 31626),
        ('022', 871198282),
        ('023', 4179871),
        ('024', 2783915460),
        ('025', 4782),
        ('026', 983),
        ('027', -59231),
        ('028', 669171001),
        ('029', 9183),
        ('030', 443839),
        ('031', 73682),
        ('032', 45228),
        ('033', 100),
        ('034', 40730),
        ('035', 55),
        ('036', 872187),
        ('037', 748317),
        ('038', 932718654),
        ('039', 840),
        ('040', 210),
        ('041', 7652413),
        ('042', 162),
        ('043', 16695334890),
        ('045', 1533776805),
        ('048', 9110846700),
        ('055', 249),
    ])
    def test_problems(self, number: str, expected: int) -> None:
        cmd = [
            'python',
            os.path.join(PROBLEMS_DIR, f'{number}_problem.py'),
        ]

        if number in self.texts:
            text = os.path.join(TEXTS_DIR, self.texts[number])
            with open(text) as input:
                self.assertEqual(
                    int(subprocess.check_output(cmd, stdin=input)),
                    expected,
                )
        else:
            self.assertEqual(int(subprocess.check_output(cmd)), expected)

        return


if __name__ == '__main__':
    unittest.main()
