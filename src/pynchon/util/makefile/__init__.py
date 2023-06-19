import re

from pynchon import cli 
from pynchon import abcs
from pynchon.util.os import invoke

from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)
zzz = "#  recipe to execute (from '"
vvv="# Variables"
fff="# files hash-table stats:"


def _get_database(makefile, make='make'):
    """ """
    tmp = abcs.Path(makefile)
    if not all([tmp.exists,tmp.is_file,]):
        raise ValueError(f"{makefile} does not exist")
    else:
        LOGGER.warning(f"parsing makefile @ {makefile}")
    cmd = f"{make} --print-data-base -pqRrs -f {makefile}"
    resp = invoke(cmd)
    out = resp.stdout.split("\n")
    return out

def _test(x):
    """ """
    return all([
        ":" in x.strip(),
        not x.startswith("#"),
        not x.startswith("."),
        not x.startswith("\t"),
    ]
        )
def _get_prov_line(body):
    # zzz = "#  recipe to execute (from '"
    pline = [x for x in body if zzz in x]
    pline = pline[0] if pline else None
    return pline

def _get_file(body=None,makefile=None):
    pline = _get_prov_line(body)
    if pline:
        return pline.split(zzz)[-1] .split('\'')[0]
    else:
        return str(makefile)

@cli.click.argument('makefile')
def parse(
    makefile:str=None, 
    bodies=False,
    **kwargs):
    """ """
    import os 
    assert os.path.exists(makefile)
    wd = abcs.Path(".")
    database = _get_database(makefile, **kwargs)
    original = open(makefile, 'r').readlines()
    variables_start = database.index(vvv)
    variables_end = database.index("", variables_start + 2)
    vars = database[variables_start:variables_end]
    database = database[variables_end:]
    implicit_rule_start = database.index("# Implicit Rules")
    file_rule_start = database.index("# Files")
    file_rule_end = database.index(fff)
    for i,line in enumerate(database[implicit_rule_start:]):
        if 'implicit rules, ' in line and line.endswith(' terminal.'):
            implicit_rule_end = implicit_rule_start+i
            break
    else:
        LOGGER.critical('cannot find `implicit_rule_end`!')
        implicit_rule_end=implicit_rule_start
    implicit_targets_section = database[implicit_rule_start:implicit_rule_end]
    file_targets_section = database[file_rule_start:file_rule_end]
    file_target_names = list(filter(_test, file_targets_section))
    implicit_target_names = list(filter(_test, implicit_targets_section))
    targets = file_target_names + implicit_target_names
    out = {}
    for tline in targets:
        bits=tline.split(":")
        target_name=bits.pop(0)
        childs = ':'.join(bits)
        # try:
        #     target_name, childs = 
        # except (ValueError,) as exc:
        #      import IPython; IPython.embed()
        type = "implicit" if tline in implicit_targets_section else "file"
        # NB: line nos are from reformatted output, not original file
        line_start = database.index(tline)
        line_end = database.index("", line_start)
        body = database[line_start:line_end]
        pline = _get_prov_line(body)
        file = _get_file(body=body,makefile=makefile)
        if pline:
            lineno = pline.split("', line ")[-1].split("):")[0]
        else:
            try:
                lineno = original.index(tline)
            except ValueError:
                LOGGER.critical(f'cant find {tline} in {file}, parametric?')
                target_name
                lineno = None
        lineno = lineno and int(lineno)
        prereqs = [x for x in childs.split() if x.strip()]
        out[target_name] = dict(
            file=file,
            lineno=lineno,
            body=body,
            type=type,
            docs=[x[len("\t@#") :] for x in body if x.startswith("\t@#")],
            prereqs=prereqs,
        )
        if type=='implicit':
            regex=target_name.replace('%', '.*')
            out[target_name].update(regex=regex)
            # out[target_name].update(implementors=[
            #     t for t in
            # ])
    #         out
    # implicit_targets = dict([k,v] for k,v in out.items() )
    for target_name, tmeta in out.items():
        if 'regex' in tmeta:
            implementors=[]
            for impl in out:
                if impl!=target_name and re.compile(tmeta['regex']).match(impl):
                    implementors.append(impl)
            tmeta['implementors']=implementors

    for target_name, tmeta in out.items():
        real_body = [b for b in tmeta['body'][1:] if not b.startswith('#') and not b.startswith('@#')]
        if not real_body:
            LOGGER.critical(f'missing body for: {target_name}')
            for chain in out:
                if target_name in out[chain].get('implementors', []):
                    tmeta['chain'] = chain
            if len(tmeta['prereqs'])==1:
                tmeta['chain'] = tmeta['prereqs'][0]

    if not bodies:
        tmp = {}
        for k,v in out.items():
            v.pop('body',[])
            tmp[k]=v
        out=tmp
    return out
parser=parse
