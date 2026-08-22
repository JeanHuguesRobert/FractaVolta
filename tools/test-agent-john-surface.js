#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "docs");
const read = (rel) => fs.readFileSync(path.join(root, rel), "utf8");

const en = read("john.md");
const fr = read("fr/john.md");
assert.match(en, /an agent/i);
assert.match(fr, /un agent/i);
assert.match(en, /not sovereign/i);
assert.match(fr, /pas souverain/i);
assert.match(en, /C\.O\.R\.S\.I\.C\.A/);
assert.match(fr, /C\.O\.R\.S\.I\.C\.A/);
assert.match(en, /agent_page: true/);
assert.match(fr, /agent_page: true/);

const include = read("_includes/agent-john.html");
assert.match(include, /Jumeau public|Public twin/);
assert.match(include, /data-john-consent-processing/);
assert.match(include, /data-john-expand/);
assert.match(include, /data-john-consent-memory/);
assert.match(include, /oleole\.acorsica\.org/);
assert.match(include, /cogentia\.fractavolta\.com\/guide\/chat/);

const js = read("assets/agent-john.js");
assert.match(js, /fractavolta\.agent-john\.v1/);
assert.match(js, /surface: "agent-john"/);
assert.match(js, /localStorage/);
assert.match(js, /agent-john-immersive/);
assert.match(js, /requestFullscreen/);
assert.match(js, /threadCompact/);
assert.match(js, /recentKeep/);
assert.match(js, /agent-john-compact/);
assert.match(js, /generatedCompact/);
assert.match(js, /historyWireLimit/);
assert.match(include, /data-john-memory/);

const legalEn = read("legal/agent-john.md");
const legalFr = read("fr/legal/agent-john.md");
assert.match(legalEn, /GDPR|personal data/i);
assert.match(legalFr, /RGPD/);
assert.match(legalEn, /browser only/i);
assert.match(legalFr, /navigateur/);

const layout = read("_layouts/default.html");
assert.match(layout, /agent-john\.js/);
assert.match(layout, /page\.agent_page/);

console.log(JSON.stringify({ ok: true, checks: ["copy", "consent", "storage", "legal", "layout"] }));
