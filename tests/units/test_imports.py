import json
input = dict(
    foo=dict(
        bar='bar',
        baz=dict(
            boom='bonk',
            list=['a','b','c'])))

def traverse(dct, visitor=None):
    import pydash
    paths = []
    def travel(obj=dct, path='', paths=[]):
        if isinstance(obj, (list, tuple)):
            for i,item in enumerate(obj):
                path_key = f"{path}.{i}"
                paths += [path_key]
                travel(item, path=path_key)
        if isinstance(obj, (dict,)):
            for k,v in obj.items():
                path_key = f"{path}.{k}"
                paths += [path_key]
                travel(v, path=path_key)
        paths = sorted(list(set(paths)))
        return paths
    paths=travel()
    result = dict(paths=paths, visited={})
    if visitor is not None:
        for path in paths:
            result['visited'][path] = visitor(path=path,value=pydash.get(dct,path))
    return result

def visit(value=None, path=None):
    print(f"[{path}: {value}]")
    return value

def test_walker():
    walker = traverse(input, visitor=visit)
    paths = walker['paths']
    assert paths==['.foo', '.foo.bar', '.foo.baz', '.foo.baz.boom', '.foo.baz.list', '.foo.baz.list.0', '.foo.baz.list.1', '.foo.baz.list.2']
    print(json.dumps(walker['visited'],indent=2))
    # tmp = dict([[p,pydash.get(input,p)] for p in paths])
    # print(tmp)
    # import IPython; IPython.embed()

if __name__=='__main__':
    test_walker()

# def test_imports():
#     from pynchon import __version__  # noqa: F401
