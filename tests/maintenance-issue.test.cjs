const assert = require('node:assert/strict');
const test = require('node:test');
const maintain = require('../.github/scripts/maintenance-issue.cjs');
const title = 'Weekly Microsoft Copilot source review required';
const context = { repo: { owner: 'test', repo: 'test' }, runId: 123, sha: 'prepared-sha' };

function mock(rows) {
  const calls = [];
  const github = {
    paginate: async (method, params) => { calls.push(['paginate', params]); return rows; },
    rest: { issues: {
      listForRepo: () => {},
      create: async params => { calls.push(['create', params]); return { data: { number: 101 } }; },
      update: async params => { calls.push(['update', params]); return { data: { number: params.issue_number } }; },
    } },
  };
  return { github, calls };
}

test('creates one maintenance issue when absent', async () => {
  const m = mock([]);
  assert.deepEqual(await maintain({ github: m.github, context }), { action: 'created', number: 101 });
  const params = m.calls.find(c => c[0] === 'create')[1];
  assert.match(params.body, /HTTP 403/);
  assert.match(params.body, /prepared-sha/);
  assert.equal(m.calls.filter(c => c[0] === 'create').length, 1);
});

test('reuses an issue beyond the first page and excludes pull requests', async () => {
  const rows = [{ title, number: 1, pull_request: {} }, ...Array.from({length: 105}, (_, i) => ({title: `other ${i}`, number: i + 2})), {title, number: 200}];
  const m = mock(rows);
  assert.deepEqual(await maintain({ github: m.github, context }), { action: 'updated', number: 200 });
  assert.equal(m.calls.some(c => c[0] === 'create'), false);
  assert.equal(m.calls.find(c => c[0] === 'update')[1].issue_number, 200);
});

test('repeated reviews update the same issue rather than creating duplicates', async () => {
  const rows = [];
  const m = mock(rows);
  await maintain({ github: m.github, context });
  rows.push({title, number: 101});
  await maintain({ github: m.github, context });
  assert.equal(m.calls.filter(c => c[0] === 'create').length, 1);
  assert.equal(m.calls.filter(c => c[0] === 'update').length, 1);
});
