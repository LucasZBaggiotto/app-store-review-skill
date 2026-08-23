# Section 1 — Safety

> Users must feel confident an App Store app won't upset them, damage their device, or cause physical harm.

## 1.1 Objectionable content

Nothing offensive, insensitive, upsetting, disgusting, in exceptionally poor taste, or "just plain creepy".

| Rule | Prohibited |
|---|---|
| 1.1.1 | Defamatory, discriminatory or mean-spirited content — especially targeting religion, race, sexual orientation, gender, national/ethnic origin, or other targeted groups. Professional political satirists/humorists are generally exempt. |
| 1.1.2 | Realistic depictions of people or animals being killed, maimed, tortured or abused; content encouraging violence. In-game "enemies" may not solely be a specific race, culture, real government, corporation or other real entity. |
| 1.1.3 | Encouraging illegal/reckless weapon use; facilitating firearm or ammunition purchase. |
| 1.1.4 | Overtly sexual or pornographic material. Includes "hookup" apps and anything facilitating prostitution, trafficking or exploitation. |
| 1.1.5 | Inflammatory religious commentary; inaccurate or misleading quotation of religious texts. |
| 1.1.6 | False information/features: inaccurate device data, trick/joke functionality, fake location trackers, anonymous or prank calls/SMS. **"For entertainment purposes" does not exempt you.** |
| 1.1.7 | Capitalizing on recent/current events — violent conflicts, terrorist attacks, epidemics. |

## 1.2 User-generated content — the four mandatory controls

Any app with UGC or social networking **must** include all four:

1. A method for **filtering objectionable material** before it is posted.
2. A **mechanism to report** offensive content — plus timely responses to reports.
3. The ability to **block abusive users**.
4. **Published contact information** so users can reach you.

Apps that end up used primarily for pornography, Chatroulette-style or random/anonymous chat, objectification of real people ("hot-or-not" voting), physical threats or bullying may be **removed without notice**. Removing violating content is your responsibility; egregious or repeated failure means removal from the App Store and the Developer Program.

Web-sourced UGC may show incidental "NSFW" content only if hidden by default and enabled by the user on *your website*.

### 1.2.1 Creator content
Apps hosting content from a community of non-developer "creators" are allowed if properly moderated. Creator experiences are **content, not apps** — they must not change the host app's core features and functionality. They must follow 1.2 (moderation) and 3.1.1 (IAP for anything monetized). Tell users which content requires additional purchases.
- **(a)** Must let users identify content exceeding the app's age rating, and gate it behind an age restriction mechanism based on verified or declared age.

## 1.3 Kids Category

- No links out of the app, no purchasing opportunities, no distractions — unless behind a **parental gate**.
- Once you ship in the Kids Category, later updates must keep meeting these rules even if you deselect the category.
- Must comply with children's privacy law worldwide (COPPA, GDPR, etc. — see 5.1.4).
- **May not send PII or device information to third parties.**
- **No third-party analytics and no third-party advertising**, with two narrow exceptions:
  - Third-party analytics that collect/transmit no IDFA and nothing identifying children, their location or their devices.
  - Third-party **contextual** advertising from services with publicly documented Kids Category policies that include **human review of ad creatives** for age appropriateness.

## 1.4 Physical harm

- **1.4.1 Medical apps** — greater scrutiny if they could give inaccurate data or be used to diagnose/treat. Accuracy claims must disclose data and methodology; unverifiable claims = rejection. Explicitly banned: taking x-rays, or measuring blood pressure, body temperature, blood glucose or blood oxygen **using only device sensors**. Remind users to consult a doctor. Submit regulatory clearance documentation if you have it.
- **1.4.2 Drug dosage calculators** — must come from the drug manufacturer, a hospital, university, health insurer, pharmacy or other approved entity, or hold FDA (or international equivalent) approval.
- **1.4.3** No encouraging tobacco/vape, illegal drugs, or excessive alcohol; never toward minors. No facilitating sale of controlled substances (except licensed pharmacies and licensed/legal cannabis dispensaries) or tobacco.
- **1.4.4** DUI checkpoints only from law-enforcement publications; never encourage drunk driving, excessive speed or reckless behavior.
- **1.4.5** Don't urge users into bets, challenges, or device use that risks physical harm.

## 1.5 Developer information

The app **and** its Support URL must offer an easy way to contact you. Especially important for classroom apps; missing/stale contact info may be illegal in some regions. Wallet passes must carry valid issuer contact info and be signed with a certificate dedicated to the brand/trademark owner.

## 1.6 Data security

Implement appropriate security measures for user information collected under the Developer Program License Agreement and these guidelines, preventing unauthorized use, disclosure, or third-party access. See 5.1.

## 1.7 Reporting criminal activity

Apps for reporting alleged criminal activity must involve local law enforcement, and may only be offered where that involvement is active.

---

## Audit checklist

- [ ] No content that trips 1.1.1–1.1.7 (check UGC samples, not just first-party content)
- [ ] UGC apps: filter + report + block + published contact — all four shipped and reachable
- [ ] UGC apps: a moderation process actually exists behind the report button
- [ ] Creator content: age-rating identification + age restriction mechanism
- [ ] Kids Category: parental gate on every link-out and purchase; zero third-party ads/analytics (or documented exception)
- [ ] Health/medical claims backed by disclosed methodology; no device-sensor-only vitals
- [ ] Contact info present in-app and at the Support URL
