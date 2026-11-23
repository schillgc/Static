"""Static project archive document and asset contracts."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.rglob("*.html"))


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.title_depth = 0
        self.title = []
        self.images = []
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        elif tag == "title":
            self.title_depth += 1
        elif tag == "img":
            self.images.append(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.references.append(value)

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth:
            self.title.append(data)


class StaticArchiveTests(unittest.TestCase):
    def test_html_documents_have_language_and_title(self):
        self.assertEqual(len(HTML_FILES), 8, "Update this count when adding/removing an archive page")
        failures = []
        for page in HTML_FILES:
            parser = PageParser()
            parser.feed(page.read_text(encoding="utf-8", errors="replace"))
            relative = page.relative_to(ROOT)
            if not parser.language:
                failures.append(f"{relative}: missing html lang")
            if not "".join(parser.title).strip():
                failures.append(f"{relative}: missing title")
        self.assertEqual(failures, [])

    def test_images_have_nonempty_alt_text(self):
        failures = []
        for page in HTML_FILES:
            parser = PageParser()
            parser.feed(page.read_text(encoding="utf-8", errors="replace"))
            for image in parser.images:
                if not image.get("alt", "").strip():
                    failures.append(
                        f"{page.relative_to(ROOT)}: image has no alt text ({image.get('src', 'no src')})"
                    )
        self.assertEqual(failures, [])

    def test_stable_projects_have_resolvable_relative_assets(self):
        failures = []
        for page in HTML_FILES:
            relative_page = page.relative_to(ROOT)
            # This older personal-photo exercise references media that is not in
            # the repository tree. Its source/rights recovery is tracked separately.
            if relative_page == LEGACY_MEDIA_EXCEPTION:
                continue
            parser = PageParser()
            parser.feed(page.read_text(encoding="utf-8", errors="replace"))
            for reference in parser.references:
                parsed = urlsplit(reference)
                if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
                    continue
                target = (page.parent / unquote(parsed.path)).resolve()
                if not target.exists():
                    failures.append(f"{relative_page} -> {reference}")
        self.assertEqual(failures, [], f"Missing local assets: {failures}")

    def test_generated_macos_metadata_is_not_tracked(self):
        leftovers = [
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob(".DS_Store")
            if path.is_file()
        ]
        self.assertEqual(leftovers, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)

class ArchivedPersonalMediaTests(unittest.TestCase):
    def test_personal_photo_exercise_is_text_only_and_not_indexed(self):
        page = ROOT / "HTML 5 & CSS 3/Bootstrap 4/Elena Sarah Mattia (aka Lori)/Lori_Mattia.html"
        html = page.read_text(encoding="utf-8").lower()
        self.assertIn('name="robots" content="noindex, nofollow"', html)
        self.assertIn("no personal photographs", html)
        self.assertIn("explicit consent", html)
        self.assertNotIn("<img", html)
        self.assertNotIn("static\\\\images", html)
        self.assertNotIn("static\\\\css", html)
