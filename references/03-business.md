# Section 3 — Business

> Pricing is yours; the *mechanism* is not. Apple rejects "clear rip-offs" and irrationally high prices, and expels developers who manipulate reviews or chart rankings with paid, incentivized, filtered or fake feedback.

If your business model isn't obvious, explain it in metadata **and** the App Review notes. Unclear monetization delays review and can trigger rejection.

## The payment decision tree

```
What is the user buying?
│
├─ Digital content, features, functionality, or services consumed IN the app
│   └─ ► IN-APP PURCHASE. Mandatory. (3.1.1)
│        No license keys, AR markers, QR codes, crypto, or your own checkout.
│
├─ Physical goods, or real-world services consumed OUTSIDE the app
│   └─ ► MUST NOT use IAP. Use Apple Pay or credit card entry. (3.1.3(e))
│
├─ Real-time person-to-person service between TWO individuals
│   (tutoring, medical consult, real estate tour, personal training)
│   └─ ► May use other payment methods. (3.1.3(d))
│        One-to-few and one-to-many real-time services → IAP.
│
├─ Access to content already purchased elsewhere
│   ├─ Magazines, newspapers, books, audio, music, video → "Reader" app (3.1.3(a))
│   ├─ Acquired in your app on another platform → Multiplatform (3.1.3(b))
│   └─ Sold by you directly to organizations for employees/students → Enterprise (3.1.3(c))
│        (Consumer / single-user / family sales still require IAP.)
│
└─ Nothing purchasable in the app at all, companion to a paid web tool
    └─ ► Free stand-alone app. (3.1.3(f))
         No purchasing inside, and no calls to action to purchase outside.
```

## 3.1.1 In-app purchase — the details

- Unlocking features/functionality (subscriptions, in-game currency, levels, premium content, full-version unlock) **must** use IAP.
- IAP currencies may be used to **tip** the developer or in-app digital content providers.
- Purchased credits or in-game currencies **may not expire**. Provide a **restore mechanism** for restorable purchases.
- **Gifting** of IAP-eligible items is allowed; gifts refund only to the original purchaser and can't be exchanged.
- Mac App Store apps may host plug-ins/extensions enabled by non-App-Store mechanisms.
- **Loot boxes** and other randomized-item purchases must **disclose the odds** of each item type before purchase.
- Digital gift cards/certificates/vouchers/coupons redeemable for digital goods: IAP only. Physical gift cards mailed to customers may use other payment methods.
- **Free trials for non-subscription apps**: a Non-Consumable IAP at Price Tier 0 named `XX-day Trial`. Before the trial starts, disclose its duration, what stops working at the end, and any downstream charges. Manage access with Receipts and DeviceCheck.
- **NFTs**: IAP may sell NFT services (minting, listing, transferring). Users may view their own NFTs, **provided NFT ownership does not unlock app features**. Browsing others' collections is allowed but — outside the United States storefront — without buttons, external links, or calls to action toward non-IAP purchasing.

### 3.1.1(a) Links to other purchase methods
- **United States storefront**: buttons, external links and calls to action to other purchasing mechanisms are permitted without an entitlement.
- **Elsewhere**: you need a **StoreKit External Purchase Link Entitlement** (region-limited, iOS/iPadOS only) to link out to your own site to inform users about other purchase options and comparatively lower prices.
- **Music streaming services** have their own entitlement, which additionally permits collecting an email address solely to send a purchase link.
- In every other storefront without an applicable entitlement, apps and their metadata **may not include buttons, external links, or other calls to action** directing customers to non-IAP purchasing.
- Misleading marketing, scams or fraud around the entitlement = app removal and possible Developer Program removal.

## 3.1.2 Subscriptions

**(a) Permissible uses** — auto-renewable subscriptions are allowed in any category, but must deliver **ongoing value**, last **at least seven days**, and work **across all of the user's devices**. Legitimate examples: new game levels, episodic content, multiplayer support, consistent substantive updates, large or continually updated media libraries, SaaS, cloud support.
- May be offered alongside à la carte purchases.
- Streaming game service subscriptions may share one subscription across third-party apps, but games must be downloaded from the App Store, avoid duplicate payment, and not disadvantage non-subscribers.
- **Users must get what they paid for without extra tasks** — no requiring social posts, contact uploads, or check-in streaks.
- May include consumable credits/gems/currency and discounted consumable access.
- **Switching an existing app to subscriptions must not remove primary functionality existing users already paid for** (a prior "full game unlock" must keep working).
- Free trials are configured in App Store Connect.
- **Scam subscriptions** — tricking users into subscribing under false pretenses, bait-and-switch — get the app removed and may end the developer account.
- Cellular carrier bundle subscriptions require prior Apple approval and must terminate with the data plan.

**(b) Upgrades/downgrades** — seamless, and users must not be able to inadvertently subscribe to multiple variations of the same thing.

**(c) Subscription information** — **before asking someone to subscribe**, clearly describe what they get for the price: how many issues per month, how much cloud storage, what kind of access. Meet the requirements in Schedule 2 of the Developer Program License Agreement.

> **Paywall checklist (3.1.2(c) + Apple Pay-style disclosure):** price, billing period, what's included, renewal-until-cancelled statement, trial length and what happens after it, how to cancel, links to Terms and Privacy Policy — all visible before the purchase button.

## 3.1.3 Other purchase methods — the shared constraint

Apps in 3.1.3 **cannot encourage users, inside the app, to use a non-IAP purchase method** — except on the United States storefront and as allowed by 3.1.1(a) and 3.1.3(a). You *may* communicate with your user base about other purchase methods **outside** the app.

- **(a) Reader apps** — access to previously purchased content or subscriptions: magazines, newspapers, books, audio, music, video. May offer free-tier account creation and account management for existing customers. The **External Link Account Entitlement** allows an informational link to your site for creating/managing an account (not required on the US storefront).
- **(b) Multiplatform services** — users may access content, subscriptions or features acquired in your app on other platforms or your website, including consumable items in multiplatform games, provided those items are also available as IAP in the app.
- **(c) Enterprise services** — apps sold directly by you to organizations for their employees or students may let enterprise users access previously purchased content. Consumer/single-user/family sales require IAP.
- **(d) Person-to-person services** — real-time services between two individuals may use other payment methods. One-to-few and one-to-many must use IAP.
- **(e) Goods and services outside the app** — physical goods or services consumed outside the app **must** use non-IAP payment (Apple Pay, card entry).
- **(f) Free stand-alone apps** — free companions to paid web tools (VoIP, cloud storage, email, web hosting) need no IAP, provided there is no purchasing in the app and no calls to action to purchase outside it.
- **(g) Advertising management apps** — apps solely for advertisers to buy and manage campaigns across media types don't need IAP; they must not display the ads themselves. **Buying ads shown inside the same app (e.g. post "boosts") must use IAP.**

## 3.1.4 Hardware-specific content
Functionality dependent on specific hardware may unlock without IAP (e.g. an astronomy app that gains features when synced to a telescope). Features unlocked optionally by an approved physical product (a toy) may unlock without IAP **provided an IAP option also exists**. You may never require buying unrelated products or engaging with advertising/marketing to unlock functionality.

## 3.1.5 Cryptocurrencies
- **(i) Wallets** — allowed, developer must be enrolled as an **organization**.
- **(ii) Mining** — **not on device**; cloud-based mining only.
- **(iii) Exchanges** — allowed on an approved exchange, only in countries/regions where the app holds licensing and permissions.
- **(iv) ICOs / crypto futures / crypto-securities** — must come from established banks, securities firms, FCMs or other approved financial institutions, and comply with all applicable law.
- **(v)** No offering currency for completing tasks — downloading other apps, referrals, social posts.

## 3.2 Other business model issues

### 3.2.1 Acceptable
- (i) Promoting your own apps within your app — as long as the app isn't merely a catalog of your apps.
- (ii) Recommending third-party apps for a specific approved need (health management, aviation, accessibility) with **robust editorial content**, not a storefront.
- (iii) Expiring access to approved **rental** content (films, TV, music, books). Nothing else may expire.
- (iv) Wallet passes for payments, offers, and identification (tickets, coupons, VIP credentials). Other uses risk rejection and Wallet credential revocation.
- (v) **Insurance apps must be free**, legally compliant in their regions, and may not use IAP.
- (vi) **Approved nonprofits** may fundraise in-app, with Apple Pay support, disclosure of fund use, legal compliance, and tax receipts. Platforms connecting donors to other nonprofits must ensure every listed nonprofit is also approved.
- (vii) Person-to-person **monetary gifts** without IAP, provided the gift is entirely optional and **100% of funds go to the receiver**. A gift connected at any point to receiving digital content or services must use IAP.
- (viii) Financial trading/investing/money management apps must be submitted by the financial institution performing the service, with the necessary licensing in every location offered.

### 3.2.2 Unacceptable
- (i) An App-Store-like interface for third-party apps, extensions or plug-ins, or a general-interest collection of them.
- (iii) Artificially inflating ad impressions or click-throughs; apps designed predominantly to display ads.
- (iv) Collecting funds for charities/fundraisers unless an approved nonprofit (see 3.2.1(vi)). Otherwise the app must be free and collect funds outside the app (Safari, SMS).
- (v) Arbitrarily restricting who may use the app — by location, carrier, etc.
- (vii) Artificially manipulating a user's visibility, status or rank on other services, unless that service's terms permit it.
- (viii) **Binary options trading is banned.** CFDs and other derivatives (e.g. FOREX) require proper licensing in every jurisdiction offered.
- (ix) **Personal loan apps** must conspicuously disclose all loan terms including maximum equivalent **APR** and payment due date. **Max APR 36%** including costs and fees, and **no repayment-in-full within 60 days or less.**
- (x) **Never force users to rate, review, download other apps, or take store-related actions** to access functionality or content. Other in-app incentives (complete a level, watch an ad) are fine.

---

## Audit checklist

- [ ] Every digital unlock goes through StoreKit — no license keys, codes, or web checkout
- [ ] Physical goods/services do **not** use IAP
- [ ] Restore Purchases exists and works; no expiring credits
- [ ] Paywall discloses price, period, renewal, trial terms, and how to cancel, before purchase
- [ ] Subscription lasts ≥7 days and works on all the user's devices
- [ ] No external purchase links outside the US storefront without the entitlement
- [ ] Loot boxes disclose odds pre-purchase
- [ ] No rating/review/download gating (3.2.2(x))
- [ ] Business model explained in Notes for Review if not self-evident
