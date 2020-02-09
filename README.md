# devfeed

> A News feed Aggregator for Developers.

- Available Websites:
	1. Hacker News
	2. Dev.to
	3. Few Subreddits
	4. ProductHunt
	5. TechCrunch

## Development

##### Prerequisites
- Python 3.6+
- virtualenv

1. Create virtual environment.
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```
2. Clone the repository.
```bash
git https://github.com/Bhupesh-V/devfeed.git
```
3. Install Dependencies.
```bash
pip install -r requirements-dev.txt
```
4. Lint the project with
```bash
flake8 .
black --check --diff .
```
5. Run the Development Server
```bash
python3 feed.py
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