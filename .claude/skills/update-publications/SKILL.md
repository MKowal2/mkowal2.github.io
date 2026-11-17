---
name: update-publications
description: Update the website's Research/publications list with Matthew's newest papers from Google Scholar/arXiv, including a teaser figure cropped from each paper. Use when the user says "update webpage publications", "add my new papers", or similar.
---

# Update webpage publications

Goal: find papers that aren't on the site yet, **ask the user which ones to add** (only the bangers,
never add everything), then add each one to `_data/projects.yml` with a teaser image cropped from the paper.

## Where things live
- Paper list: `_data/projects.yml` (rendered by `_layouts/home.html` → `_includes/research-card.html`).
  The `_publications/` folder is legacy and unused, so don't touch it.
- Images: `/images/<short_snake_name>.(png|jpg)`.
- Cards show the image at **280×180 with `object-fit: cover`**, so teasers should be 14:9.
- Badge classes (`_sass/_variables.scss`): `icml cvpr iccv iclr bmvc tpami ijcv caic preprint`.
  For a venue without a class (e.g. KDD, NeurIPS), add a `$badge-x` color + `&--x` rule in `_sass/_research.scss`.
- Helper scripts: `.claude/skills/update-publications/scripts/`. In the same dir: `declined.txt`
  (papers the user said no to) and `wanted.txt` (papers the user wants once they reach arXiv).
  If the user says "add X when it's out", put X in `wanted.txt`.

## Steps

### 1. Find candidates
- Run `python3 .claude/skills/update-publications/scripts/new_papers.py .`
  It queries arXiv by **full name** (`au:"Matthew Kowal"`; `au:Kowal_M` returns a nuclear physicist)
  and prints `NEW` / `WANTED` / `ON SITE` / `DECLINED` for each paper, with author position.
- `WANTED` = the user already asked for this paper (listed in `wanted.txt`). Add it **without asking**,
  then delete its line from `wanted.txt`. Also check `wanted.txt` against Scholar: if an item has a
  real venue page or PDF there but still no arXiv version, mention it to the user.
- Cross-check Google Scholar with WebFetch on
  `https://scholar.google.com/citations?user=FCg8QxUAAAAJ&hl=en&sortby=pubdate&pagesize=100`
  to get citation counts, venues (e.g. a preprint now listed as ICML/ICLR), and non-arXiv items (workshops).
  WebFetch summaries can be lossy, so trust arXiv for IDs and titles.
- **Venue upgrades:** if an `ON SITE` paper with `venue: "Preprint"` now has a venue on Scholar or a
  `journal_ref`, update its `venue`/`venue_class` too (e.g. Interpreting Physics → ICML 2026).

### 2. Ask the user which papers to add (required)
Use AskUserQuestion with `multiSelect: true`, grouping NEW papers by theme (≤4 options per question,
≤4 questions). Put author position, citation count, and month in each option's description.
Skip patents, theses, and `DECLINED` items. Append the papers the user doesn't pick to `declined.txt`
with a dated header so they aren't re-proposed next time.

### 3. Get the teaser figure (per paper)
Work in a fresh temp dir per paper (e.g. `/tmp/pubdl/src_<id>/`). Run scripts from the scripts dir,
not from inside downloaded sources. Don't use `python3 -I`: it hides the user-site PIL.
```
curl -sL -A "Mozilla/5.0" https://arxiv.org/e-print/<id> -o /tmp/pubdl/src_<id>.bin
mkdir -p /tmp/pubdl/src_<id> && tar xzf /tmp/pubdl/src_<id>.bin -C /tmp/pubdl/src_<id>
python3 scripts/find_figures.py /tmp/pubdl/src_<id>      # lists Fig 1-3 files + captions
pdftoppm -png -r 220 -singlefile <fig.pdf> /tmp/pubdl/raw/<id>   # PDF figs; copy PNG/JPG figs as-is
python3 scripts/make_teaser.py --preview <raw> /tmp/pubdl/prev/<id>.png   # then Read it
python3 scripts/make_teaser.py <raw> x0 y0 x1 y1 images/<name>.png   # fractions of width/height
python3 scripts/make_teaser.py --sheet /tmp/pubdl/sheet.png images/<new files...>   # Read to review
```
Choosing and cropping:
- Default to **Figure 1** (the teaser). If it's text-heavy (chat transcripts) or a very thin strip,
  use another figure that reads at 280px: a plot, a qualitative grid, or a 3D manifold.
  Past examples: the conspiracy paper used Fig 2a, and Shaping & Monitoring used its qualitative waterbird figure.
- Crop to the visually striking part (e.g. 1–2 panels of a wide multi-panel figure) and aim close to 14:9
  so there's little padding. Make sure labels and legends aren't clipped and no sliver of a neighboring panel
  sneaks in. On dark or photo backgrounds, avoid padding: crop to exactly 14:9.
- Use `.jpg` for photo-heavy crops (PNG > ~600 KB), `.png` for diagrams and plots.
- **Always look at the contact sheet** before moving on, and re-crop anything that looks off.

### 4. Add entries to `_data/projects.yml`
Keep the list **newest-first by arXiv submission date** (insert accepted-venue papers by date too).
```yaml
- title: "Exact Paper Title in Title Case"
  description: "One sentence, ~15-25 words, usually starting with 'We ...', stating the main finding."
  image: "/images/<name>.png"
  venue: "Preprint"          # or "ICML 2026", "CVPR 2024", ...
  venue_class: "preprint"    # matches a badge class
  # note: "Spotlight"        # optional (Oral/Spotlight)
  year: 2026
  links:
    - label: "Paper"
      url: "https://arxiv.org/abs/<id>"
    - label: "Code"          # only if public: check curl -o /dev/null -w '%{http_code}' == 200
      url: "https://github.com/..."
```
- Find Code/Project/Demo/Data links by grepping the LaTeX: `grep -rhoE 'https?://[^}{ ]*(github\.com|github\.io|huggingface\.co)[^}{ ]*' src_<id> --include='*.tex'`.
  Goodfire papers usually have a `github.com/goodfire-ai/<repo>` link on the title page.
  Skip links to private-looking `*.pages.github.io` dashboards.

### 5. Validate
- `ruby -ryaml -e 'd=YAML.load_file("_data/projects.yml"); d.each{|x| abort x["title"] unless File.exist?("."+x["image"])}; puts d.size'`
- Local `bundle exec jekyll build` currently fails (system Bundler too old for Gemfile.lock),
  so don't spend time on it. GitHub Pages builds on push.

### 6. Commit
One commit for the batch (e.g. "Add N new papers: …"). **Ask before pushing**, because pushing to
`master` publishes the site. Then summarize the papers added, which figure each teaser came from,
and any venue upgrades.
