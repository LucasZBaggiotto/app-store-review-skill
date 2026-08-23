# Rejection Playbook

How to read a rejection, the fixes that actually work, and what to write back.

## First: classify the rejection

| Signal in App Store Connect | Meaning |
|---|---|
| **Rejected** | Binary problem. Needs a new build (usually). |
| **Metadata Rejected** | Fixable in App Store Connect without a new binary — name, screenshots, description, age rating, IAP metadata, review notes. |
| **Binary Rejected** with a guideline number | Read the number, then the reviewer's message, then the screenshot. Reviewers attach evidence; the screenshot often reveals they hit a different screen than you expected. |
| **Developer Code of Conduct** / 5.6 language | Serious. Account-level risk. Respond carefully and factually; consider an improvement plan. |

Then decide: **fix**, **clarify**, or **appeal**. Most rejections are fixes. Clarify when the reviewer misread the app (very common with demo accounts, region-gated features, and hardware dependencies). Appeal when the cited guideline genuinely does not apply.

---

## The rejections that actually happen

### 2.1 — App Completeness (the #1 cause)
**Usually means:** crash on the reviewer's device, a login they couldn't get past, a dead backend, an IAP that didn't load, or "we need more information".
**Fix:**
- Reproduce on a physical device with a **clean install** and a fresh account, on the current OS, over both Wi-Fi and cellular, and on an IPv6-only network.
- Verify the demo account still works *today* and isn't rate-limited, expired, or region-locked.
- Confirm the backend, feature flags, and remote config are live for the reviewer's region (often the US) — a feature flag off for their locale reads as a broken app.
- If Apple asked "we need more information", answer every question with specifics; don't restate marketing copy.

### 2.3.1 — Hidden or undisclosed features
**Usually means:** a feature reachable only under conditions Apple didn't see, a remote kill-switch, unshipped code paths, or review notes that said "bug fixes" on a feature release.
**Fix:** disclose everything in Notes for Review with steps to reach it, or remove the dormant code. This one escalates to account termination if it looks intentional — never argue it away, fix it.

### 2.3.3 / 2.3.8 — Screenshot problems
**Usually means:** screenshots show the splash/login screen, don't match the current UI, are wrong for the device size, or aren't 4+ appropriate.
**Fix:** regenerate from the real app in use. Metadata-only, so no new binary.

### 2.3.10 — Other platforms in metadata
**Usually means:** an Android device frame, a "Also on Google Play" line, or a competitor marketplace mention.
**Fix:** remove and resubmit metadata.

### 3.1.1 — Missing in-app purchase
**Usually means:** the app unlocks digital content or features with something other than StoreKit — a web checkout, a promo/license code, an account upgraded on your site, a Stripe flow, a crypto payment.
**Fix:** move that unlock to StoreKit, or (rarely) prove your case falls under 3.1.3(a)–(g) — reader, multiplatform, enterprise, person-to-person, physical goods, free stand-alone, or ad management. Write the argument with the sub-letter, plainly.
**Also triggers on:** an external link or call to action toward non-IAP purchasing, outside the US storefront, without the entitlement.

### 3.1.2 — Subscription disclosure
**Usually means:** the paywall doesn't state the price, the billing period, the auto-renewal, or how to cancel; or Terms/Privacy links are missing.
**Fix:** put all of it above the purchase button — price, period, "renews until cancelled", trial length and what happens after, cancellation instructions, Terms and Privacy Policy links.

### 4.2 — Minimum functionality
**Usually means:** the app is a web wrapper, a link collection, or too thin to justify a native app.
**Fix:** add genuine native value — offline behavior, notifications tied to real events, native navigation, device integrations. A cosmetic change won't clear this; the reviewer is judging substance.

### 4.3 — Spam / duplicate
**Usually means:** it looks like an existing app, or like one of several near-identical apps from you, or it's in a saturated category (dating, flashlight, wallpaper, sound effects, simple timers, fortune telling).
**Fix:** consolidate multiple bundle IDs into one app with IAP variants, and articulate — in the notes and the description — what is meaningfully different.

### 4.8 — Sign in with Apple missing
**Usually means:** the app offers Google/Facebook/X login for the primary account with no equivalent privacy-preserving option.
**Fix:** add Sign in with Apple, or claim an exemption from 4.8's list (own account system only, education/enterprise, government eID, or a client for a specific third-party service).

### 5.1.1(v) — Account deletion missing
**Usually means:** the app creates accounts but only offers "contact support to delete".
**Fix:** ship a real in-app deletion flow that deletes the account (not just the local session), reachable from the app's own UI — typically Settings → Account → Delete Account, with a confirmation step. Then point the reviewer at the exact path in the notes.

### 5.1.1(i) / (ii) — Privacy policy and purpose strings
**Usually means:** no policy link inside the app, a policy that doesn't cover third-party sharing or deletion, or a vague `NS*UsageDescription`.
**Fix:** rewrite purpose strings to name the feature and the benefit ("Photo access lets you attach receipts to a transaction; photos stay on your device"). Add the in-app policy link. Re-verify nutrition labels against every SDK.

### 5.1.2 — Tracking without ATT
**Usually means:** an SDK collects identifiers for cross-app tracking with no ATT prompt, or the app blocks features when the user declines.
**Fix:** implement `ATTrackingManager.requestTrackingAuthorization`, and make the app fully usable when the answer is No.

### 5.2.x — Intellectual property
**Usually means:** third-party brand names, logos, characters, or content without evidence of rights.
**Fix:** remove it, or supply the authorization — Apple will ask for documentation, so have it ready before you reply.

### Guideline 1.2 — UGC controls
**Usually means:** the app lets people post but has no report, no block, or no filter.
**Fix:** ship all four controls (filter, report, block, published contact) and show the reviewer where each one lives.

---

## Reply templates

### Fixed in a new build
> Hi App Review team,
>
> Thank you for the detailed feedback regarding Guideline **{N}**.
>
> We have addressed this in build **{version} ({build})**:
> - {specific change 1}
> - {specific change 2}
>
> To verify: {step-by-step path, starting from launch}.
> Demo account: **{user} / {password}**.
>
> Please let us know if anything else needs clarification.

### Clarification — the reviewer misread the app
> Hi App Review team,
>
> Thank you for the review. We believe there may be a misunderstanding regarding Guideline **{N}**.
>
> {One paragraph: what the app actually does, and why what the reviewer saw is not what the guideline describes.}
>
> Steps to observe the intended behavior:
> 1. {step}
> 2. {step}
>
> {Attach a screen recording if the behavior is timing- or state-dependent.}
> We are happy to make changes if we've misunderstood the concern.

### Appeal — the guideline doesn't apply
> We would like to appeal the rejection under Guideline **{N}**.
>
> **What our app does:** {2 sentences.}
> **Why {N} does not apply:** {cite the exact sub-clause or exemption, e.g. "3.1.3(e), because the purchase is a physical good delivered to the customer's address".}
> **Supporting evidence:** {licensing docs, ToS authorization, screenshots, prior precedent in our own app history.}
>
> We appreciate the Board's consideration.

### Requesting the bug-fix exception (app already live)
> Our app is currently live on the App Store and this submission contains only bug fixes for {issue affecting users}. Per the Bug Fix Submissions policy, we request that this build be approved and commit to resolving the Guideline **{N}** issue in our next submission.

---

## Rules of engagement

- **Answer every point.** Partial replies get partial re-reviews and another round trip.
- **Be specific and verifiable.** "We fixed it" restarts the clock; "Settings → Account → Delete Account, confirmation dialog, DELETE /v1/account" ends it.
- **Attach a screen recording** for anything state- or timing-dependent. It's the single highest-leverage thing you can send.
- **Never argue tone.** Guideline 5.6 makes respect a compliance requirement, and reviewers are people.
- **Don't resubmit the same binary** hoping for a different reviewer — repeat rejections for the same guideline slow down all your future reviews.
- **Expedited review is finite credibility.** Use it for real emergencies (a live crash, a legal deadline), not for a launch date you chose.
- **Metadata rejections need no new binary** — fix in App Store Connect and resubmit for review.
