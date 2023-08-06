!!! info
    Termage requires the following markdown extensions:

    - attr-list
    - pymdown-superfences
    - pymdown-tabbed


```termage height=10 width=60
from pytermgui import highlight_python, tim

code = """
while True:
    if condition:
        print("Hello")
    else:
        print("Goodbye")

    input()

"""

tim.print(highlight_python(code))
```

## Setup

To use the plugin, you should first add it to your `mkdocs.yml` plugin list:

```yaml title="mkdocs.yml"
plugins:
    - termage
```

!!! warning
    Termage should be loaded before any other markdown pre-processor plugins, to avoid conflicts while formatting.

Additionally, you need to make sure some markdown extensions are enabled:

```yaml title="mkdocs.yml"
markdown_extensions:
  - attr_list
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
```
