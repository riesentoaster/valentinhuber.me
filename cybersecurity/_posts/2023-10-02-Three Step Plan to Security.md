---
title: Three Step Plan to Security
---

> tl;dr: Properly use a password manager on an up to date, backed up device.

I believe that these three rules should be followed by anyone and, if done properly, will make you more secure than most other internet users. This list does is not extensive and if you have an increased risk profile (so e.g. if you are a head of state, CEO or CFO or a company, or journalist working with dissidents), you will want to do more. It also doesn't mean you are fully secure and don't have to pay attention anymore.

## Updates
This is the easiest rule: Keep your devices up to date.

- If your device doesn't receive security updates anymore, it's probably time to retire it and get a new one.
- It is fine to use devices that do not receive security updates anymore, as long as you are sure that it will never (even indirectly) connect to the internet.
- This rule also applies to any other internet-connected device you own (routers, printers, smart speakers, smart fridges or other appliances, etc.).

The reason to do this is easy: If there is an update provided for your device, there is a known security vulnerability out there, and chances are that it is already being actively exploited by certain actors. The attacks for many vulnerabilities start [before the update is even available](https://www.mandiant.com/resources/blog/time-to-exploit-trends-2021-2022) and some are [created within literal minutes after it is released](https://resources.infosecinstitute.com/topics/vulnerabilities/time-to-patch-vulnerabilities-exploited-in-under-five-minutes/).

## Backups
Make backups of all the data you don't want to lose. Backups protect you against two things: attacks and user error. The first can be in the form of ransomware that encrypts all your data and asks for money to decrypt it again, and the latter has saved me more often than I want to acknowledge.

- Cloud synchronization services such as iCloud Drive, Dropbox and Google Drive don't count because they don't protect you against either of the two. They are probably still a good idea and will help in certain cases.
- I recommend having some form of incremental backup: This will not only store a copy of all your files but also the edit history. This means that you can recover a file you deleted two weeks ago or go back to an old version of a document.
- I recommend using the easiest and most common form of backup for your platform unless you have good reason to use something else: [iCloud Backup for iPhones and iPads](https://en.wikipedia.org/wiki/ICloud#Backup_and_restore), [Time Machine for Macs](https://en.wikipedia.org/wiki/Time_Machine_(macOS)), etc.
- I recommend having more than one backup of your most important data like your pictures. I also recommend having a backup that is not physically in your house but stores your data e.g. in the cloud (don't confuse this with sync services!). This will protect you against break-ins and your house burning down.

## Passwords
Generally, [users are *terrible* at creating passwords](https://www.pentestfactory.com/why-we-crack-80-of-your-employees-passwords/). Chances are, you aren't much better than the average. And I don't blame you: Humans are terrible at remembering data in the form necessary for passwords to be secure. Further, you need to have a different password for each account (I have something over 400 passwords in my password manager) and this just does not scale well.

Because of this, I recommend using a password manager. This means that you will only have to remember two passwords: the one to unlock your computer and the one to unlock the password manager. You can make those really strong and let the password manager deal with the rest. Let it generate passwords that are far longer and more complex than you could ever remember. Because password managers only automatically fill your passwords on the websites they belong to, this will also somewhat protect you against fishing attacks. So:

- Use a password manager! Choose any that you like.
  - Check if your device ecosystem has one built in like [Apple's iCloud Keychain](https://en.wikipedia.org/wiki/ICloud#iCloud_Keychain).
  - I'd recommend going with a major player in the field. This way, they will probably have more resources to keep your passwords secure and if they do end up having a breach, you aren't the person that has the biggest problem, which is a great place to be in.
  - Your password manager may cost something. Pay it. It will be worth it.
- Use two factor authentication whenever possible.
  - In my opinion, this is mandatory for all important accounts such as banking and your email account (if I have access to that, I can most likely reset the password to any other account of yours and get access like that).
  - Adding the second factor like a one-time password (OTP) to your password manager makes it slightly less secure but much more convenient to use because it will be automatically filled in like your password and takes away the hassle of getting out a second device, opening a specific app, and manually copying a code. It will still be much more secure than not having a second factor at all. I personally take this tradeoff.
- Consider registering for [haveibeenpwned](https://haveibeenpwned.com). It will check if any of your accounts were previously breached and you can set it so that it will send you an email if it happens in the future.

To make sure that your remaining passwords are secure, I would recommend using passphrases. This [comic](https://xkcd.com/936/) explains the concept. Make sure you use 4 random words that aren't connected. If you need a way to generate such passphrases, use [this](https://xkpasswd.net/).