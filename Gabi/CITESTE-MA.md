# Site Loredana Crișan — Breath & Sound Healing
Predare către programator — notițe de la Ary / Oaza Advertising

## Ce este acest fișier

`index.html` este site-ul complet, într-un singur fișier HTML de sine stătător (self-contained):
toate imaginile sunt încorporate direct în fișier (base64), iar CSS și JavaScript sunt inline, în
același fișier. Nu există alte fișiere, foldere de assets, build tools, npm, React etc. — e HTML/CSS/JS
simplu, scris manual.

**De aceea fișierul e mare (~5 MB)** — e normal, din cauza imaginilor încorporate. Dacă vrei să optimizezi
pentru producție, poți extrage imaginile din base64 în fișiere separate (.jpg/.png) și le poți servi normal,
dar nu e obligatoriu să funcționeze.

## Cum se deschide / rulează

Cel mai simplu: deschizi `index.html` direct în orice browser (dublu-click).

Pentru dezvoltare recomand totuși un mic server local (ca să funcționeze corect orice fetch/scroll-anchor),
de exemplu:
```
npx serve .
```
sau
```
python3 -m http.server 8000
```
apoi deschizi `http://localhost:8000/index.html`.

## Dependențe externe

Singura dependență externă este Google Fonts (încărcat prin `<link>` în `<head>`):
- **Bodoni Moda** (titluri, elemente italice/editoriale)
- **Montserrat** (text curent)

Nu sunt alte scripturi externe, librării JS sau CDN-uri.

## Structura secțiunilor (în ordine, cu id-uri)

1. `#home` — hero
2. `#despre-mine` — Despre Loredana + certificări
3. `#misiunea` — Misiune & Viziune
4. `#beneficii` — Beneficii
5. `#servicii` — Servicii & Tarife (cu cele 3 carduri de preț)
6. `#programari` — Programări (vezi placeholder mai jos)
7. `#breath-house` — Breath House + galerie foto (filmstrip cu drag-scroll și lightbox)
8. `#contact` — Contact
9. `#faq` — Întrebări frecvente

Navigarea de sus (`nav.topnav`) are linkuri către aceste secțiuni prin ancore (`#servicii`, etc.).

## Lucruri PLACEHOLDER care trebuie completate înainte de lansare

Astea sunt marcate și vizual în site cu un chenar galben punctat ("placeholder-note"), dar le listez și aici:

1. **Linkurile social media** din header și footer (Instagram, WhatsApp, Telegram, Facebook, Google Business
   Profile) sunt toate `href="#"` — trebuie puse linkurile reale. Căutați `aria-label="Instagram"` etc. în
   fișier ca să le găsiți rapid (sunt 2 seturi — unul în header, unul în footer).
2. **Datele de contact** (număr WhatsApp, handle Instagram) din secțiunea `#contact` sunt placeholder.
3. **Butoanele de programare** (din `#programari` și din `#contact`) duc momentan tot către secțiunea de
   contact — urmează să fie conectate la un calendar real de rezervări (Calendly / Google Calendar sau
   echivalent).

## Note tehnice utile

- Paleta de culori e definită ca variabile CSS în `:root` (ex. `--ink`, `--body`) — ușor de găsit la
  începutul blocului `<style>`.
- Galeria foto (`#breath-house`) e un "filmstrip" orizontal cu scroll (drag-to-scroll cu mouse) + săgeți
  prev/next + lightbox la click pe imagine. JS-ul e la finalul fișierului, caută comentariul / clasa
  `.filmstrip` și `.gallery-arrow`.
- Site-ul e responsive (breakpoint principal pe mobil în jur de 680px — caută `@media` în `<style>`).

## Contact

Pentru context sau întrebări despre conținut, contactați-o pe Ary (Oaza Advertising).
