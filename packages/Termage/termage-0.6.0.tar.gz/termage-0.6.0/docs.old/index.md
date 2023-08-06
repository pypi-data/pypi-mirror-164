`Termage`, at the basic level, allows you to execute Python code and capture its result as an SVG file. It also offers a plugin, which can insert the SVG file into your `mkdocs` page!

!!! note
    `Termage` uses [PyTermGUI](https://github.com/bczsalba/pytermgui) to export screenshots. Thus, it has native support for capturing the result of `WindowManager`-based applications within the library.


```termage title=Hey\ there!
from pytermgui import tim, ColorPicker
from pytermgui.pretty import print

tim.print("Welcome to [!gradient(112) bold]Termage[/]!\n")
tim.print("Termage allows you to display [italic]any[/italic] terminal output in a terminal-mimicking [bold]SVG[/bold]!")

tim.print("\nHere are the current locals:")
print(locals())
```


## Installation

`Termage` is best installed using `pip`:

```
$ pip install termage
```

This will install PyTermGUI, as well as termage. The mkdocs plugin is included within the module as well.
