# 2-7 Stripping Names

# Gonna do this in one print command (I think that's what the author wanted us to do).

name = "    edgar  "

print(f"Unstripped: '{name}',\nstripped r-side: '{name.rstrip()}',\nstripped l-side: '{name.lstrip()}',\nstripped on both sides: '{name.strip()}'.\nAll next to each other, separated by tabs: '{name}', \t'{name.rstrip()}', \t'{name.lstrip()}', \t'{name.strip()}'")