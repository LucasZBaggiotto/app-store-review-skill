# Section 4 — Design

> "Minimum standards for approval." Design quality is enforceable: apps that stop working or degrade may be removed at any time, even years after approval.

## 4.1 Copycats
- **(a)** Don't copy a popular app, or make minor changes to another app's name or UI and pass it off as your own.
- **(b)** Impersonating other apps or services violates the Developer Code of Conduct and may end your Developer Program membership.
- **(c)** You cannot use another developer's icon, brand or product name in your app's icon or name without their approval.

## 4.2 Minimum functionality

The app must have features, content and UI that **elevate it beyond a repackaged website**. If it isn't particularly useful, unique or "app-like," or lacks lasting entertainment value or adequate utility, it will be rejected. A single song or movie belongs on the iTunes Store; a book or game guide belongs on Apple Books.

- **4.2.1** ARKit apps must deliver rich, integrated AR — dropping a model into an AR view or replaying an animation is not enough.
- **4.2.2** Apart from catalogs, apps must not primarily be marketing materials, advertisements, web clippings, content aggregators, or link collections.
- **4.2.3** (i) The app must work on its own without requiring another app to be installed. (ii) If it downloads additional resources to function on first launch, **disclose the download size and prompt** before downloading.
- **4.2.6 Template / app-generation apps** are rejected unless submitted **directly by the provider of the app's content**. Template services must not submit on clients' behalf; they should give clients tools to build customized, innovative apps, or ship a **single binary hosting all client content** in an aggregated/"picker" model (e.g. one restaurant-finder app with a page per client restaurant).
- **4.2.7 Remote desktop clients** that mirror specific software/services (rather than a generic mirror of the host device) must:
  - (a) connect only to a **user-owned personal computer or dedicated game console**, with host and client on the **same local LAN**;
  - (b) fully execute and render all software on the host device, using no APIs beyond what streaming requires;
  - (c) initiate all account creation and management **from the host device**;
  - (d) not resemble an iOS or App Store view, offer a store-like interface, or allow browsing/selecting/purchasing software the user doesn't already own (transactions inside mirrored software need not use IAP if processed on the host);
  - (e) thin clients for cloud-based apps are not appropriate for the App Store.

## 4.3 Spam
- **(a)** No multiple Bundle IDs of the same app (one map app per city instead of a searchable world map). Ship one app and use IAP for variations by location, team, university, etc.
- **(b)** No apps **indistinguishable from what's already widely available**. Opportunistic variants of existing categories or popular apps degrade discovery. **Dating, flashlight, sound effects, wallpaper, simple timers and fortune telling are considered saturated** — new submissions need a meaningfully different or improved experience, and existing ones may be removed if not updated or if they attract no customers. Drinking games, Kama Sutra, fart and burp apps are called out as low-effort; repeat submissions can end your Developer Program membership.

## 4.4 Extensions
Must comply with the App Extension Programming Guide or the Safari app/web extension documentation, and should include functionality like help screens and settings interfaces. Disclose available extensions clearly in marketing text. **Extensions may not include marketing, advertising or in-app purchases.**

- **4.4.1 Keyboards** — **must**: provide keyboard input; follow Sticker guidelines if they include images/emoji; provide a way to progress to the next keyboard; remain functional without full network access and without Full Access; collect user activity only to enhance the keyboard extension on that device. **Must not**: launch apps other than Settings; repurpose keyboard buttons (e.g. hold Return to launch the camera).
- **4.4.2 Safari extensions** — must run on the current Safari version, must not interfere with System or Safari UI, never include malicious or misleading content or code (violation = Developer Program removal), and should not claim access to more websites than strictly necessary.

## 4.5 Apple sites and services
- **4.5.1** You may use approved Apple RSS feeds, but may **not scrape** Apple sites (apple.com, iTunes Store, App Store, App Store Connect, developer portal) or create rankings from that information.
- **4.5.2 Apple Music / MusicKit**
  - (i) Users must initiate playback and be able to use standard controls (play/pause/skip). **You may not charge for or indirectly monetize access to Apple Music** (IAP, advertising, requesting user info). Don't download, upload or enable sharing of MusicKit-sourced music files beyond what the documentation permits.
  - (ii) MusicKit is not a substitute for licensing. Playing a specific song at a moment, or creating shareable audio/video, requires synchronization/adaptation rights from rights-holders. Cover art and metadata only in connection with playback or playlists — not marketing or advertising without authorization. Follow the Apple Music Identity Guidelines.
  - (iii) Accessing Apple Music user data (playlists, favorites) must be disclosed in the purpose string. That data may not be shared with third parties except to support/improve the app, and may never identify users or devices or target advertising.
- **4.5.3** Don't use Apple services (Game Center, Push Notifications, Live Activities) to spam, phish or send unsolicited messages. Don't reverse-lookup, trace, mine or exploit Player IDs or aliases — that ends your Developer Program membership.
- **4.5.4 Push Notifications** — must not be required for the app to function, and must not carry sensitive personal or confidential information. **Promotional or direct-marketing pushes require explicit opt-in via consent language in your app's UI, plus an in-app opt-out.**
- **4.5.5** Game Center Player IDs only as approved; never displayed in the app or to third parties.
- **4.5.6** Apple emoji may be used as Unicode characters in your app and metadata, but not on other platforms and never embedded in your binary.

## 4.7 Mini apps, mini games, streaming games, chatbots, plug-ins, game emulators

Apps may offer software not embedded in the binary: HTML5/JavaScript mini apps and mini games, streaming games, **chatbots**, and plug-ins; retro game console and PC emulators may offer game downloads. **You are responsible for all such software** — its guideline compliance and its legality. Non-compliant hosted software rejects the host app.

- **4.7.1** Hosted software must: follow all privacy guidelines including 5.1 (collection, use, sharing, sensitive data such as health and kids' data); include **content filtering, a report mechanism with timely responses, and user blocking**; and follow **3.1** for any digital goods or services.
- **4.7.2** Don't extend or expose native platform APIs or technologies to the hosted software without prior Apple permission.
- **4.7.3** Don't share data or privacy permissions with any individual hosted software without **explicit user consent in each instance**.
- **4.7.4** Provide an **index of the software and metadata** available in your app, including **universal links** to all of it.
- **4.7.5** Let users identify software exceeding the app's age rating, and gate it with an age restriction mechanism based on verified or declared age.

> This is the section that governs AI chatbot marketplaces, LLM "app stores", and prompt/agent galleries.

## 4.8 Login services (Sign in with Apple, in practice)

If your app uses a **third-party or social login service** (Facebook Login, Google Sign-In, Log in with X, Sign In with LinkedIn, Login with Amazon, WeChat Login) to set up or authenticate the user's **primary account**, you must **also** offer an equivalent login option that:

1. limits data collection to the user's **name and email address**;
2. lets users **keep their email address private** while setting up the account; and
3. does **not** collect app interactions for advertising without consent.

**Not required if:**
- Your app exclusively uses your own account system.
- Your app is an alternative app marketplace, or distributed from one, using a marketplace-specific login.
- It's an education/enterprise/business app requiring an existing education or enterprise account.
- It uses a government or industry-backed citizen ID or electronic ID.
- It's a client for a specific third-party service and users must sign in to that account directly to reach their content.

## 4.9 Apple Pay
Provide **all material purchase information before the sale**, and use Apple Pay branding and UI elements per the Apple Pay Marketing Guidelines and HIG. Recurring payments via Apple Pay must disclose, at minimum:
- the renewal term length and that it continues until cancelled;
- what is provided each period;
- the actual charges billed;
- how to cancel.

## 4.10 Monetizing built-in capabilities
You may not monetize hardware or OS capabilities — Push Notifications, the camera, the gyroscope — or Apple services and technologies such as Apple Music access, iCloud storage, or the Screen Time APIs.

---

## Audit checklist

- [ ] The app is more than a wrapped website; it has native value (4.2)
- [ ] Not a template/generator output submitted by a non-owner (4.2.6)
- [ ] Not a saturated-category clone without meaningful differentiation (4.3(b))
- [ ] One app, not N bundle IDs of the same thing (4.3(a))
- [ ] Extensions carry no ads, marketing, or IAP (4.4)
- [ ] Push notifications aren't required to use the app; marketing pushes are opt-in with in-app opt-out (4.5.4)
- [ ] Social/third-party primary login is paired with Sign in with Apple or an equivalent (4.8)
- [ ] Hosted AI/mini-app content: moderation, index with universal links, age gating, IAP for monetization (4.7)
- [ ] Apple Pay recurring disclosures present (4.9)
- [ ] No monetizing OS/Apple capabilities (4.10)
