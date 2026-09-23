"""Validate generated pages, cross-page anchors, images and navigation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote, urljoin

root = Path('public')
expected = ('/', '/features/', '/deployment/', '/about/', '/support/', '/privacy/', '/terms/')

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = set(), []
        self.h1 = 0
        self.stores = 0
        self.dashboard = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs['id'])
        self.h1 += tag == 'h1'
        for key in ('src', 'href'):
            if key in attrs:
                self.refs.append(attrs[key])
        if tag == 'img':
            assert 'alt' in attrs, 'Image missing alternative text'
        if tag == 'a' and 'store-button' in attrs.get('class', '').split():
            assert attrs.get('href') == '#', 'Store link must remain a placeholder'
            assert 'not yet available' in attrs.get('aria-label', '').lower()
            self.stores += 1
        if tag == 'a' and attrs.get('href') == 'https://shado-host.golden-alpha.ts.net/login':
            self.dashboard += 1

pages = {}
for file in root.rglob('*.html'):
    page = Page()
    page.feed(file.read_text())
    assert page.h1 == 1, f'Expected one primary heading: {file}'
    pages[file] = page
for route in expected:
    file = root / route.lstrip('/') / 'index.html'
    assert file in pages, f'Missing required page: {route}'
    assert pages[file].stores >= 2, f'Missing store buttons: {route}'
    assert pages[file].dashboard >= 1, f'Missing dashboard link: {route}'
for file, page in pages.items():
    current_url = '/' + str(file.relative_to(root))
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        if not url.path:
            target = file
        else:
            target = root / unquote(urlsplit(urljoin(current_url, url.path)).path.lstrip('/'))
            if target.is_dir():
                target /= 'index.html'
        assert target.exists(), f'Missing local target in {file}: {ref}'
        if url.fragment:
            assert target in pages and url.fragment in pages[target].ids, f'Missing anchor in {file}: {ref}'
assert (root / 'CNAME').read_text().strip() == 'shado.rv.sa'
print(f'PASS: {len(pages)} pages; local assets, cross-page anchors, downloads, dashboard links, headings and image alt text')
