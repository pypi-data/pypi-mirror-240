# jorm

This project aims to provide a standalone version of Django's ORM for use in offline projects, such as desktop applications. It allows you to leverage the power and convenience of Django's ORM without the need for the full Django web framework.

## Getting Started

### Prerequisites

- Python 3.12^ (it could work with lower versions but there is no warranty)
- (Optional) Virtual environment for isolation

### Installation

```bash
pip install jorm
```

Note: We recommend using [python poetry](https://python-poetry.org/)

### Contributing
Feel free to contribute by opening issues or pull requests. Make sure to follow good code of conduct (good manners, zero harrasing, zero bad words, respect others ideas, etc).

#### What I expect to accomplish? 
Just the following flow on desktop apps
1. `pip install djorm`
2. `djorm-admin startproject .` (this is open to discussion if is good idea to use template for just these or entire "recommended" app template)
This step creates the following files and directories `manage.py`, `db/settings.py`, `db/models.py`, `db/__init__.py`, `db/migrations/__init__.py`
(preserving as much functionality of manage.py as possible)
3. From anywhere on the app just `from db.models import ExampleModel` and working as if on django.

### License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
