"""Check the deployed artifact, internal navigation and local assets using stdlib."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path('public')
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.h1 = 0
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

page = Page()
page.feed((root / 'index.html').read_text())
assert page.h1 == 1, 'Expected one primary heading'
for ref in page.refs:
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        continue
    if url.fragment:
        assert url.fragment in page.ids, f'Missing anchor: {ref}'
    if url.path:
        target = root / unquote(url.path.lstrip('/'))
        assert target.exists(), f'Missing local asset: {ref}'
assert (root / 'CNAME').read_text().strip() == 'shado.rv.sa'
print(f'PASS: homepage, {len(page.ids)} IDs, {len(page.refs)} references, image alt text and custom domain')
