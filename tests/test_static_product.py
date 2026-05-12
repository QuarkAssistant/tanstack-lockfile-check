import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TanStackStaticProductTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_required_disclosure_and_tip_jar_are_present(self):
        required = "Built by Quark Assistant — autonomous AI agent. Code authored by AI under owner supervision."
        self.assertIn(required, self.index)
        self.assertIn(required, self.readme)
        self.assertIn("https://ko-fi.com/quarkassistant", self.index)
        self.assertIn("https://ko-fi.com/quarkassistant", self.readme)

    def test_social_metadata_supports_public_pages_distribution(self):
        expected = [
            '<link rel="canonical" href="https://quarkassistant.github.io/tanstack-lockfile-check/" />',
            '<meta property="og:title" content="TanStack Lockfile Check" />',
            '<meta property="og:url" content="https://quarkassistant.github.io/tanstack-lockfile-check/" />',
            '<meta property="og:type" content="website" />',
            '<meta name="twitter:card" content="summary" />',
        ]
        for snippet in expected:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_response_pack_can_be_copied_and_downloaded_after_scan(self):
        for snippet in [
            'id="triagePack"',
            'id="copyReportBtn"',
            'id="downloadReportBtn"',
            'Copy triage report',
            'Download report .txt',
            'Copy detected package-manager commands',
            'id="pmCommands"',
            'id="pmLabel"',
            'id="commandsText"',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)
        for snippet in [
            'function buildReport(arr, bad, warn, pm)',
            'function detectPackageManager(text)',
            "packageManager:'pnpm@10.0.0'",
            'PM_COMMANDS = {',
            "Detected package manager: ${pm}",
            "pnpm list '@tanstack/*' tanstack --depth 20",
            'function downloadReport()',
            "new Blob([lastReport + '\\n'], {type:'text/plain'})",
            "a.download = 'tanstack-lockfile-triage-report.txt'",
            "document.getElementById('downloadReportBtn').addEventListener('click', downloadReport)",
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_prevention_policy_pack_generates_manager_specific_snippets(self):
        for snippet in [
            'id="preventionPack"',
            'Supply-chain prevention pack',
            'id="ageSelect"',
            'id="copyPolicyBtn"',
            'function buildPolicyPack(pm)',
            'function selectedAgePolicy()',
            'const POLICY_TEMPLATES = {',
            'minimumReleaseAge: ${minutes}',
            'npmMinimalAgeGate: "${days}d"',
            'minimumReleaseAge = ${seconds}',
            'min-release-age=${days}',
            'trustedDependencies',
            'blockExoticSubdeps: true',
            'Update prevention pack',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_github_actions_cache_poisoning_guard_is_local_and_copyable(self):
        for snippet in [
            'id="workflowGuard"',
            'GitHub Actions cache-poisoning guard',
            'id="workflowInput"',
            'Scan workflow YAML',
            'Load risky workflow sample',
            'Copy workflow guard report',
            'id="workflowReport"',
            'pasted lockfile and workflow YAML stay in local browser memory',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)
        for snippet in [
            'function analyzeWorkflowYaml(text)',
            'function buildWorkflowGuardReport(text)',
            'function scanWorkflow()',
            'function loadWorkflowSample()',
            'pull_request_target',
            'actions/cache/save',
            'Writable token on untrusted trigger',
            'Trusted-publishing token on untrusted path',
            'github.event.* strings as attacker-controlled input',
            "document.getElementById('copyWorkflowReportBtn').addEventListener('click'",
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)
        self.assertIn('GitHub Actions cache-poisoning guard', self.readme)

    def test_detection_data_and_privacy_claim_are_embedded(self):
        self.assertIn('"@tanstack/react-router": {bad:["1.169.5","1.169.8"], patched:"1.169.9"}', self.index)
        self.assertIn('"tanstack": {bad:["2.0.4","2.0.5","2.0.6","2.0.7"]', self.index)
        self.assertIn("no external JavaScript", self.index)
        external_scripts = re.findall(r'<script[^>]+src=', self.index, flags=re.I)
        self.assertEqual([], external_scripts)

    def test_robots_and_sitemap_exist_for_live_url(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("Sitemap: https://quarkassistant.github.io/tanstack-lockfile-check/sitemap.xml", robots)
        self.assertIn("https://quarkassistant.github.io/tanstack-lockfile-check/", sitemap)
        self.assertIn("<changefreq>daily</changefreq>", sitemap)


if __name__ == "__main__":
    unittest.main()
