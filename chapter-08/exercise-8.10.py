"""
8.10 Paint Fill

Implement the "paint fill" function that one might see on many image editing
programs. That is, given a screen (represented by a two-dimensional array of
colors), a point, and a new color, fill in the surrounding area until the
color changes from the original color.
"""

def paint_fill(screen, r, c, ncolor):
    if screen[r][c] == ncolor:
        return False
    return paint_fill_aux(screen, r, c, screen[r][c], ncolor)

def paint_fill_aux(screen, r, c, ocolor, ncolor):
    if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0]):
        return False

    if screen[r][c] == ocolor:
        screen[r][c] = ncolor
        paint_fill_aux(screen, r-1, c, ocolor, ncolor)
        paint_fill_aux(screen, r+1, c, ocolor, ncolor)
        paint_fill_aux(screen, r, c-1, ocolor, ncolor)
        paint_fill_aux(screen, r, c+1, ocolor, ncolor)

    return True
