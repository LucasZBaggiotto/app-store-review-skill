---
name: app-store-review
description: Audit an app, its metadata, or a feature plan against the Apple App Store Review Guidelines before submitting to App Review, and diagnose or appeal a rejection. Use whenever working on an iOS/iPadOS/macOS/watchOS/tvOS/visionOS app that will ship on the App Store — adding in-app purchase or a paywall, subscriptions, external payment links, accounts/login, sign-in with a social provider, account deletion, user-generated content, kids/children features, health or HealthKit data, location, ATT/tracking, ads, push notifications, VPN, MDM, crypto, gambling, AI/chatbot or mini-app content, permissions and purpose strings, privacy policy or privacy nutrition labels, screenshots, app name/subtitle/keywords/description, age rating, TestFlight betas, or the "Notes for Review" — and whenever the user mentions App Review, a rejection, Guideline 2.1 / 3.1.1 / 4.3 / 5.1.1 (or any numbered guideline), Metadata Rejected, expedited review, or an appeal.
---

# App Store Review

Get an app through App Review on the first try, and unblock it fast when it isn't.

Source: <https://developer.apple.com/app-store/review/guidelines/> — last synced **2026-06-08**.
Sections: **1. Safety · 2. Performance · 3. Business · 4. Design · 5. Legal**.

## How to use this skill

1. **Identify the mode** — one of:
   - **Pre-submission audit** → run the [Audit workflow](#audit-workflow) below.
   - **Feature check** ("can we do X?") → jump straight to the relevant reference file, answer with the guideline number, then state the compliant alternative.
   - **Rejection triage** → open `references/rejection-playbook.md`, match the guideline number Apple cited, apply the fix, then draft the Resolution Center reply.
2. **Read only the reference you need.** Each file is self-contained.
3. **Always cite the rule number** (e.g. "3.1.1 requires IAP here") — it is how Apple communicates and how the user will argue back.
4. **Never assert compliance you did not verify.** If you did not open the file, the plist, or the App Store Connect field, say it is unverified.

## Reference map

| File | Covers | Reach for it when |
|---|---|---|
| `references/01-safety.md` | Objectionable content, UGC moderation, Kids Category, physical harm, medical, developer contact, data security | The app has user content, a social layer, kids, health/medical, or anything harm-adjacent |
| `references/02-performance.md` | App completeness, demo accounts, TestFlight, **all metadata rules**, hardware, software/API rules, background modes, ads | Any submission — this is where most first-time rejections land |
| `references/03-business.md` | IAP, subscriptions, external purchase links, reader apps, physical goods, crypto, loans, ad models | The app takes money in any form |
| `references/04-design.md` | Copycats, minimum functionality, spam, extensions, Apple services, mini apps/chatbots/emulators, Sign in with Apple, Apple Pay | Thin apps, template apps, web wrappers, extensions, third-party login, AI/mini-app content |
| `references/05-legal-privacy.md` | Privacy policy, consent, data minimization, account deletion, ATT, health, kids' privacy, location, IP, gambling, VPN, MDM, Code of Conduct | Anything touching user data — which is nearly everything |
| `references/rejection-playbook.md` | The ~15 rejections that actually happen, with fixes and reply templates | You have a rejection in hand |
| `references/submission-checklist.md` | Copy-paste pre-flight checklist | Right before hitting Submit for Review |

`scripts/fetch_guidelines.py` re-downloads the live guidelines to `references/_cache/guidelines.txt` when you need the exact current wording or want to check whether a rule changed since the sync date.

## Audit workflow

Run these in order. Report findings as a table: **Guideline · Severity (Blocker / Likely rejection / Risk) · Evidence (file:line or ASC field) · Fix.**

### 1. Map the app's surface area
Determine which high-risk areas are in play, because they decide which references to read:

```
grep -rin "StoreKit\|SKProduct\|Purchases\.\|RevenueCat\|Superwall\|Adapty" --include=*.swift .   # → 03-business
grep -rin "ATTrackingManager\|AppTrackingTransparency\|IDFA\|AdSupport"     --include=*.swift .   # → 05-legal 5.1.2
grep -rin "HealthKit\|HKHealthStore\|CMMotion\|ClassKit\|HomeKit"           --include=*.swift .   # → 05-legal 5.1.3
grep -rin "ASAuthorizationAppleID\|GIDSignIn\|FBSDK\|LoginManager"          --include=*.swift .   # → 04-design 4.8
grep -rin "SFSafariViewController\|WKWebView\|openURL" --include=*.swift .                        # → 3.1.1(a), 4.2, 5.1.1(vii)
grep -rin "UNUserNotificationCenter\|CLLocationManager\|AVCaptureDevice"    --include=*.swift .   # → purpose strings
```

### 2. Info.plist purpose strings (5.1.1(ii), 5.1.5)
Every `NS*UsageDescription` must say *specifically* what the data is used for and why the user benefits. Generic strings ("We need your location") are a standing rejection.

```
plutil -p **/Info.plist | grep -i "UsageDescription" -A1
```
Also check: is any permission requested that the core feature does not need (5.1.1(iii) data minimization)? Does the app degrade gracefully when the user says No (5.1.1(iv))?

### 3. Accounts (5.1.1(v), 4.8)
- Login required to use the app at all? Only allowed if account-based features are genuinely core.
- Account creation offered? **In-app account deletion is mandatory** — not "email us". This is one of the most common rejections.
- Third-party/social login used for the *primary* account? Then Sign in with Apple (or an equivalent privacy-preserving option) must be offered too, unless an exemption in 4.8 applies.

### 4. Money (3.1)
Walk the decision tree in `references/03-business.md`. The core split: **digital content/features consumed in the app → IAP, mandatory.** Physical goods/services consumed outside the app → must *not* use IAP. Then check subscription disclosure (3.1.2(c)) and any external link against 3.1.1(a) / 3.1.3.

### 5. Privacy artifacts (5.1.1(i))
- Privacy policy URL set in App Store Connect **and** reachable from inside the app.
- Policy states: what is collected, how, every use, third-party recipients, retention/deletion, how to revoke consent.
- Privacy nutrition labels in ASC match what the code actually collects (including every SDK).
- Third-party SDKs: you are responsible for them. Check each one's data collection and its Privacy Manifest.

### 6. Metadata (2.3)
Name ≤30 chars · subtitle accurate, no competitor references, no unverifiable claims · screenshots show the app *in use* (not splash/login) · previews are real screen captures · all metadata 4+ appropriate · category correct · age rating honest · keywords free of trademarks and competitor names · "What's New" describes real changes.

### 7. Completeness (2.1) — the single largest rejection bucket
No crashes, no placeholder text, no dead links, backend live during review, **demo account or full demo mode provided**, all IAPs visible and functional to the reviewer, non-obvious features explained in the Notes for Review.

### 8. Substance (4.2, 4.3)
Is it more than a wrapped website? Does it offer lasting utility? Is it distinguishable from what already exists? Is it a template/generator output submitted by someone other than the content owner (4.2.6)?

## Decision rules worth memorizing

- **Anything unlocking digital content or functionality inside the app → in-app purchase.** License keys, QR codes, crypto, external checkout: all rejected under 3.1.1.
- **Physical goods or real-world services → must NOT use IAP.** Using IAP there is also a rejection.
- **Account creation ⇒ in-app account deletion.** No exceptions worth arguing.
- **UGC ⇒ four mandatory controls**: content filter, report mechanism, block users, published contact info (1.2).
- **Tracking across apps/sites ⇒ ATT prompt**, and the app must work if the user declines (5.1.2(i)).
- **Never gate functionality on granting a permission, enabling notifications, rating the app, or downloading another app** (5.1.2(i), 3.2.2(x)).
- **Public APIs only, current shipping OS, no downloading executable code** (2.5.1, 2.5.2).
- **Hidden or undisclosed features are a Developer Program termination risk**, not a rejection (2.3.1).
- **Kids Category ⇒ no third-party analytics or ads** (with narrow exceptions), parental gate for any link out or purchase (1.3).
- **The "for entertainment purposes only" disclaimer does not rescue anything** (1.1.6).

## Writing the Notes for Review

A good note prevents rejections. Include, in this order:

1. Demo account credentials (username/password) — or how to enter demo mode.
2. What the app does in two sentences, and how it makes money.
3. Step-by-step repro for any non-obvious feature, and where to find each IAP.
4. Regulatory/licensing documentation links, if the app is in a regulated field (5.1.1(ix)).
5. Anything a reviewer might mistake for a violation, pre-explained with the guideline number.

Generic notes ("Bug fixes") on a release with new features are themselves a 2.3.1 rejection.

## Responding to a rejection

1. Read the exact guideline number and the reviewer's screenshot/text — do not guess.
2. Decide: **fix** (most cases), **clarify** (the reviewer misread the app), or **appeal** (the guideline does not apply).
3. Reply in Resolution Center: acknowledge, state precisely what changed or why the guideline does not apply, give reproduction steps. Stay factual and respectful — 5.6 makes tone an actual compliance matter.
4. If it is a metadata-only issue, you can often fix it in App Store Connect without a new binary.
5. Bug-fix updates to already-live apps are not blocked over non-legal, non-safety guideline issues — you may ask to defer the fix to the next submission.
6. Appeals go through the App Review Board form; expedited review exists but is spent credibility — use it for real emergencies.

Templates are in `references/rejection-playbook.md`.
