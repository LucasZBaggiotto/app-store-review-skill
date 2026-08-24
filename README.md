# App Store Review: a Coding agent skill

An agent skill that makes Claude actually useful for getting an app past **Apple's App Store Review**.

It distills the [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) into something an AI coding agent can *act* on: a concrete audit workflow that greps your codebase and your `Info.plist`, decision trees for the rules people get wrong, and a rejection playbook with reply templates for the Resolution Center.

Synced with Apple's guidelines as of **June 8, 2026**.

---

## Why

Most App Store rejections aren't exotic. They're the same dozen issues, over and over:

- The reviewer's demo account didn't work (**2.1**)
- Account creation without in-app account deletion (**5.1.1(v)**)
- A digital unlock that bypasses StoreKit (**3.1.1**)
- Social login without Sign in with Apple (**4.8**)
- A paywall that never states the renewal terms (**3.1.2(c)**)
- Screenshots of the login screen (**2.3.3**)
- Purpose strings that say "We need your location" (**5.1.1(ii)**)

An LLM has fuzzy, half-remembered versions of these rules and will confidently tell you the wrong thing. This skill gives it the actual text, organized by the question you're asking, plus the rule numbers to cite — because rule numbers are how Apple talks and how you argue back.

## What's in it

```
SKILL.md                              Entry point: audit workflow, decision rules,
                                      how to write Notes for Review, how to answer a rejection
references/
  01-safety.md                        UGC moderation, Kids Category, medical, physical harm
  02-performance.md                   Completeness, demo accounts, ALL metadata rules, APIs, ads
  03-business.md                      IAP decision tree, subscriptions, external links, crypto
  04-design.md                        Minimum functionality, spam, extensions, Sign in with Apple,
                                      mini apps / chatbots / emulators (4.7), Apple Pay
  05-legal-privacy.md                 Privacy policy, consent, ATT, account deletion, health,
                                      kids, IP, gambling, VPN, MDM, Code of Conduct
  rejection-playbook.md               The ~15 rejections that actually happen + reply templates
  submission-checklist.md             Copy-paste pre-flight checklist
scripts/
  fetch_guidelines.py                 Re-download Apple's live text to check for changes
```

Every reference file ends with its own audit checklist. Claude reads only the file it needs, so the skill stays cheap in context.

## Install

**Claude Code — global (available in every project):**

```bash
git clone https://github.com/LucasZBaggiotto/app-store-review-skill.git \
  ~/.claude/skills/app-store-review
```

**Claude Code — single project:**

```bash
git clone https://github.com/LucasZBaggiotto/app-store-review-skill.git \
  .claude/skills/app-store-review
```

Restart Claude Code (or start a new session). That's it — the skill loads on its own when the conversation touches App Review.

> Works anywhere skills are supported. For Claude.ai, zip the folder and upload it as a Skill in Settings → Capabilities.

## Use

The skill triggers automatically. You can also invoke it directly:

```
/app-store-review
```

Things worth asking it:

```
Audit this app against the App Store Review Guidelines before I submit.

We got rejected under Guideline 3.1.1. Here's what the reviewer wrote — what do we do?

Can we charge for this feature with Stripe instead of StoreKit?

Write the Notes for Review for this release.

Check my Info.plist purpose strings and my privacy nutrition labels against the code.

Does this paywall meet 3.1.2(c)?
```

It will answer with the guideline number, the evidence (`file:line` or the App Store Connect field), and the fix.

## Keeping it current

Apple revises the guidelines several times a year. To check whether anything moved since the sync date:

```bash
python3 scripts/fetch_guidelines.py
# → Apple's stated last update: June 8, 2026
```

That writes the current full text to `references/_cache/guidelines.txt` (git-ignored) so Claude can diff the exact wording. If Apple's date is newer than the one in `SKILL.md`, ask Claude to reconcile the reference files against the cache.

## Notes and limits

- **Not legal advice, and not affiliated with Apple.** The reference files are an independent summary written for agent use; Apple's page is always the authority. The full copyrighted text is deliberately *not* redistributed here — the fetch script pulls it on demand.
- **App Review is human.** These rules are applied with judgment, and reviewers occasionally disagree with each other. The playbook is built around that: clarify and appeal are first-class outcomes, not last resorts.
- **The audit is only as good as its evidence.** The skill is instructed never to claim compliance for something it didn't actually open and read.

## Contributing

Guidelines change, and rejection patterns change with them. Issues and PRs welcome — especially:

- new or reworded guidelines after an Apple update
- real rejection reasons that aren't in the playbook yet
- concrete grep/plist checks that catch a violation before submission

## License

[MIT](LICENSE) for the skill's own content. Apple's App Store Review Guidelines are © Apple Inc. and are neither included nor redistributed here.
