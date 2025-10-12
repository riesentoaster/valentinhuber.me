---
title: Drei-Schritte-Plan zur Sicherheit
hidden: true
---

> tl;dr: Benutze einen Passwortmanager auf einem aktuallisierten Gerät mit Backup.

> This post is also available [in English]({% post_url blog/cybersecurity/2023-10-02-Three Step Plan to Security %}).

Ich glaube, diese Regeln sollten von jeder Person befolgt werden und werden diese sicherer machen als die allermeisten anderen Internet-Benutzer. Die Liste ist nicht abschliessend und wenn du ein erhöhtes Risiko-Profil hast (z. B. wenn du Regierungschef, CEO oder CFO einer Firma, oder mit Dissidenten arbeitender Journalist bist) willst du vermutlich noch weitere Schritte machen. Das alles heisst weiter auch nicht, dass du völlig sicher bist und nicht mehr aufpassen musst.

## Updates
Das ist die einfachste Regel: Mach auf deinen Geräten alle verfügbaren Updates.

- Wenn dein Gerät keine Sicherheits-Updates mehr bekommt, solltest du das Gerät ersetzen.
- Solche Gerät können prinzipiell weiterbenutzt werden, solange sie *nie* (auch indirekt) mit dem Internet verbunden werden.
- Diese Regel gilt für alle mit dem Internet verbundenen Geräte, also auch Router, Drucker, Smart-Home-Geräte, etc.

Der Grund für diese Regel ist einfach: Wenn es für dein Gerät ein Update gibt, gibt es eine bekannte Schwachstelle und die Chance dass sie schon aktiv benutzt wird von bössartigen Gruppen. Attacken für viele Schwachstellen [starten schon bevor das Update verfügbar ist (en)](https://www.mandiant.com/resources/blog/time-to-exploit-trends-2021-2022), oder [werden innerhalb von wenigen Minuten nach dem Release der Updates erstellt (en)](https://resources.infosecinstitute.com/topics/vulnerabilities/time-to-patch-vulnerabilities-exploited-in-under-five-minutes/).

## Backups

Mach Backups von allen Daten, die du nicht verlieren möchtest. Backups beschützen dich vor zweierlei: Hacking und Benutzerfehler. Ersteres kommt zum Beispiel in Form von Ransomware vor, die all deine Daten verschlüsselt und Geld verlangt, sie wieder zu entschlüsselt, und zweiteres hat mich schon häufiger gerettet als ich zugeben möchte.

- Cloud-Dienste wie iCloud Drive, Dropbox oder Google Drive zählen nicht, weil sie dich von keinem der beiden Risiken beschützen. Sie sind vermutlich trotzdem eine gute Idee und helfen in gewissen Fällen.
- Ich empfehle eine Art von inkrementellem Backup: Diese speichern nicht nur eine Kopie aller deiner Dateien, sondern auch einzelne Bearbeitungs-Schritte. Das heisst, du kannst eine Datei, die du vor zwei Wochen gelöscht hast, wiederherstellen, oder ein Dokument auf eine alte Version zurücksetzen.
- Benutze die einfachste und am weitesten verbreitetsten Art von Backups auf deiner Platform, ausser du hast einen guten Grund: [iCloud Backup für iPhones und iPads](https://de.wikipedia.org/wiki/ICloud), [Time Machine für Macs](https://de.wikipedia.org/wiki/Time_Machine_(Apple)), etc.
- Ich empfehle mehr als ein Backup von deinen wichtigsten Daten zu haben, wie z. B. deiner Fotos. Ich empfehle weiter ein Backup zu haben, das physisch an einem anderen Ort liegt, also z. B. in der Cloud (nicht zu verwechseln mit oben genannten Sync-Diensten). Das beschützt gegen Einbrüche und Hausbrände.

## Passwörter
[Menschen sind im Allgemeinen sehr, sehr schlecht beim Passwörter erstellen (en)](https://www.pentestfactory.com/why-we-crack-80-of-your-employees-passwords/). Höchstwahrscheinlich bist du nicht viel besser als der Durchschnitt. Und das soll kein Vorwurf sein: Menschen sind grundsätzlich nicht gut darin, sich Informationen zu merken in einer Form, die nötig ist, um sichere Passwörter zu erstellen. Weiter brauchst du verschiedene Passwörter für alle deine Accounts (ich habe über 500 Passwörter in meinem Passwort-Manager), und dein Hirn skalliert nicht gut.

Darum empfehle ich, einen Passwort-Manager zu verwenden. Damit musst du dir nur zwei Passwörter merken: Eines, um deinen Computer zu entsperren und eines, um deinen Passwort-Manager zu entsperren. Diese beiden kannst du dann wirklich sicher gestalten und deinem Passwort-Manager alles andere überlassen. Dieser generiert Passwörter, die länger und komplizierter sind, als dass du sie dir merken könntest. Und weil Passwort-Manager Passwörter automatisch auf den Seiten ausfüllen, zu denen sie gehören, beschützen sie dich auch ein Stück weit gegen Phishing-Attacken. Also:

- Benutz einen Passwort-Manager! Such dir einen aus.
  - Schau mal, ob dein Geräte-Ökosystem einen bereitstellt, wie z. B. [Apple's iCloud Keychain](https://support.apple.com/de-de/109016).
  - Ich empfehle, einen etablierten Anbieter zu nehmen. Diese haben typischerweise mehr Resourcen, um deine Passwörter zu sichern und nicht der grösste Kunde zu sein ist im Fall der Fälle immer gut.
  - Unter Umständen kostet dein Passwort-Manager etwas. Bezahle das. Es lohnt sich.
- Benutze Zweifaktor-Authentifizierung wo möglich.
  - Das sollte verpflichtend sein für alle wichtigen Accounts wie fürs E-Banking und den Email-Account (wenn ich Zugriff dazu habe, kann ich vermutlich von allen anderen deiner Accounts das Passwort zurücksetzen).
  - Wenn möglich, [benutze nicht SMS als zweiten Faktor (en)](https://www.cnet.com/news/privacy/do-you-use-sms-for-two-factor-authentication-heres-why-you-shouldnt), sondern eine App.
  - Rotierende Passwörter direkt im Passwort-Manager zu verwalten macht das ganze etwas weniger sicher, aber deutlich angenehmer in der Benutzung, weil sie automatisch ausgefüllt werden. Wenn dir sonst der Aufwand für Zweifaktor-Authentifizierung zu gross ist, ist das immer noch deutlich besser als komplett ohne.
- Überlege dir, ob du dich nicht bei [haveibeenpwned](https://haveibeenpwned.com) anmelden möchtest. Es überprüft, ob deine Accounts in einer öffentlich verfügbaren Liste von Passwörtern auftaucht und schickt dir ein Mail, falls das je passiert – dann weisst du, dass du dein Passwort besser ändern solltest.

Sich gute Passwörter zu merken ist schwierig. Ich empfehle, dafür sogenannte Passphrases zu verwenden. [Dieser Comic (en)](https://xkcd.com/936/) erklärt das Konzept. Zusammenfassend: Nimm mindestens 4 Wörter, die nicht miteinander zu tun haben, und hänge sie einfach hintereinander. Wenn du eine Idee dafür brauchst, kann dir [diese Website](https://www.xkpasswd.net) Passphrases generieren.

## Bonus-Tipps
- Benutze einen Ad-Blocker! Das macht es deutlich angenehmer, das Internet zu benutzen, und verbessert Privatsphäre und Sicherheit. Wo verfügbar empfehle ich [uBlock Origin](https://ublockorigin.com): Es ist sowohl open-source (und damit gratis) und auch qualitätsmässig die beste Option, die mir bekannt ist.