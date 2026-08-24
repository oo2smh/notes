# Container
- Anything that holds an inner child is considered a container.
- Can be broken down by levels.

1. Boilerplate: html, body
2. Main Landmark: main
3. Alt Landmarks: All other sectional tags (header, footer, nav, aside, section)
4. Component Membrane: Permeable containers for components (list, table, form, gallery, panel, iframe)
5. `Card`: self-contained, visually distinct container that groups related information or actions into a single unit.

# Padding
> Which containers should have padding applied?
1. `Membranes`:
  - No external padding. Relies on child (content) to provide the padding.
  - Provides inner structural rules for children. Layout rules (flex/grid/gap). Content-limiter (max-width).
  1. Main, aside, etc.
  2. Prebuilts+: list, form, table, gallery, panel, iframe
    - prebuilts are usually `permeable` or the same color as the parent.
    - If prebuilts are `delineated` (section is marked with bkg-filling or bordered), then padding should be added
2. `Standard`:
  - All other containment objects should be padded as normal.

> [!warning] If a membrane is the direct child in another membrane. The child membrane transforms into a standard containment. Padding should be provided!
> Example is a nav within the header! The nav will set the padding for the header. Since the nav transforms to as std container. The ul stays a membrane.

- You could add padding in a membrane-membrane parent-child element IFF you want extra padding. Apple relies on the height of its inner elements and does not add extra padding, making the header the size of the icon (44x44).

## *PADDING ARCHETYPES*
> Stick with 1 or 2 archetypes. Only use 3 for stylistic effects!
- 3 archetypes (sleek, std, airy)
  1. Sleek: Dense spacing. Picture-dominant or text-heavy sites. Apple. Adobe. Louis Vuitton. Josh Comeau.
  2. Std: Sketch. Tailwind. Mix of text and images.
  3. Airy: Greater spacing. Anti-pattern. Results in wasted space unless it's for a stylistic effect.

## *ADDITIVE PADDING*
- This refers to the padding relations between a parent and its child element.
  1. `Seamless`: Child element blends into the parent. Same background. No demarcation
  2. `Demarcated`: Child element's region is demarcated with a border and/or fill.

> When the padding is demarcated, you do need to add padding to the child-element. So that its kids can have breathing room. Especially in smaller screens, this eats away at precious real estate. You can set the padding to a small amount like 8px to account for this. The total viewport size however should be at least 16px!

# Page

# Padding Table

## *MOBILE/DESKTOP PADDING*
- apple has smaller padding in its header/footer. But those font sizes are also smaller (12)

| Item | Min | Std | Max | Notes |
|---|---|---|---|---|
| Viewport | 8 | 16 | 24 | comeau/sketch,apple/adobe |
| Header | 0 | 0 | 16 | typically 0, comeau exception on btn only header  |
| Footer Head | 10 | 32  | 48  |  adobe,sketch,tailwind |
| Footer Foot | 8  | 32  | 48  |  apple,adobe,sketch |
| Card (apple)| 12 | 24 | 72 | use clamp(16px, 5vw, 64px). Em. Size based on card sizes |
| Card (fixed)| 16 | 24 | 32/48 | used by most websites |
| Mobile Pg-Sections |  20 | 24/28/32 | 64 | (per section * 2) apple,comeau/sketch/adobe,design-pickle |
| Desktop Pg-Sections | 36 | 48 | 64 | (per section, total-gap should be doubled) sketch,material,apple |


# Gap
> Start thinking about adding gap starting from the page sections (hero, testimonial). Anything bigger than that, use padding!

- Gap shifts between inline 🛼 and block 🟫. 🛼 is usually smaller than 🟫. When the gap is `uniform` like in a card-gallery, the gap is small like `inline`.

## *MOBILE/DESKTOP GAP*

| Item | Min | Std | Max | Notes |
|---|---|---|---|---|
| Card 🛼/🟫 | 8/12 | 24 | 32 | apple/josh comeau, sketch, dribble/adobe|
| Desktop Demarcated Sections 🛼 | 60/64 | 80 | 128 | sketch,material,apple |


# My Starting Point
- aesthetics from design-pickle and apple

- 16, 24, 32, 48, 64, 80, 108

| Item | Value |
|---|---|
| Viewport inline-pad | 16 |
| Header inline | 0 |
| Floating Header inline | 16 |
| Footer block head:foot | 32:24 |
| Card pad sm:md:lg:xl | 16:24:48:64 |
| Pg section pad sm:md:lg:xl | 64:80:108:144 |
| eyebrow gap sm:md:lg | 04:08:12 |
| subtitle gap sm:md:lg | 04:08:12 |
| para-related  | 20:24:28 |
| text-unrelated  | 28:32:36 |
| btn/input field narrow in:block | 08,12:16 |
| li block sm:md:lg  | 12:16:24 |
| nav li inline sm:md:lg  | 12:16:20 |
| icon-text inline sm:md:lg  | 08:12:16 |
| h2-child dense sm:md:lg  | 08:12:16 |
| h2-child ui sm:md:lg  | 20:24 |


# Images and Their Sizes

| Item | Ratio | Dimen.. | Usage | Resol..  |
|---|---|---|---|---|
| Avatar xs | 1:1 | 36x36 | Inline, Dense UI, Youtube | 36, 72|
| Avatar sm | 1:1 | 64x64 | Heading Avatar | 64, 128 |
| Avatar md | 1:1 | 160x160 | Google contacts profile | 160, 320 |



# Card Aspect Ratios
- Cards typically contain cards. Longer than they are wider. Combo of pictures + text

- 1:1
