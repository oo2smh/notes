# tldr
- when designing a website, having a design system reduces decision fatigue
  1. Major Trio
    - Spacing
    - Typography
    - Color
  2. Effects (supplementary)
    - Icons
    - Transitions/Animations

- `Omni`: All possible value in the scale. =
- `Priority role`: A filtered set of tokens. Tokens are assigned a priority like `clr-primary, sz-section-lg`
- `Functional Roles`: From the tokens, we assign roles based on how it will be used `bg-color-dark`.

# *SPACING*
## *GENERAL RULES*
- Start with base value (16). Then adjust down if you want a leaner, more dense look, or up if you want a more spacious look. I prefer the denser look.
- Use padding for a container's external whitespace. Use gap with inner-middle spacing. Reach for margin only when needed. Margin collapse. etc. Margin-centering can be used, but try to use flex/grid to center.
- There are 2 ways to set spacing explicit, implicit.
  - Explicit is general
    - Dynamic (em): certain text-heavy websites use em to dynamically set the spacing between text elements. 1.95 BETWEEN (OUTER) H2 elements and 1.72 BETWEEN H3 elements. I find that this adds more complexity and generally will not reach for it unless the webpage is text heavy (news website)

  - Implicit (min(1200px, 90%), )
    - most webpage has 1-2 containers. The main container is between 980-1140px. The industry standard is 1140px, but apple uses 980px. For a single column layout, this makes sense as text should be 65-80 chars max! Some other websites break this to go for a more cinematic, BIG feeling (ie tailwind). This works if you are going to use a multi-column layout mainly within the main body of your webpage

## *SIZE (WIDTH/HEIGHT)*
- height/width are typically put on the html tag itself for media (img/icons). This is for ux issues
- icons are (16, 24, 32, 48)
- touch size should be (44x44 apple), (48x48 google). We'll go with the bigger number 48x48

## *ASIDE*
- spacing is used mainly for `padding` and `gaps`. Gaps refer to the space between 2+ elements and padding refers to a container's inner frame whitespace. Both use from the tokens which are all the possible values. Then priority-roles use the t-shirt scale to determine how it should be used.
- padding represents the whitespace for a CONTAINER. gap represents the spacing between the INNER ELEMS. Between the INNER ELEMS, there are cliques. We use the terms inner/outer to represent the type of gap. INNER is the gap between a related group (ie: the space between a H2 and a following paragraph). OUTER refers to the space between 2 different groups (ie: between 2 h2 groups). In general, there are 6 levels of gaps. Use base as the default for spacing between RELATED elems. Go md or higher between OUTER elems. Else you can use sm/xs for a denser look between RELATED elems


- Typically, padding is used for horizontal spacing. Gap is used for vertical spacing. Use padding when needed to create space. Also margin might be needed when you are designing a ui where the groups are different colors.

- gap-xl: 80+ (space between landmarks)
- gap-lg: 48px (1.95em --medium) (space between OUTER h1/h2, or major_components)
- gap-md: 24/32px (space between text and ui elements, text & btn ie)
- gap-base: 16px (default. space between INNER text H1/H2-paragraph, DEFAULT space between inner elements, go small for denser look)
- gap-sm: 8/12px (space between INNER text, denser look -- h1/h2, or used with h3 INNER)
- gap-xsm 4px (space between inline icons)

- To show 2 OUTER separation, there are 2 ways.
  1. Whitespace-only separator
  2. Line separation: using border or hr
  - Example among h2 using `whitespace-only separator`, the gap is usually `gap-lg` (48px). Using the `line-separator` method, it would be `gap-md` between the 2 things. Using the gap property does not work too well except with some hacks. The better alternative when a box is bounded by a line (either in 1+) direction, is to think of it as a container and use padding, either `padding-block` or the whole `padding` property.
    - There are certain situations where `padding-bleed` might occur. This refers to when the background color of a container and an inner container clashes. When this happens, the 1st/last elems might look like it has extra whitespace compared with the middle elements. This is common as many ui prefer a clean aestetic. During these times, put the hack as high up the DOM tree as possible. For instance, in a nav -> ul -> li. If the li has padding bleed with the nav, then put the negative margins or reduction in the nav. Alternative method is to create a class to apply the fix.

## *TOKENS*

## where to add spacing?
- With nested tags, spacing can compound and be additive. This can be a headache to find and add which elems are adding the spacing.
- Solution: Designate certain elements to be `expandables`. Expandables take on the width/height of their contents. No padding should be added here!
  - Landmarks are `expandables`. Do not add padding! Only set the content-wrapper (aka container) to set the content max-width. Use grid with 3 columns to achieve this!

- Components are reusable, self-contained content-filled objects. There are different levels of components. Bigger components are composed of smaller components.
  1. 🏛️ Organ system (pg sections): fixed page sections in main (hero, testimonial, etc)
  2. 👻 Transitories: (popups, toggleables: sidebar, mobile_menu) -- transitory structures made up of organs. Often simpler than fixed pg sections. Sometimes denser-spacing than organ-systems.
  3. 🫧 Membrane: (list, form, gallery, carousel, table, panel):
    - Delineated Organs: list, table, gallery, carousel: (4-16px)
    - Std: panel, form  (16-32px): Usually
  4. 🫀 Organ


## Permeable or Delineated
- 🫧 Permeable = Object is same bkg color as parent. No borders/bkg filling.
- 🔳 Delineated = A group is delineated/made explicitly visible by bordering/filling the bkg.

> Landmarks are always permeable! Membranes (list, form, gallery, carousel, table, panels ) are almost always permeable!

- No padding in permeables!
- Permeables are padding-less containers that sets inner rules/restrictions. Max-width container, layout rules: flex/grid.
- However, if you delineate the group for these containers, then you do need padding, to provide breathing room between the delineation and child elements.
- When creating a component, you should create both variants, permeable and delineated!


organs (sidebar, popups, menu-mobile,list, form, card-gallery, carousel, table, panel), tissue (card, list-item, form-field, table-row), cell (card_head, card_foot, form_field), atoms (button, icons, text, img).
  - Organ systems are a structural category. Other organs, tissue are expected to live in a organ system.
  - Spacing decreases as you go down the hierarchy

# Padding

| Buckets | Members|Range |
|---|---|---|
|Landmarks|main,header,footer,nav|❌ |
|Org System |pg sections|(36-64,64-96,96-128)|
|Organ|gallery,form,carousel,table,panel|(04-16,08-24) |




- Everything is a box in css. But the macro-containers (landmarks, page sections) are considered `zones`. You could use `gap` to add space between these, but prefer `padding` here! Why? It's because `zones` usually have separate bkg-colors and padding is used with bkg-colors.
  - Use padding to set spacing between zones!
  - Use gap to set spacing within a macro-component's peers!

### Zones
- Xl: Landmarks (header, footer, nav, main, aside, sidebar): Semantic. Set content-restriction container here using grid (980-1140px usually). Use padding for all landmarks except main. Padding-block for these elements differ.
  - Header (8-16), Footer ()
- Lg: Page sections in `main` (hero, features, testimonials, pricing)
  - Page sections are borderless. Mainly semantic/structural grouping. Use padding to add separation within `main`.
- Md: Macro-Components. 1st level organism that live within the page sections (card, panels, modals, Forms, Ul/Ol).
  - Components can be borderless, colored or framed. IF colored and/or framed, then reduce the pg-section's padding to reduce the visual spacing between sections.



- Sm: Component section (card_head, card_foot)
- Xs: Atomic: A grouping of 2atoms (icon and text, 2 texts, inline li)

- Both padding and gap add spacing between 2 or more elements. Padding makes sense to add expand away the border of a container (often used for background-color). Gap is used to push away siblings 🙆🏻‍♂️ (or related groupings) WITHIN a container by an equal amount. Uniform inner spacing. Often times 2 peers live within a container, but are isolated. These 2 groups are considered aliens 👽 (ie: header_logo, header_nav). Flexbox is often used here (space-between).

- Everything is a box in css. But the macro-containers (landmarks, page sections) are considered `zones`. You could use `gap` to add space between these, but prefer `padding` here! Why? It's because `zones` usually have separate bkg-colors and padding is used with bkg-colors.
  - Use padding to add the paint area. Use grid and divide into 3 columns on the landmark to set the inner-content region.

> [!warn] You can use max-width to set the inner-content region, but it will undo the bkg-paint. You can also create an extra div to undo this, but this adds further complexity. Using grid is the most elegant solution.



- `Padding`

- Gaps are divided into inline 🛼, block 🟫
- Gaps can be divided further into acquaintance 🐺, sibling 🙆🏻‍♂️, child 🧒🏻, outsider 👽

- XL landmarks, usually have no gap, but padding. Within the landmarks, content-wrapper containers are usually implemented.
- Page sections have lg-block gaps (📱36-64, 📑 64-96, 🖥️ 96-156): Easiest to set mobile/desktop and ignore tablet.
  - Tailwind (64, 96, 96/156), Hulu(64, 64),
  - Dense. Content/Img heavy might use smaller spacing to include more content (hulu).

| Level

### Gaps

-  =  inner_gap
  - ©️ Copyright: 8 (apple)
  - 🦐 Icon: 4, 8
  -

  - 📋 List item:


- 📤 = outer_gap

| Sym | Description | Values-Range | Responsive Range |
|---|---|---|---|
| ©️ | copyright |



| Name | Rem | Px | Usage |
|---|---|---|---|
| 1 | 0.25 | 4px | copyright, icon gap |
| 2 | 0.50 | 8px | dense text inner-group, copyright, icon gap |
| 3 | 0.75 | 12px | copyright, icon gap |
| 4 | 1.00 | 16px | base, default |
| 5 | 1.25 | 20px |   |
| 6 | 1.5 | 24px | OUT-Group gap 1 |
| 8 | 2.0 | 32px | OUT-Group gap 2 |
| 9 | 2.25 | 36px |    |
| 10 | 2.50 | 40px | copyright, icon gap |
| 12 | 3.00 | 48px | OUT-Group gap big  |
| 14 | 3.50 | 56px | copyright, icon gap |
| 16 | 4.00 | 64px | copyright, icon gap |
| 20 | 5.00 | 80px | landmark sectional division  |
| 24 | 6.00 | 96px | landmark gap huge |
| 28 | 7.00 | 112px | landmark gap |
| 32 | 8.00 | 128px | landmark huge |



## *PRIORITY ROLES*
```
# pr = priority
-- space-xxs: 4
-- space-xs: 8
-- space-sm: 12
-- space-base: 16
-- space-md: 24,28
-- space-lg: 32,48
-- space-xl: 64
-- space-xxl: 80, 96 128, 144

# Used in containers for max-width
--measure-max-md: 71.25rem; #1140px
--measure-mid-sm: 61.25rem; #980px
--measure-max-lg: 75rem; #1140px
--measure-max-xl: 85rem; #1140px
```

## *FUNCTIONAL ROLES*
```
--pad-viewport: 8, 16, 24
--pad-card: 16, 24, 32
--pad-button: 8, 12, 24
--pad-header: 8, 12, 16
--pad-footer: 8, 12, 16

# h1 is often used once for hero section. Will use the same spacing as h2.
--gap-landmarks-out: 80+, (64 or less for data-heavy sites)
--gap-section-out: --space-md

--gap-title-in: --space-xs
--gap-h-out: --space-lg,
--gap-h3-in: --space-xxs
--gap-h3-out: --space-md
```


# TYPOGRAPHY
> font is based off a geometric scale (not linear like space). The scale that is often used is the minor third (1.25). That is what the notes will be based off of.

## *PRIORITY ROLES*
```css
12/14, 16, 24, 32, 44/48, 64, 80+

--fs-sm: 12/14
--fs-base: 16/18
--fs-md: 20/24
--fs-lg: 32
--fs-xl: 44/48
--fs-2xl: 64
--fs-3xl: 80

--fw-bold: 700
--fw-black: 800/900

--lh-body: 1.4-1.6
--lh-heading: 1.2-1.3
--lh-display: 1.1-1.2 #optional

# OPTIONAL (letter spacing)
--ls-body: 0
--ls-heading: 0.5
--ls-display: 1px (#another option is to add a text svg which scales normally)

# LINE MEASURE

# optional
--ff-body: 'Inter', sans-serif;          /* main content */
--ff-heading: 'Inter', sans-serif;       /* standard headings */
--ff-display: 'Playfair Display', serif; /* H1 / hero headings */

```

## *FUNCTIONAL ROLES*
- h3 is harder to distinguish based on size alone. Consider styling it differently to make it stand out from the body. Weight, color, border, etc.
- I also personally like making h2 (italic, uppercase) for scanability
```
h1 hero/text pop: 64+
h1 standard/article-website: 44(medium) 48(standard)
sectional h2: 32 (affinity), 24 (text-heavy, medium)
h3: (medium), when using sections, u typically don't write h3
body: 16/18
ui elements: 12/14
```


# Color
## *TOKENS*
> Some brands have 2 primary colors. So they use both on different pages are within the same page. This adds visual interest, but it is harder to pull off. In that case you would name primary1/2, secondary1/2. You could also add additonal accent colors for visual interest.

- You will need 7 semantic tokens. Each will have its own scale. Colors might overlap. For instance, brand color is red. Then you would not need to create a separate red for status.
  1. Brand (Primary): Has the greatest pop
  2. Accent (Secondary): More subdued pop.
  3. Neutral (warm, cool, green, mystic(purple))
  4. Status (error, warning, success, info) [red, yellow/orange, green, blue]

- create your own scale or use tailwind color system


- text coloring
- background coloring
- icons coloring
- img matching (img should ideally be chosen to match or at least not conflit with other colors)

```
- body is


```
