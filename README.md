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

![GitHub release (latest by date)](https://img.shields.io/github/v/release/bhupesh-v/defe?logo=GitHub)
![PyPI](https://img.shields.io/pypi/v/defe)
![GitHubLicense](https://img.shields.io/github/license/bhupesh-v/defe)
![PyPI - Status](https://img.shields.io/pypi/status/defe)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/39926b7f89ab404d9d5a491fe2778db6)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bhupesh-V/defe&amp;utm_campaign=Badge_Grade)


## ✨ Features
- PWA
- Share Stories
- Minimal UI
- Command Line Interface
- Feeds from more than 100 sources categorized in
	- 📰 News
	- 🎙️ Podcasts 
	- 📧 Newsletters 
	- _... And Much More_

## 🔮 Installation

Install **defe CLI** using `pip` from PyPI

```bash
pip install defe
```


## Development

1. Clone the repository:
```bash
git clone https://github.com/Bhupesh-V/defe.git
```
2. Create virtual environment:
```bash
python3 -m venv venv
```
3. Activate virtual environment:

	**Linux/MacOS**
	```bash
	source venv/bin/activate
	```
	**Windows**
	```pwsh
	.\venv\Scripts\activate
	```
4. Install Dependencies.
```bash
pip install -r requirements.txt
```
5. Lint the project with
```bash
flake8 .
black --check --diff .
```
6. Run the Development Server (for *webapp*)
```bash
flask run
```
7. To Use **defe CLI**
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
