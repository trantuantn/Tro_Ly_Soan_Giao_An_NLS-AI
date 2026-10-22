"""Regression tests for structural integrity and QA blockers, not lesson quality."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/lesson-planning-nls-ai'
spec=importlib.util.spec_from_file_location('validator',SKILL/'scripts/validate_skill.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

def valid_form():
    return {'scores':{k:{'points':m,'evidence':'Synthetic fixture; not factual proof'} for k,m in v.WEIGHTS.items()},
            'gates':{k:{'status':'pass','evidence':'Synthetic fixture for blocker logic'} for k in v.GATES},
            'unresolved_core_sources':[], 'total_minutes':35,
            'activities':[{'minutes':5},{'minutes':15},{'minutes':10},{'minutes':5}]}

class ValidationTests(unittest.TestCase):
    def setUp(self): self.q=valid_form()
    def status(self): return v.validate_qa(self.q)['status']
    def test_package(self): self.assertEqual(v.validate_package(SKILL),[])
    def test_100_pass(self): self.assertEqual(self.status(),'pass')
    def test_85_boundary(self):
        self.q['scores']['accuracy']['points']=10
        self.assertEqual(self.status(),'pass')
    def test_below_threshold(self):
        self.q['scores']['accuracy']['points']=9.5
        self.assertEqual(self.status(),'needs_revision')
    def test_each_hard_gate_failure(self):
        for g in v.GATES:
            with self.subTest(g=g):
                self.q=valid_form();self.q['gates'][g]['status']='fail'
                self.assertEqual(self.status(),'needs_revision')
    def test_unknown_not_pass(self):
        self.q['gates']['HG4']['status']='unknown'
        self.assertEqual(self.status(),'needs_revision')
    def test_core_source_blocks(self):
        self.q['unresolved_core_sources']=['Official YCCD unverified']
        self.assertEqual(self.status(),'needs_revision')
    def test_overtime_blocks(self):
        self.q['activities'][0]['minutes']=10
        self.assertEqual(self.status(),'needs_revision')
    def test_undertime_blocks(self):
        self.q['activities'][0]['minutes']=1
        self.assertEqual(self.status(),'needs_revision')
    def test_negative_minutes_invalid(self):
        self.q['activities'][0]['minutes']=-1
        self.assertEqual(self.status(),'invalid')
    def test_missing_category_invalid(self):
        del self.q['scores']['safety'];self.assertEqual(self.status(),'invalid')
    def test_over_max_invalid(self):
        self.q['scores']['accuracy']['points']=26;self.assertEqual(self.status(),'invalid')
    def test_bool_score_invalid(self):
        self.q['scores']['safety']['points']=True;self.assertEqual(self.status(),'invalid')
    def test_nonfinite_score_invalid(self):
        self.q['scores']['safety']['points']=float('nan');self.assertEqual(self.status(),'invalid')
    def test_evidence_required(self):
        self.q['gates']['HG2']['evidence']='';self.assertEqual(self.status(),'invalid')
    def test_missing_gate_invalid(self):
        del self.q['gates']['HG3'];self.assertEqual(self.status(),'invalid')
    def test_unknown_status_invalid(self):
        self.q['gates']['HG1']['status']='probably';self.assertEqual(self.status(),'invalid')
    def test_qa_not_object(self): self.assertEqual(v.validate_qa([])['status'],'invalid')
    def test_empty_activities_invalid(self):
        self.q['activities']=[];self.assertEqual(self.status(),'invalid')
    def test_missing_unresolved_invalid(self):
        del self.q['unresolved_core_sources'];self.assertEqual(self.status(),'invalid')
    def test_missing_resource(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/SKILL.name;shutil.copytree(SKILL,p)
            (p/'references/ai-safety.md').unlink()
            self.assertTrue(any('ai-safety' in x for x in v.validate_package(p)))
    def test_escape_link(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/SKILL.name;shutil.copytree(SKILL,p)
            with (p/'SKILL.md').open('a') as f:f.write('\n[unsafe](../../../other.md)\n')
            self.assertTrue(any('escapes' in x for x in v.validate_package(p)))
    def test_native_materialized_folder(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/('skill-'+'a'*32);shutil.copytree(SKILL,p)
            self.assertEqual(v.validate_package(p),[])
    def test_invalid_name(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/SKILL.name;shutil.copytree(SKILL,p)
            f=p/'SKILL.md';f.write_text(f.read_text().replace('name: lesson-planning-nls-ai','name: INVALID_NAME'))
            self.assertTrue(any('name' in x for x in v.validate_package(p)))

if __name__=='__main__': unittest.main()
