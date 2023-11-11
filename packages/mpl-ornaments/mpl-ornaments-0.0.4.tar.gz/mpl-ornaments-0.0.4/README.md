# mpl-ornaments
A library featuring some extensions to [Matplotlib](https://matplotlib.org/). Full documentation available [here]( https://bianconif.github.io/mpl_ornaments/).

## The `titles` module
The title module allows to add title and subtitle to a Matplotlib's `Figure` in a and neat and easy way.

###  Example

```python
import matplotlib.pyplot as plt
from mpl_ornaments.titles import set_title_and_subtitle

fig, ax = plt.subplots(figsize=(5,6))
set_title_and_subtitle(fig=fig, title='Figure title', subtitle='Figure subtitle')
fig.savefig(fname='title1.png')
```

The above code produces the following result:

![title1](output/title1.png)
