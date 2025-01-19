---
title: Three Step Plan to Security
---

> tl;dr: Properly use a password manager on an up-to-date, backed-up device.

I believe these three rules should be followed by everyone and, if done properly, will make you more secure than most other internet users. This list is not exhaustive and if you have a higher risk profile (e.g. if you are a head of state, CEO or CFO of a company, or a journalist working with dissidents) you will want to do more. It also doesn't mean that you're fully secure and don't need to pay attention.

## Updates
This is the simplest rule: Keep your devices up to date.

- If your device no longer receives security updates, it's probably time to retire it and get a new one.
- It is fine to use devices that no longer receive security updates, as long as you are sure they will never connect to the internet (even indirectly).
- This rule also applies to any other internet-connected device you own (routers, printers, smart speakers, smart fridges or other appliances, etc.).

The reason for this is simple: if there is an update available for your device, there is a known vulnerability and chances are that it is already being actively exploited by certain actors. Attacks for many vulnerabilities start [before the update is even available](https://www.mandiant.com/resources/blog/time-to-exploit-trends-2021-2022) and some are [created within literal minutes of the release](https://resources.infosecinstitute.com/topics/vulnerabilities/time-to-patch-vulnerabilities-exploited-in-under-five-minutes/).

## Backups
Back up any data you don't want to lose. Backups protect you from two things: attacks and user error. The former can come in the form of ransomware that encrypts all your data and demands money to decrypt it, and the latter has saved me more times than I would like to admit.

- Cloud sync services such as iCloud Drive, Dropbox and Google Drive don't count because they don't protect you from either. They are probably still a good idea and will help in certain cases.
- I recommend some form of incremental backup: This will not only store a copy of all your files, but also the editing history. This means you can recover a file you deleted two weeks ago, or go back to an old version of a document.
- Use the simplest and most common form of backup for your platform, unless you have a good reason to use something else: [iCloud Backup for iPhones and iPads](https://en.wikipedia.org/wiki/ICloud#Backup_and_restore), [Time Machine for Macs](https://en.wikipedia.org/wiki/Time_Machine_(macOS)), etc.
- I recommend having more than one backup of your most important data, such as your pictures. I also recommend having a backup that is not physically in your house, but stores your data in the cloud, for example (not to be confused with sync services!). This will protect you against break-ins and house fires.

## Passwords
In general, [users are *terrible* at creating passwords](https://www.pentestfactory.com/why-we-crack-80-of-your-employees-passwords/). Chances are you're not much better than average. And I don't blame you: Humans are terrible at remembering data in the form required for passwords to be secure. Also, you need to have a different password for each account (I have well over 400 passwords in my password manager), and that just does not scale well.

This is why I recommend using a password manager. That way you only have to remember two passwords: one to unlock your computer and one to unlock your password manager. You can make these really strong and let the password manager handle the rest. Let it generate passwords that are much longer and more complex than you could ever remember. Because password managers only automatically fill in your passwords on the sites they belong to, this will also protect you a bit against fishing attacks. So:

- Use a password manager! Choose any you like.
  - Check if your device ecosystem has one built in, like [Apple's iCloud Keychain](https://en.wikipedia.org/wiki/ICloud#iCloud_Keychain).
  - I'd recommend going with a major player in the field. That way, they're likely to have more resources to keep your passwords secure, and if they do have a breach, you won't be the one with the biggest problem, which is a great place to be.
  - Your password manager may cost something. Pay it. It will be worth it.
- Use two-factor authentication where possible.
  - This is mandatory for all important accounts such as your bank and your email account (if I have access to that, I can probably reset the password on any of your other accounts and get access that way).
  - If at all possible, [don't use SMS as a second factor](https://www.cnet.com/news/privacy/do-you-use-sms-for-two-factor-authentication-heres-why-you-shouldnt) but instead a dedicated app. 
  - Adding the second factor like a one-time password (OTP) to your password manager makes it slightly less secure but much more convenient to use because it is automatically filled in like your password and saves you the hassle of taking out a second device, opening a special app and manually copying a code. It will still be much more secure than not having a second factor at all. Personally, I accept this trade-off.
- Consider signing up for [haveibeenpwned](https://haveibeenpwned.com). It will check if any of your accounts have ever been compromised, and you can set it to send you an email if this happens in the future.

To make sure your other passwords are secure, I would recommend using passphrases. This [comic](https://xkcd.com/936/) explains the concept. Make sure you use 4 random words that aren't related. If you need a way to generate such passphrases, use [this](https://xkpasswd.net/).

## Bonus Tips
- Use an ad blocker! They make the web a lot more pleasant and help with both privacy and security. Wherever available, I would recommend [uBlock Origin](https://ublockorigin.com), it's both open source (and therefore free) and simply the best I've come across so far.

## Changelog
- 2023-11-19: Added section about ad blockers
- 2025-01-19: Added note about not using SMS as a second factor