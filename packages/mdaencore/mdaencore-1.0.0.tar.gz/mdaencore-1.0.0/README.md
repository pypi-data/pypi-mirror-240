mdaencore
==============================
[//]: # (Badges)

| **Latest release** | [![Last release tag][lastreleasetag]][githubreleases] ![GitHub commits since latest release (by date) for a branch][commitssincerelease]  [![Documentation Status][badge_docs]][docsurl] [![Anaconda-Server Badge][badge_condaforge]][conda_url]|
| :------            | :-------                                                                                                                                                                              |
| **Status**         | [![GH Actions Status][badge_actions]][mainworkflow] [![codecov][badge_codecov]][codecovio]                                                                                            |
| **Community**      | [![License: GPL v2][badge_license]][licenseinfo]    [![Powered by MDAnalysis][mdanalysis_badge]][mdaorg]                                                                              |

[badge_actions]: https://github.com/MDAnalysis/mdaencore/actions/workflows/gh-ci.yaml/badge.svg
[badge_codecov]: https://codecov.io/gh/MDAnalysis/mdaencore/branch/main/graph/badge.svg
[badge_license]: https://img.shields.io/badge/License-GPLv2-blue.svg
[badge_docs]: https://github.com/MDAnalysis/mdaencore/actions/workflows/docs.yaml/badge.svg?branch=main
[badge_condaforge]: https://anaconda.org/conda-forge/mdaencore/badges/version.svg
[conda_url]: https://anaconda.org/conda-forge/mdaencore

[codecovio]: https://codecov.io/gh/MDAnalysis/mdaencore/branch/main
[commitssincerelease]: https://img.shields.io/github/commits-since/MDAnalysis/mdaencore/latest
[githubreleases]: https://github.com/MDAnalysis/mdaencore/releases
[lastreleasetag]: https://img.shields.io/github/release-pre/MDAnalysis/mdaencore.svg
[licenseinfo]: https://www.gnu.org/licenses/gpl-2.0
[mainworkflow]: https://github.com/MDAnalysis/mdaencore/actions?query=branch%3Amain+workflow%3Agh-ci
[mdanalysis_badge]: https://img.shields.io/badge/powered%20by-MDAnalysis-orange.svg?logoWidth=16&logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIAAoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJD+XwCY/fEAkf3uAJf97wGT/a+HfHaoiIWE7n9/f+6Hh4fvgICAjwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACT/yYAlP//AJ///wCg//8JjvOchXly1oaGhv+Ghob/j4+P/39/f3IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJH8aQCY/8wAkv2kfY+elJ6al/yVlZX7iIiI8H9/f7h/f38UAAAAAAAAAAAAAAAAAAAAAAAAAAB/f38egYF/noqAebF8gYaagnx3oFpUUtZpaWr/WFhY8zo6OmT///8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgICAn46Ojv+Hh4b/jouJ/4iGhfcAAADnAAAA/wAAAP8AAADIAAAAAwCj/zIAnf2VAJD/PAAAAAAAAAAAAAAAAICAgNGHh4f/gICA/4SEhP+Xl5f/AwMD/wAAAP8AAAD/AAAA/wAAAB8Aov9/ALr//wCS/Z0AAAAAAAAAAAAAAACBgYGOjo6O/4mJif+Pj4//iYmJ/wAAAOAAAAD+AAAA/wAAAP8AAABhAP7+FgCi/38Axf4fAAAAAAAAAAAAAAAAiIiID4GBgYKCgoKogoB+fYSEgZhgYGDZXl5e/m9vb/9ISEjpEBAQxw8AAFQAAAAAAAAANQAAADcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjo6Mb5iYmP+cnJz/jY2N95CQkO4pKSn/AAAA7gAAAP0AAAD7AAAAhgAAAAEAAAAAAAAAAACL/gsAkv2uAJX/QQAAAAB9fX3egoKC/4CAgP+NjY3/c3Nz+wAAAP8AAAD/AAAA/wAAAPUAAAAcAAAAAAAAAAAAnP4NAJL9rgCR/0YAAAAAfX19w4ODg/98fHz/i4uL/4qKivwAAAD/AAAA/wAAAP8AAAD1AAAAGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALGxsVyqqqr/mpqa/6mpqf9KSUn/AAAA5QAAAPkAAAD5AAAAhQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADkUFBSuZ2dn/3V1df8uLi7bAAAATgBGfyQAAAA2AAAAMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0AAADoAAAA/wAAAP8AAAD/AAAAWgC3/2AAnv3eAJ/+dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9AAAA/wAAAP8AAAD/AAAA/wAKDzEAnP3WAKn//wCS/OgAf/8MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIQAAANwAAADtAAAA7QAAAMAAABUMAJn9gwCe/e0Aj/2LAP//AQAAAAAAAAAA
[mdaorg]: https://mdanalysis.org
[docsurl]: https://www.mdanalysis.org/mdaencore/

Ensemble overlap comparison software for molecular data.

mdaencore is bound by a [Code of Conduct](https://github.com/MDAnalysis/mdaencore/blob/main/CODE_OF_CONDUCT.md).

### Installation

To build mdaencore from source, we highly recommend using virtual environments.
If possible, we strongly recommend that you use [Anaconda](https://docs.conda.io/en/latest/) as your package manager.
Below we provide instructions both for `conda` and for `pip`.

#### With conda

Ensure that you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed.
Install in your preferred conda environment with
```
conda install -c conda-forge mdaencore
```

To update
```
conda update -c conda-forge mdaencore
```


#### With pip

To build the package from source, run:

```
pip install .
```

If you want to create a development environment, install the dependencies required for tests and docs with:

```
pip install -e ".[test,doc]"
```

### Copyright

The mdaencore source code is hosted at https://github.com/MDAnalysis/mdaencore
and is available under the GNU General Public License, version 2 or any later version (see the file [LICENSE](https://github.com/MDAnalysis/mdaencore/blob/main/LICENSE)).

Please note that the code is packaged and released under the terms of the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html)  or any later version.

Copyright (c) 2023, mdaencore authors (see the file [AUTHORS.md](https://github.com/MDAnalysis/mdaencore/blob/release_v1.0.0/AUTHORS.md))


#### Acknowledgements
 
Project based on the  [MDAnalysis Cookiecutter](https://github.com/MDAnalysis/cookiecutter-mda) version 0.1.
Please cite [MDAnalysis](https://github.com/MDAnalysis/mdanalysis#citation) and the [ENCORE paper](https://doi.org/10.1371/journal.pcbi.1004415) when using mdaencore in published work:

1. M. Tiberti, E. Papaleo, T. Bengtsen, W. Boomsma, and K. Lindorff-Larsen. ENCORE: Software for quantitative ensemble comparison. PLoS Comput Biol, 11 (2015), e1004415. doi: 10.1371/journal.pcbi.1004415
2. R. J. Gowers, M. Linke, J. Barnoud, T. J. E. Reddy, M. N. Melo, S. L. Seyler, D. L. Dotson, J. Domanski, S. Buchoux, I. M. Kenney, and O. Beckstein. MDAnalysis: A Python package for the rapid analysis of molecular dynamics simulations. In S. Benthall and S. Rostrup, editors, Proceedings of the 15th Python in Science Conference, pages 98-105, Austin, TX, 2016. SciPy. doi:10.25080/Majora-629e541a-00e


