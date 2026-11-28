# 9 glass buttons (made with Claude)

Open `buttons.html`. Hover or press each button. One file, plain HTML and CSS, no JavaScript.

| # | name | try |
|---|---|---|
| 01 | Press to Glass | press and hold |
| 02 | Droplet | hover |
| 03 | Jelly | press |
| 04 | Neon Rim | hover |
| 05 | Frost | press and hold |
| 06 | Prism | press and hold |
| 07 | Liquid Fill | hover |
| 08 | Split | hover |
| 09 | Glass Orb | press |

- Copy a button: take the shared `.b` rules, its `.bN` rules, its `<button>` and the `<filter>` it points to.
- `--u` sets the size unit, `--p` drives the effect (0 to 1).
- The glass bend uses an SVG filter inside `backdrop-filter`: Chrome and Edge. Other browsers show see-through buttons.
- Each lens map is made for one size. Change a button's size and the map needs to be remade.
