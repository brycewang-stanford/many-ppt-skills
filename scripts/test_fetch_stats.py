"""Regression coverage for failed fetches across checkpoint writes."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import fetch_stats


class FetchStatsTests(unittest.TestCase):
    def test_failed_repo_preserves_prior_stats_after_checkpoint(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills = root / 'skills.json'
            stats = root / 'stats.json'
            repos = ['owner/missing'] + [f'owner/repo{i}' for i in range(20)]
            skills.write_text(json.dumps({'skills': [{'repo': r} for r in repos]}))
            stats.write_text(json.dumps({'repos': {'owner/missing': {'stars': 7}}}))
            def fetch(repo):
                return None if repo == 'owner/missing' else {'stars': 1}
            with patch.multiple(fetch_stats, ROOT=root, SKILLS=skills, STATS=stats), \
                 patch.object(fetch_stats, 'fetch', side_effect=fetch), \
                 patch('sys.argv', ['fetch_stats.py']), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(fetch_stats.main(), 0)
            result = json.loads(stats.read_text())
            self.assertEqual(result['repos']['owner/missing'], {'stars': 7, 'stale': True})
            self.assertEqual(result['failed'], ['owner/missing'])
            self.assertEqual(len(result['repos']), 21)


if __name__ == '__main__':
    unittest.main()
