# Section 5 — Legal

> You must comply with all laws everywhere the app ships — not just these guidelines. Apps soliciting, promoting or encouraging criminal or clearly reckless behavior are rejected; in extreme cases (human trafficking, child exploitation) Apple notifies authorities.

## 5.1 Privacy

### 5.1.1 Data collection and storage

**(i) Privacy policies** — every app must link to its privacy policy **in App Store Connect metadata and inside the app, easily accessible**. The policy must clearly and explicitly:
- identify **what data is collected, how, and every use** of it;
- confirm that **any third party** receiving user data (analytics tools, ad networks, third-party SDKs, parent/subsidiary/related entities) provides the **same or equal protection** as the policy and these guidelines require;
- explain **data retention/deletion** and how a user can **revoke consent and/or request deletion**.

**(ii) Permission** — consent is required for collecting user or usage data, **even if anonymous at or immediately after collection**. **Paid functionality must not depend on granting data access.** Provide an easy, understandable way to **withdraw consent**. Purpose strings must clearly and completely describe your use of the data. Relying on GDPR legitimate interest without consent requires full compliance with that law.

**(iii) Data minimization** — request only data relevant to core functionality; collect only what the task requires. Prefer the **out-of-process picker or share sheet** over full access to Photos or Contacts.

**(iv) Access** — respect permission settings; never manipulate, trick or force consent. (Don't demand microphone access before letting someone upload a photo.) Provide alternatives when consent is declined — e.g. manual address entry when Location is refused.

**(v) Account sign-in** — this is the account-deletion rule:
- If the app has **no significant account-based features**, let people use it **without a login**.
- **If the app supports account creation, it must offer account deletion within the app.**
- Don't require personal information to function unless directly relevant to core functionality or legally required.
- If your core functionality isn't tied to a specific social network, provide access without that social login.
- Provide an in-app mechanism to **revoke social network credentials** and disable data access.
- Social credentials/tokens may **not be stored off-device**, and may only be used to connect directly to the social network from the app while in use.

**(vi)** Surreptitiously discovering passwords or private data = Developer Program removal.
**(vii)** `SFSafariViewController` must be visibly presented — never hidden or obscured — and may not be used to track users without knowledge and consent.
**(viii)** Compiling personal information from any source other than directly from the user, or without explicit consent — **even public databases** — is not permitted.
**(ix)** Apps in **highly regulated fields** (banking and financial services, healthcare, gambling, legal cannabis, air travel, crypto exchanges) or requiring sensitive user information must be submitted by the **legal entity providing the service**, not an individual developer. Legal cannabis sales must be **geo-restricted** to the legal jurisdiction.
**(x)** Basic contact info (name, email) may be requested only if **optional**, with no features or services conditional on providing it.

### 5.1.2 Data use and sharing
**(i)** No using, transmitting or sharing personal data without permission. Disclose how and where data is used. **Sharing with third parties — including third-party AI — must be clearly disclosed with explicit permission first.** App data may only be shared with third parties to improve the app or serve advertising. **Tracking requires explicit permission via App Tracking Transparency.** **The app may not require users to enable push notifications, location, or tracking to access functionality, content, or compensation of any kind (including gift cards and codes).**
**(ii)** Data collected for one purpose may not be repurposed without further consent.
**(iii)** No surreptitious user profiling; no attempting, facilitating or encouraging re-identification of anonymous users or reconstruction of profiles from Apple API data or data you called "anonymized"/"aggregated".
**(iv)** Never build a contact database from Contacts/Photos/other user-data APIs for your own use or for sale; never collect which other apps are installed for analytics or advertising.
**(v)** Don't contact people using data from a user's Contacts or Photos except at that user's explicit, individualized initiative. **No "Select All" and no pre-selecting all contacts.** Show the user exactly how the message will appear to the recipient and who it appears to be from.
**(vi)** Data from HomeKit, HealthKit, Clinical Health Records, MovementDisorder, ClassKit, or depth/facial-mapping tools (ARKit, Camera, Photo APIs) may **never** be used for marketing, advertising, or use-based data mining, including by third parties.
**(vii)** Apple Pay data may only be shared with third parties to facilitate or improve delivery of goods and services.

### 5.1.3 Health and health research
**(i)** Health/fitness/medical-research data (Clinical Health Records, HealthKit, Motion and Fitness, MovementDisorder, health-related human subject research) may **not** be used or disclosed for advertising, marketing or use-based data mining — only for improving health management, or for health research with permission. You may use health/fitness data to give a benefit directly to that user (e.g. a reduced insurance premium) if your app is submitted by the entity providing the benefit and the data isn't shared. **Disclose the specific health data you collect from the device.**
**(ii)** Never write false or inaccurate data into HealthKit or other medical/health apps. **Personal health information may not be stored in iCloud.**
**(iii)** Human subject research requires participant consent (parent/guardian for minors) covering: nature/purpose/duration; procedures, risks and benefits; confidentiality and data handling including third-party sharing; a point of contact; and the withdrawal process.
**(iv)** Human subject research requires **approval from an independent ethics review board**, provable on request.

### 5.1.4 Kids
**(a)** Comply with COPPA, GDPR, and any other applicable law. Birthdate and parental contact info may be requested **only** to comply with those statutes, and the app must offer useful functionality or entertainment value regardless of age. **Apps intended primarily for kids should not include third-party analytics or third-party advertising.**
**(b)** Narrow exceptions mirror Guideline 1.3. Apps in the Kids Category — or any app that collects, transmits, or *can* share personal information from a minor (name, address, email, location, photos, videos, drawings, chat capability, other personal data, or persistent identifiers combined with the above) — must include a privacy policy and comply with all children's privacy statutes. **A parental gate is not the same as parental consent for data collection.** Per 2.3.8, apps outside the Kids Category may not use terms in name, subtitle, icon, screenshots or description implying children are the main audience.

### 5.1.5 Location services
Use Location Services **only when directly relevant** to the app's features. Location APIs must not provide emergency services or autonomous control of vehicles, aircraft and other devices — except small devices such as lightweight drones, toys, or remote car-alarm systems. **Notify and obtain consent before collecting, transmitting or using location data**, and explain the purpose in the app.

## 5.2 Intellectual property

- **5.2.1** No protected third-party material (trademarks, copyrighted works, patented ideas) without permission; no misleading, false or copycat representations, names or metadata in the bundle or the developer name. Apps must be submitted by the person or legal entity that owns or licensed the rights.
- **5.2.2 Third-party sites/services** — using, accessing, monetizing access to, or displaying third-party content requires that service's terms to specifically permit it. **Authorization must be provided on request.**
- **5.2.3 Audio/video downloading** — no facilitating illegal file sharing; no saving, converting or downloading media from third-party sources (Apple Music, YouTube, SoundCloud, Vimeo) without explicit authorization. Streaming may also violate Terms of Use — check first.
- **5.2.4 Apple endorsements** — never suggest Apple is a source or supplier of the app, or endorses it. The "Editor's Choice" badge is applied by Apple automatically.
- **5.2.5 Apple products** — don't look confusingly similar to an Apple product, interface (Finder), app (App Store, iTunes Store, Messages) or advertising theme. **Apps, extensions, third-party keyboards and Sticker packs may not include Apple emoji.** iTunes/Apple Music previews may not be used for entertainment value (background music, game soundtracks); if you provide previews you must link to the corresponding music. Activity rings must not visualize Move/Exercise/Stand data in a way resembling the Activity control. Apple Weather data must follow WeatherKit attribution requirements.

## 5.3 Gaming, gambling and lotteries
- **5.3.1** Sweepstakes and contests must be **sponsored by the app's developer**.
- **5.3.2** Official rules must be presented in the app and state clearly that **Apple is not a sponsor or involved in any manner**.
- **5.3.3** **IAP may not buy credit or currency for real money gaming of any kind.**
- **5.3.4** Real money gaming (sports betting, poker, casino games, horse racing) and lotteries require licensing and permissions where used, must be **geo-restricted** to those locations, and must be **free on the App Store**. Illegal gambling aids, including card counters, are banned. Lottery apps need consideration, chance and a prize.

## 5.4 VPN apps
Must use the **NEVPNManager API** and may only be offered by developers enrolled as an **organization**. Declare clearly, **on an app screen before any purchase or use**, what user data is collected and how it's used. **VPN apps may not sell, use or disclose any data to third parties for any purpose**, and must commit to this in their privacy policy. Comply with local law; provide license information in App Review Notes where a VPN license is required. Parental control, content blocking and security apps from approved providers may also use NEVPNManager. Non-compliance = removal and possible Developer Program expulsion.

## 5.5 Mobile Device Management
MDM capability must be requested from Apple. Only commercial enterprises, educational institutions, government agencies, and in limited cases companies using MDM for parental control or device security. Declare data collection and use on an app screen before purchase or use. **No selling, using or disclosing any data to third parties**, committed to in the privacy policy. Limited third-party analytics only about your MDM app's performance — never about the user, their device, or other apps. Apps offering configuration profiles must meet the same requirements.

## 5.6 Developer Code of Conduct

Treat everyone with respect — in App Store review replies, support requests, and all communication with Apple including App Store Connect. No harassment, discrimination, intimidation or bullying. **Repeated manipulative or misleading behavior or fraudulent conduct ends your Developer Program account.**

> Apps should never prey on users or rip them off, trick them into unwanted purchases, force unnecessary data sharing, **raise prices in a tricky manner**, charge for undelivered features, or use any other manipulative practice, inside or outside the app.

Terminated accounts may be restored by submitting a written improvement plan that Apple approves and confirms as implemented.

- **5.6.1 App Store reviews** — respond respectfully, stay on topic, include no personal information, spam or marketing. **Use `SKStoreReviewController` / the official review API** — custom review prompts are disallowed.
- **5.6.2 Developer identity** — your representation of yourself, your business and your offerings must be truthful, relevant and up to date.
- **5.6.3 Discovery fraud** — manipulating charts, search, reviews or referrals is prohibited.
- **5.6.4 App quality** — excessive negative reviews and excessive refund requests are treated as signals that you may be violating the Code of Conduct.

---

## Audit checklist

- [ ] Privacy policy linked in App Store Connect **and** reachable in-app
- [ ] Policy covers collection, uses, third parties, retention/deletion, consent revocation
- [ ] Every purpose string is specific and honest
- [ ] Permissions requested are minimal; app degrades gracefully when denied
- [ ] **In-app account deletion exists** if account creation exists
- [ ] No functionality gated on notifications, location, or ATT consent
- [ ] ATT prompt implemented if any cross-app/site tracking occurs
- [ ] Privacy nutrition labels match actual code + SDK behavior
- [ ] Health data: not in iCloud, not used for advertising, specific disclosure
- [ ] Kids: no third-party ads/analytics, privacy policy, statute compliance
- [ ] All content is owned or licensed; third-party service ToS permit your use
- [ ] Regulated-field apps submitted by the licensed legal entity, geo-restricted where required
- [ ] Official review API used, never a custom rating prompt
