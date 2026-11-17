import os, re, sys
root = sys.argv[1]
texs = []
for d, _, fs in os.walk(root):
    for f in fs:
        if f.endswith('.tex'): texs.append(os.path.join(d, f))
main = [t for t in texs if '\\documentclass' in open(t, errors='ignore').read()]
def expand(path, depth=0):
    s = open(path, errors='ignore').read()
    s = re.sub(r'(?<!\\)%.*', '', s)
    def rep(m):
        name = m.group(2)
        for cand in [name, name + '.tex']:
            p = os.path.join(root, cand)
            if os.path.isfile(p) and depth < 5: return expand(p, depth + 1)
        return ''
    return re.sub(r'\\(input|include)\{([^}]*)\}', rep, s)
for m in main:
    s = expand(m)
    figs = re.findall(r'\\begin\{(figure\*?|teaserfigure)\}(.*?)\\end\{\1\}', s, re.S)
    # also catch teaser in \twocolumn[...] or before \begin{abstract}
    pre = s.split('\\begin{abstract}')[0] if '\\begin{abstract}' in s else ''
    pre_imgs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', pre)
    print('MAIN', os.path.relpath(m, root), '| pre-abstract imgs:', pre_imgs)
    for i, (_, body) in enumerate(figs[:3]):
        imgs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', body)
        cap = re.search(r'\\caption\{(.{0,160})', body, re.S)
        print(f'  FIG{i+1}', imgs, '|', ' '.join(cap.group(1).split()) if cap else '')
