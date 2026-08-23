# Pre-Submission Checklist

Copy into your PR or release ticket. Every unchecked box is a review round trip.

## Build quality (2.1, 2.4, 2.5)
- [ ] No crashes: clean install, fresh account, physical device, current shipping OS
- [ ] Tested on the smallest and largest supported screen sizes
- [ ] Tested on an **IPv6-only** network (2.5.5)
- [ ] Tested with permissions **denied** — the app still works (5.1.1(iv))
- [ ] Tested offline / on a poor connection
- [ ] iPhone app runs on iPad if at all possible (2.4.1)
- [ ] No excessive battery drain, heat, or background work; no mining (2.4.2)
- [ ] Public APIs only; no deprecated frameworks; no downloaded executable code (2.5.1, 2.5.2)
- [ ] Background modes limited to their declared purpose (2.5.4)
- [ ] No dead links, placeholder text, or unfinished screens anywhere

## Reviewer access (2.1)
- [ ] Demo account created, tested **today**, not rate-limited or expiring
- [ ] Backend, feature flags and remote config live for the reviewer's region
- [ ] Every IAP is reachable and purchasable in the sandbox
- [ ] Any hardware requirement stated, or a demo mode provided
- [ ] Notes for Review: demo credentials, what the app does, how it earns money, repro steps for non-obvious features, regulatory docs

## Money (3.1)
- [ ] Digital unlocks go through StoreKit — no codes, no web checkout, no crypto
- [ ] Physical goods/services do **not** use IAP
- [ ] Restore Purchases implemented and tested
- [ ] Paywall shows: price · billing period · renews-until-cancelled · trial terms · how to cancel · Terms · Privacy Policy
- [ ] Subscription ≥ 7 days, works across the user's devices
- [ ] No external purchase links outside the US storefront without the entitlement
- [ ] Loot box odds disclosed pre-purchase, if applicable
- [ ] Nothing gated on rating, reviewing, or downloading another app (3.2.2(x))

## Accounts (4.8, 5.1.1(v))
- [ ] App usable without login if account features aren't core
- [ ] **In-app account deletion** shipped and reachable (path documented in the notes)
- [ ] Sign in with Apple (or equivalent) offered alongside any social login for the primary account
- [ ] Social tokens never stored off-device; in-app credential revocation available

## Privacy (5.1)
- [ ] Privacy policy URL in App Store Connect **and** linked inside the app
- [ ] Policy covers: what's collected, how, all uses, third-party recipients, retention/deletion, consent revocation
- [ ] Every `NS*UsageDescription` names the feature and the user benefit
- [ ] Only permissions the core features need (data minimization)
- [ ] ATT prompt implemented if any cross-app/site tracking occurs; app fully usable if declined
- [ ] Privacy nutrition labels audited against the code **and every third-party SDK**
- [ ] Privacy Manifests present for the app and required SDKs
- [ ] Recording/logging user activity: consent + visible or audible indicator (2.5.14)
- [ ] Health data: not in iCloud, never for advertising, specifically disclosed (5.1.3)
- [ ] Kids: no third-party ads/analytics, privacy policy, parental gate (1.3, 5.1.4)

## User-generated content (1.2)
- [ ] Content filter for objectionable material
- [ ] Report mechanism, with a real process behind it
- [ ] Block abusive users
- [ ] Published contact information

## Metadata (2.3)
- [ ] App name ≤ 30 characters, unique
- [ ] Subtitle accurate, no competitor references, no unverifiable claims
- [ ] Keywords: no trademarks, no competitor names, no pricing
- [ ] Screenshots show the app **in use**, current UI, correct device sizes
- [ ] Preview videos are real screen captures of the app
- [ ] Icons/screenshots/previews all 4+ appropriate
- [ ] Category correct; age rating answered honestly
- [ ] Description discloses that features/levels/content require additional purchases
- [ ] No other-platform names, icons, or imagery
- [ ] "What's New" describes the actual changes
- [ ] Support URL live, with a working way to contact you (1.5)

## Legal (5.2–5.6)
- [ ] All content owned or licensed; third-party service ToS permit your use
- [ ] No Apple emoji embedded; no Apple-endorsement implication; no Apple-product lookalike UI
- [ ] Regulated fields: submitted by the licensed legal entity, geo-restricted where required
- [ ] Gambling/sweepstakes: licensed, geo-restricted, free, rules in-app, Apple disclaimed as sponsor
- [ ] Official review-prompt API used, not a custom rating dialog (5.6.1)

## Ads (2.5.18)
- [ ] Ads only in the main app binary
- [ ] Age-appropriate for the app's rating; targeting info visible without leaving the app
- [ ] No targeting from health, classroom, or kids' data
- [ ] Interstitials labeled, non-deceptive, with a large easy close button
- [ ] Users can report inappropriate ads
