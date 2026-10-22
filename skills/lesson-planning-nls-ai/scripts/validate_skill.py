#!/usr/bin/env python3
"""Validate package and optional human-authored QA form. Never grades factual truth."""
import argparse
import json
import math
from pathlib import Path
import re

WEIGHTS = {'accuracy':25, 'objectives':15, 'activities':20,
           'assessment':15, 'integration':15, 'safety':10}
GATES = ('HG1', 'HG2', 'HG3', 'HG4', 'HG5')
REFS = ('curriculum','source-priority','lesson-analysis','nls-framework',
        'ai-competence','pedagogy','activity-design','assessment',
        'differentiation','ai-safety','quality-gates','output-contract','sources')
ASSETS = ('lesson-plan-template','nls-mapping-template','ai-mapping-template',
          'assessment-rubric','quality-checklist')

def validate_package(root):
    root = Path(root).resolve()
    errors = []
    main = root / 'SKILL.md'
    if not main.is_file():
        return ['Missing SKILL.md']
    content = main.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n',content,re.S)
    if not match:
        errors.append('Missing YAML frontmatter delimiters')
    else:
        front = match[1]
        keys = re.findall(r'^([a-z_]+):',front,re.M)
        if sorted(keys) != ['description','name']:
            errors.append('Frontmatter must contain name and description once each')
        name_match = re.search(r'^name:\s*([a-z0-9-]+)\s*$',front,re.M)
        if not name_match or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name_match[1]) or len(name_match[1]) > 64:
            errors.append('Invalid skill name')
        elif name_match[1] != root.name and not re.fullmatch(r'skill-[0-9a-f]{32}',root.name):
            errors.append('Skill name and folder differ')
        desc = re.search(r'^description:\s*(.*?)\Z',front,re.S|re.M)
        if not desc or len(desc[1].strip()) < 40:
            errors.append('Description is absent or too short')
    if len(content.splitlines()) >= 500:
        errors.append('SKILL.md must remain under 500 lines')
    required = [root/'references'/f'{n}.md' for n in REFS]
    required += [root/'assets'/f'{n}.md' for n in ASSETS]
    required += [root/'agents/openai.yaml',root/'scripts/validate_skill.py']
    for path in required:
        if not path.is_file() or len(path.read_text(encoding='utf-8').strip()) < 60:
            errors.append(f'Missing or empty resource: {path.relative_to(root)}')
    for path in root.rglob('*.md'):
        data=path.read_text(encoding='utf-8')
        if re.search(r'\bTODO\b|\[INSERT',data):
            errors.append(f'Unfinished scaffold: {path.relative_to(root)}')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',data):
            if re.match(r'https?://',target) or target.startswith('#'):
                continue
            dest=(path.parent/target.split('#')[0]).resolve()
            if not dest.is_relative_to(root):
                errors.append(f'Link escapes skill: {target}')
            elif not dest.exists():
                errors.append(f'Broken link in {path.relative_to(root)}: {target}')
    for p in required:
        if p.suffix == '.md' and str(p.relative_to(root)) not in content:
            errors.append(f'Resource not directly discoverable: {p.relative_to(root)}')
    meta = root/'agents/openai.yaml'
    if meta.is_file() and '$lesson-planning-nls-ai' not in meta.read_text(encoding='utf-8'):
        errors.append('Agent default prompt must mention skill')
    return errors

def validate_qa(data):
    """Schema: scores={key:{points,evidence}}, gates={HGn:{status,evidence}},
    unresolved_core_sources=[...], total_minutes=number, activities=[{minutes:number}].
    Evidence is human supplied; validity of its claims is not machine verified.
    """
    errors=[]
    if not isinstance(data,dict):
        return {'status':'invalid','total':None,'errors':['QA must be an object']}
    scores=data.get('scores')
    total=0
    if not isinstance(scores,dict) or set(scores) != set(WEIGHTS):
        errors.append('scores must contain exactly six rubric categories')
    for key,maximum in WEIGHTS.items():
        item=scores.get(key) if isinstance(scores,dict) else None
        if not isinstance(item,dict):
            errors.append(f'Missing score object: {key}');continue
        points=item.get('points')
        if not number(points) or not 0 <= points <= maximum:
            errors.append(f'Invalid score: {key}')
        else:
            total+=points
        if not isinstance(item.get('evidence'),str) or not item['evidence'].strip():
            errors.append(f'Missing score evidence: {key}')
    gates=data.get('gates')
    blocked=False
    if not isinstance(gates,dict) or set(gates) != set(GATES):
        errors.append('gates must contain exactly HG1-HG5')
    for key in GATES:
        gate=gates.get(key) if isinstance(gates,dict) else None
        if not isinstance(gate,dict):
            errors.append(f'Missing gate object: {key}');continue
        if gate.get('status') not in ('pass','fail','unknown'):
            errors.append(f'Invalid gate status: {key}')
        elif gate['status'] != 'pass':
            blocked=True
        if not isinstance(gate.get('evidence'),str) or not gate['evidence'].strip():
            errors.append(f'Missing gate evidence: {key}')
    unresolved=data.get('unresolved_core_sources')
    if not isinstance(unresolved,list) or any(not isinstance(x,str) or not x.strip() for x in unresolved):
        errors.append('unresolved_core_sources must be a list of nonempty strings')
    elif unresolved:
        blocked=True
    budget=data.get('total_minutes')
    activities=data.get('activities')
    if not number(budget) or budget <= 0:
        errors.append('total_minutes must be positive')
    if not isinstance(activities,list) or not activities:
        errors.append('activities must be a nonempty list')
    else:
        durations=[a.get('minutes') if isinstance(a,dict) else None for a in activities]
        if any(not number(x) or x <= 0 for x in durations):
            errors.append('Every activity must have positive minutes')
        elif number(budget) and not math.isclose(sum(durations),budget,abs_tol=0.01):
            blocked=True
    status='invalid' if errors else ('pass' if total>=85 and not blocked else 'needs_revision')
    return {'status':status,'total':None if errors else total,'errors':errors,
            'scope':'Form consistency only; factual and pedagogical review remains human.'}

def number(value):
    return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill_dir',type=Path)
    parser.add_argument('--qa',type=Path)
    args=parser.parse_args()
    errors=validate_package(args.skill_dir)
    result={'package':'pass' if not errors else 'fail','errors':errors}
    if args.qa:
        try:
            result['qa']=validate_qa(json.loads(args.qa.read_text(encoding='utf-8')))
        except (OSError,ValueError) as exc:
            result['qa']={'status':'invalid','errors':[str(exc)]}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if errors or result.get('qa',{}).get('status','pass')!='pass' else 0

if __name__=='__main__':
    raise SystemExit(main())
