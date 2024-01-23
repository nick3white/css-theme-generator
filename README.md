# CSS Theme Generator

Uses pywal to take a list of images (newline-separated list, either full paths or relative paths) and makes css files from them.  See the test files/examples in this repo.

Intended to be used with the theme-switching web component which is still broken and not published at this point, but whose functionality can be seen (functionally) at queercoding.org.

Note that the color values are provided as r, g, b values; this is so they can be used in either alpha or non-alpha contexts: `rgb(var(--color))` or `rgba(var(--color), 0.5);`

Also, no filename path is provided for the wallpaper variables; since there's no telling where you crazy kids will want your images, I didn't feel that was worth adding.

***Note:* this is here because github is where most things are.  Usually I use [source hut](https://sr.ht/), and [that version of the repo](https://git.sr.ht/~jeremyparker/css-theme-generator) might be more up to date, depending on how hectic my life is at any given moment.**

fwiw source hut is smol web so you should too 
