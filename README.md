<p align="center">
  <a href="https://defe-app.herokuapp.com"><img src="static/images/logodefe.svg" alt="defe logo" height="160"></a>
  <br>
  <p align="center">
    <b>A Tech feed Aggregator for Developers</b>
  </p>
  <p align="center">
     <i>Read Stories which matter</i>
  </p>
</p>

[![build](https://github.com/Bhupesh-V/defe/workflows/build/badge.svg?branch=master)](https://github.com/Bhupesh-V/defe/actions)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bhupesh-v/defe?logo=GitHub)](https://github.com/Bhupesh-V/defe/releases) 
 [![Website](https://img.shields.io/website?down_color=red&down_message=down&up_color=blueviolet&up_message=up&url=https%3A%2F%2Fdefe-app.herokuapp.com)](https://kutt.it/defe) 
 [![PyPI](https://img.shields.io/pypi/v/defe)](https://pypi.org/project/defe/)
[![GitHub](https://img.shields.io/github/license/Bhupesh-V/defe?color=purple)](https://github.com/Bhupesh-V/defe/blob/master/LICENSE)
[![PyPI Downloads](https://img.shields.io/pypi/dm/defe.svg?label=pypi%20downloads&logo=PyPI&logoColor=white)](https://pypi.org/project/defe/)
[![lgtm alerts](https://img.shields.io/lgtm/alerts/github/Bhupesh-V/defe.svg?logo=lgtm&logoWidth=18&color=red)](https://lgtm.com/projects/g/Bhupesh-V/defe/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/39926b7f89ab404d9d5a491fe2778db6)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bhupesh-V/defe&amp;utm_campaign=Badge_Grade)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Bhupesh-V/defe.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Bhupesh-V/defe/context:python)
[![Gitter](https://badges.gitter.im/devfeed/community.svg)](https://gitter.im/devfeed/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

  <p align="center">
    <sub>Built with ❤︎ by
      <a href="https://github.com/Bhupesh-V">Bhupesh Varshney</a><br>
	    <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/bhupeshimself?style=social"><br>
	    <sub align="center">The <a href="https://dev.to/bhupesh/defe-all-your-tech-updates-at-one-place-fih">story</a> behind defe</sub>
    </sub>
  </p>

## ✨ Features
- PWA
- Share Stories
- Minimal UI
- Command Line Interface
- Feeds from more than 100 sources categorized in
	- 📰 News
	- 🎙️ Podcasts 
	- 📧 Newsletters 
 ... _And Much More_

## :rainbow: Demo 
### CLI

<p align="center">
<img height="500px" src="https://drive.google.com/uc?export=view&id=110y95mO2kvV9tH0U1gCroj2XYVecGdzP">
</p>

### :package: Package
You can use the defe package to build bots :robot:
```python

from defe import defe
import pprint

f = defe.feed()

pprint.pprint(f.news(3))
pprint.pprint(f.feeders("newsletters"))

```

See [Dcoumetation](https://defe.readthedocs.io/en/latest/) for more.


## 🔮 Installation

Install **defe CLI** using `pip` from PyPI

```bash
pip install defe
```


## Development

1. Clone the repository
```bash
git clone https://github.com/Bhupesh-V/defe.git
```
2. Create virtual environment
```bash
python3 -m venv venv
```
3. Activate virtual environment

	**Linux/MacOS**
	```bash
	source venv/bin/activate
	```
	**Windows**
	```pwsh
	.\venv\Scripts\activate
	```
4. Install Dependencies
```bash
pip install -r requirements.txt
```
5. Lint the project with
```bash
black --check --diff .
```
6. Run the Development Server (for *WebApp*)
```bash
flask run
```
7. To Use the **defe CLI**, run
```bash
python -m defe
```


## 📝 Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for details.


## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## 📜 License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for details.

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.
