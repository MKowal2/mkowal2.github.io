"""List Matthew Kowal's arXiv papers and flag which are not yet in _data/projects.yml.

Usage: python3 new_papers.py <repo_root>
NOTE: query by full name. `au:Kowal_M` matches a nuclear physicist (M. Kowal) instead.
"""
import re, sys, urllib.request, os
root = sys.argv[1] if len(sys.argv) > 1 else '.'
url = ('https://export.arxiv.org/api/query?search_query=au:%22Matthew+Kowal%22'
       '&sortBy=submittedDate&sortOrder=descending&max_results=60')
xml = urllib.request.urlopen(url, timeout=60).read().decode()
site = open(os.path.join(root, '_data/projects.yml')).read()
norm = lambda t: re.sub(r'[^a-z0-9]', '', t.lower())
site_titles = {norm(t) for t in re.findall(r'title:\s*"(.*?)"', site)}
dpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'declined.txt')
declined = [l.split('#')[0].strip() for l in open(dpath) if l.split('#')[0].strip()] if os.path.exists(dpath) else []
wpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'wanted.txt')
wanted = [l.split('#')[0].strip() for l in open(wpath) if l.split('#')[0].strip()] if os.path.exists(wpath) else []
is_wanted = lambda aid, t: any(w == aid or norm(w) in norm(t) for w in wanted)
for e in xml.split('<entry>')[1:]:
    title = ' '.join(re.search(r'<title>(.*?)</title>', e, re.S).group(1).split()).replace('&amp;', '&')
    aid = re.search(r'<id>.*?abs/(.*?)(v\d+)?</id>', e).group(1)
    date = re.search(r'<published>(.*?)</published>', e).group(1)[:10]
    authors = re.findall(r'<name>(.*?)</name>', e)
    pos = next((i + 1 for i, a in enumerate(authors) if 'Kowal' in a), '?')
    jref = re.search(r'<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>', e, re.S)
    on_site = aid in site or norm(title) in site_titles
    status = 'ON SITE ' if on_site else 'WANTED  ' if is_wanted(aid, title) else 'DECLINED' if (aid in declined or norm(title) in map(norm, declined)) else 'NEW     '
    print(f"{status} {date} {aid:<11} author {pos}/{len(authors):<3} {title}"
          + (f"  [journal_ref: {' '.join(jref.group(1).split())}]" if jref else ''))
