#!/usr/bin/env python3
import json
import tempfile
import unittest
from pathlib import Path

import depth6_32_keymeta_aggregate as A


class AggregateTests(unittest.TestCase):
    def test_json_safe_gate_serializes_tuple_q_keys_without_losing_counts(self):
        gate={
            'kind':'BQG_DEPTH6_32_KEYMETA_UNION_GATE',
            'q_block_occupancy':{('v0',(1,2)):3,('v2',(3,4)):5},
            'q_row_totals':{('v0',(1,2)):7,('v2',(3,4)):11},
            'blocks':2,'columns':4,
            'rank_certified':False,'numerical_closure_claimed':False,
        }
        got=A.json_safe_gate(gate)
        encoded=json.dumps(got,sort_keys=True)
        self.assertIn('v0',encoded)
        self.assertEqual(8,sum(got['q_block_occupancy'].values()))
        self.assertEqual(18,sum(got['q_row_totals'].values()))
        self.assertFalse(got['rank_certified'])

    def test_write_gate_is_atomic_and_json_readable(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'gate.json'
            A.write_json_gate(p,{
                'q_block_occupancy':{('q',(1,)):1},
                'q_row_totals':{('q',(1,)):2},
                'rank_certified':False,
                'numerical_closure_claimed':False,
            })
            got=json.loads(p.read_text())
            self.assertEqual(1,sum(got['q_block_occupancy'].values()))
            self.assertEqual(2,sum(got['q_row_totals'].values()))


if __name__=='__main__': unittest.main()
