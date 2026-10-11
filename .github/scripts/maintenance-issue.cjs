const fs = require('node:fs');

module.exports = async ({ github, context, diagnostic = false }) => {
  const title = diagnostic ? 'Maintenance issue self-test (pilot)' : 'Weekly Microsoft Copilot source review required';
  const { owner, repo } = context.repo;
  const issues = await github.paginate(github.rest.issues.listForRepo, {
    owner, repo, state: 'open', per_page: 100,
  });
  const existing = issues.find(i => !i.pull_request && i.title === title);
  const read = path => fs.existsSync(path) ? fs.readFileSync(path, 'utf8') : 'Report unavailable.';
  const body = [
    diagnostic
      ? 'Diagnostic self-test: verifies issue write permission and reuse. No source defect or expired verification date is asserted by this test.'
      : 'The source maintenance checks require review.',
    '',
    `Run: https://github.com/${owner}/${repo}/actions/runs/${context.runId}`,
    `Commit: ${context.sha}`,
    '',
    '## Freshness (verification age)',
    '```text', read('freshness.txt').trim(), '```',
    '',
    '## HTTP access (not content verification)',
    '```text', read('reachability.txt').trim(), '```',
    '',
    'HTTP 403 means the client was denied access; it does not prove the source is obsolete. '
      + 'Read the official page in a supported browser before changing verification dates. '
      + 'Keep critical freshness and access failures visible until reviewed.',
  ].join('\n');
  if (existing) {
    const result = await github.rest.issues.update({ owner, repo, issue_number: existing.number, body });
    return { action: 'updated', number: result.data.number };
  }
  const result = await github.rest.issues.create({ owner, repo, title, body });
  return { action: 'created', number: result.data.number };
};
