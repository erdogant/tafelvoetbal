# tafelvoetbal

[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/tafelvoetbal/)
[![LOC](https://sloc.xyz/github/erdogant/tafelvoetbal/?category=code)](https://github.com/erdogant/tafelvoetbal/)
[![Downloads](https://static.pepy.tech/personalized-badge/tafelvoetbal?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/tafelvoetbal)
[![Downloads](https://static.pepy.tech/personalized-badge/tafelvoetbal?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/tafelvoetbal)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/tafelvoetbal/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/tafelvoetbal.svg)](https://github.com/erdogant/tafelvoetbal/network)
[![Issues](https://img.shields.io/github/issues/erdogant/tafelvoetbal.svg)](https://github.com/erdogant/tafelvoetbal/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![DOI](https://zenodo.org/badge/228166657.svg)](https://zenodo.org/badge/latestdoi/228166657)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://towardsdatascience.com/what-are-tafelvoetbal-loadings-and-biplots-9a7897f2e559)
![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/tafelvoetbal)
![GitHub repo size](https://img.shields.io/github/repo-size/erdogant/tafelvoetbal)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://erdogant.github.io/tafelvoetbal/pages/html/Documentation.html#)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->





<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``tafelvoetbal`` is Python package

# 
**Star this repo if you like it! ⭐️**
#


## Blog/Documentation

* [**tafelvoetbal documentation pages (Sphinx)**](https://erdogant.github.io/tafelvoetbal/)
* [**Read more details and usage about tafelvoetbal in this blog!**](https://towardsdatascience.com/tafelvoetbal)

* <a href="https://erdogant.github.io/tafelvoetbal/"> <img src="https://img.shields.io/badge/Sphinx-Docs-Green" alt="Open documentation pages"/> </a> tafelvoetbal documentation pages 
* <a href="https://towardsdatascience.com/a-step-by-step-guide-for-clustering-images-4b45f9906128"> <img src="https://img.shields.io/badge/Medium-Blog-blue" alt="Open Blog"/> </a> Blog: A step-by-step guide for clustering images 


### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install tafelvoetbal from PyPI (recommended). tafelvoetbal is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_tafelvoetbal python=3.8
conda activate env_tafelvoetbal
```

```bash
pip install tafelvoetbal            # normal install
pip install --upgrade tafelvoetbal # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/erdogant/tafelvoetbal.git@0.1.0#egg=master
pip install git+https://github.com/erdogant/tafelvoetbal#egg=master
pip install git+https://github.com/erdogant/tafelvoetbal

# By cloning
git clone https://github.com/erdogant/tafelvoetbal.git
cd tafelvoetbal
pip install -U .
```  

#### Import tafelvoetbal package
```python
import tafelvoetbal as tafelvoetbal
```

#### Example:
```python
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/tafelvoetbal/data/example_data.csv')
model = tafelvoetbal.fit(df)
G = tafelvoetbal.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/tafelvoetbal/blob/master/docs/figs/fig1.png" width="600" />
  
</p>


#### References
* https://github.com/erdogant/tafelvoetbal

#### Citation
Please cite in your publications if this is useful for your research (see citation).
   
### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
