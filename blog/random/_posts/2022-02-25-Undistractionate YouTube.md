---
title: Undistractionate YouTube
---
One thing I've done in the past is use a combination of hacks to hide certain distractions in YouTube to prevent me from falling down rabbit holes. Requirements (this is personal and might be different for you!):

- Hide recommended videos next/under a playing video (don't hide comments!)
- Redirect home and discover tabs to subscription

This allows me to watch what I intend to watch (read: subscriptions), search for specific videos and watch videos I get a link for. Remember: I don't want to block YouTube, I want to block the parts of YouTube that cost me all my precious time.

## Working solution for iOS as of Feb 2022
*precursor: I don't use the iOS YouTube app to be able to use an AdBlocker. This only works when using Safari and the YouTube website.*

Using [HyperWeb](https://hyperweb.app), I use a custom AdBlock rule to hide recommendations, and some [custom JavaScript](https://gist.github.com/riesentoaster/235f84394f045a4229aa0725ad7ffc3d) to do the redirection. In the app, navigate to "Popular" > "Blocker" > "Local", and add [this link](https://raw.githubusercontent.com/hadig/Focus-for-Youtube/master/focus4yt.txt). Under "Popular" > "Custom Scripts" > "Local", add [this link](https://gist.githubusercontent.com/riesentoaster/235f84394f045a4229aa0725ad7ffc3d/raw/66ff4d95ed424b920fdc3f6e7621d0962553eb73/youtube-redirect.js).

There might also be other apps that allow you to do similar things, I know of several other AdBlockers that allow you to provide custom block lists.

This most definitely isn't the most efficient or best solution. But it works for me.

## Further Solutions
The custom AdBlock block list is taken from a [GitHub repository](https://github.com/hadig/Focus-for-Youtube) of a [Mac App Store App](https://apps.apple.com/us/app/focus-for-youtube/id1514703160?mt=12). I haven't tested this, but if you want to try it, feel free.

## Related
I've created a custom block list to deal with similar issues in Instagram and [written about it]({% post_url blog/random/2023-12-12-Undistractionate Instagram %}).