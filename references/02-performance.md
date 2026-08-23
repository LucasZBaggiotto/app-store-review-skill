# Section 2 — Performance

> Where most first-submission rejections happen. 2.1 and 2.3 alone account for the majority.

## 2.1 App completeness

**(a)** Submissions (including pre-orders) must be **final versions**: complete metadata, working URLs, no placeholder text, no empty websites, no temporary content. Tested on-device for bugs and stability.
- Provide **demo account credentials** if the app has a login. If legal/security obligations prevent that, a built-in **demo mode** is allowed *with prior Apple approval* and must exhibit the app's full features.
- **Turn your backend on** and keep it live through review.
- Incomplete bundles, crashes, or obvious technical problems = rejection.

**(b)** In-app purchases must be complete, up to date, **visible to the reviewer**, and functional. If a configured IAP can't be found in the app, explain why in the review notes.

## 2.2 Beta testing

Demos, betas and trial versions belong on **TestFlight**, not the App Store. TestFlight builds must be intended for public distribution and comply with these guidelines. **Testers may not be compensated in any way**, including as a crowdfunding reward. Significant updates to a beta build go through TestFlight App Review first.

## 2.3 Accurate metadata

Metadata — privacy information, description, screenshots, previews — must accurately reflect the app's **core experience** and stay current.

### 2.3.1 Hidden features / misleading marketing
- **(a)** No hidden, dormant or undocumented features. Functionality must be clear to users *and* App Review. **Every new feature, functionality and product change must be described with specificity in Notes for Review — generic descriptions will be rejected.** Misleading marketing (promoting content or services the app doesn't offer, e.g. iOS virus/malware scanners; advertising a false price, inside or outside the App Store) is grounds for **removal and developer account termination**.
- **(b)** Egregious or repeated dishonesty = removal from the Apple Developer Program.

### 2.3.2 In-app purchase disclosure
Description, screenshots and previews must clearly indicate when featured items, levels or subscriptions require additional purchases. Promoted IAPs need public-audience-appropriate Display Name, Screenshot and Description, and the app must handle `SKPaymentTransactionObserver` so promoted purchases complete on launch.

### 2.3.3 Screenshots
Must show the **app in use** — not merely title art, a login page, or a splash screen. Text and image overlays are allowed (e.g. animated touch points, Apple Pencil demos), as is showing extended on-device functionality.

### 2.3.4 App previews
**Video screen captures of the app itself only.** Stickers/iMessage extensions may show the Messages experience. Narration and video/text overlays may be added for clarity.

### 2.3.5 Category
Pick the most appropriate one; Apple may recategorize you.

### 2.3.6 Age rating
Answer honestly so parental controls work. Mis-rating surprises customers and can trigger regulator inquiries. You are responsible for local content-rating/warning requirements per territory.

### 2.3.7 Name and keywords
- **App names ≤ 30 characters.**
- Unique name; keywords that genuinely describe the app.
- No trademarked terms, popular app names, pricing information, or irrelevant phrases stuffed into metadata.
- Names, subtitles, screenshots and previews must not include prices, terms, or descriptions not specific to that metadata type.
- Subtitles must not include inappropriate content, reference other apps, or make unverifiable product claims.
- Apple may modify inappropriate keywords at any time.

### 2.3.8 4+ metadata rule
App and IAP **icons, screenshots and previews must adhere to a 4+ age rating**, even for a higher-rated app. "For Kids"/"For Children" in metadata is reserved for the Kids Category. Keep all icon variants (small, large, Apple Watch, alternate) similar to avoid confusion.

### 2.3.9 Rights and fictional data
You must own the rights to everything in icons, screenshots and previews. Display **fictional account information**, never a real person's data.

### 2.3.10 Platform focus
No names, icons or imagery of other mobile platforms or alternative app marketplaces in the app or its metadata, absent specific approved interactive functionality. Keep metadata about the app itself; no irrelevant information.

### 2.3.11 Pre-orders
Must be complete and deliverable as submitted; the released app must not be materially different from what was advertised. Material changes (e.g. a new business model) mean restarting pre-order sales.

### 2.3.12 "What's New"
Must clearly describe new features and product changes. Only simple bug fixes, security updates and performance improvements may use a generic description.

### 2.3.13 In-app events
Must match an App Store Connect event type; all metadata must be accurate and about the *event*, not the app. Events must occur at the selected times/dates across all storefronts. Monetization must follow Section 3. Deep links must land on the correct in-app destination.

## 2.4 Hardware compatibility

- **2.4.1** iPhone apps should run on iPad whenever possible.
- **2.4.2** Use power efficiently; don't rapidly drain battery, generate excessive heat, strain resources, or perform excessive SSD write cycles. Don't tell users to put the device under a mattress or pillow while charging. **No unrelated background processes — cryptocurrency mining is explicitly banned**, including inside third-party ads.
- **2.4.3** Apple TV apps must be usable with only the Siri Remote or third-party game controllers. If a controller is required, say so in metadata.
- **2.4.4** Never suggest or require a device restart, or system-setting changes unrelated to core functionality (e.g. don't ask users to turn off Wi-Fi or disable security features).
- **2.4.5 Mac App Store extras:**
  - (i) Properly sandboxed; follow macOS File System documentation; use the appropriate APIs to touch other apps' user data.
  - (ii) Packaged and submitted with Xcode technologies; no third-party installers; self-contained single-app bundles; no code/resources in shared locations.
  - (iii) No auto-launch or login items without consent; no processes surviving quit without consent; no auto-adding Dock icons or desktop shortcuts.
  - (iv) May not download or install standalone apps, kexts, or additional code/resources that add functionality or significantly change the app.
  - (v) No escalation to root, no setuid.
  - (vi) No license screen at launch, no license keys, no own copy protection.
  - (vii) Updates via the Mac App Store only.
  - (viii) Must run on the currently shipping OS; no deprecated or optionally installed technologies (e.g. Java).
  - (ix) All localizations in a single bundle.

## 2.5 Software requirements

| Rule | Requirement |
|---|---|
| 2.5.1 | **Public APIs only**, running on the currently shipping OS. Phase out deprecated frameworks. Use frameworks for their intended purpose (HomeKit for home automation; HealthKit for health/fitness, integrated with the Health app) and state the integration in the description. |
| 2.5.2 | Apps must be **self-contained in their bundle**; no reading/writing outside the container; **no downloading, installing or executing code** that introduces or changes features. Narrow exception for educational coding apps, where the code must be fully viewable and editable by the user. |
| 2.5.3 | No transmitting viruses/files/code that harm or disrupt the OS or hardware, including via Push Notifications and Game Center. Egregious/repeat = Developer Program removal. |
| 2.5.4 | Background modes only for their intended purposes: VoIP, audio playback, location, task completion, local notifications, etc. |
| 2.5.5 | Must be **fully functional on IPv6-only networks**. |
| 2.5.6 | Web browsing must use WebKit and WebKit JavaScript. Alternative browser engine entitlements exist for the EU and Japan. |
| 2.5.8 | No alternate desktop/home screen environments. |
| 2.5.9 | Don't alter or disable standard switches (volume, Ring/Silent) or other native UI elements and behaviors; don't block links out to other apps. |
| 2.5.11 | **SiriKit/Shortcuts** — (i) only register intents you can handle alone and that users expect from your stated functionality; (ii) plist vocabulary and aliases must relate to your app/company, never generic terms or third-party names; (iii) fulfil the request as directly as possible, **no ads or marketing between request and fulfilment**, disambiguate only when required. |
| 2.5.12 | CallKit / SMS Fraud Extension apps may only block **confirmed spam** numbers. Marketing text must identify the blocking/spam-ID feature and explain list criteria. The accessed data may not be used for anything beyond operating/improving the app — no tracking, profiling, sharing or selling. |
| 2.5.13 | Facial recognition for account authentication must use **LocalAuthentication** (not ARKit or other face tech) where possible, plus an alternate method for users under 13. |
| 2.5.14 | **Explicit consent plus a clear visual and/or audible indicator** when recording or logging user activity — camera, microphone, screen recordings, or other inputs. |
| 2.5.15 | File pickers must include the Files app and the user's iCloud documents. |
| 2.5.16 | Widgets, extensions and notifications must relate to the app's content and functionality. **(a)** All App Clip features must exist in the main binary; **App Clips cannot contain advertising.** |
| 2.5.17 | Matter support must use Apple's Matter framework to initiate pairing; any non-Apple Matter component must be CSA-certified for the platform. |
| 2.5.18 | **Advertising rules** — ads only in the main app binary, never in extensions, App Clips, widgets, notifications, keyboards or watchOS apps. Ads must match the app's age rating; users must be able to see all targeting information without leaving the app. **No targeted/behavioral advertising from sensitive data** (HealthKit, ClassKit, or kids). Interstitials must be labeled as ads, must not trick users into tapping, and need an easily visible close/skip button large enough to hit. The app must let users **report inappropriate or age-inappropriate ads**. |

---

## Audit checklist

- [ ] No crashes on the current OS, on-device, on a clean install
- [ ] Backend live and staying live during review; demo account or approved demo mode supplied
- [ ] Every IAP visible and purchasable by the reviewer (or explained in notes)
- [ ] No placeholder copy, no dead links, no Lorem Ipsum, no "coming soon" screens
- [ ] Notes for Review specifically describe each new feature — not "bug fixes"
- [ ] App name ≤ 30 chars; no trademarks or competitor names in name/subtitle/keywords
- [ ] Screenshots show real in-use UI, not splash/login; previews are real screen captures
- [ ] All icons/screenshots/previews are 4+ appropriate
- [ ] Age rating answered honestly; category correct
- [ ] "What's New" describes actual changes
- [ ] Public APIs only; IPv6-only network tested; no downloaded executable code
- [ ] Background modes justified; no mining, no unrelated background work
- [ ] Recording/logging has consent + an on-screen indicator
- [ ] Ads (if any): main binary only, labeled, dismissible, age-appropriate, reportable
