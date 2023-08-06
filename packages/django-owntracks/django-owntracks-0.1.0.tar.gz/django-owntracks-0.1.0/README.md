# django-owntracks

[![PyPI](https://img.shields.io/pypi/v/django-owntracks)](https://pypi.org/project/django-owntracks/)

**django-owntracks** add basic support for viewing [owntracks] data in the context of django application.

[owntracks]: https://owntracks.org/

# Usage

- Add `"owntracks"` and `"dmqtt"` to your `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    "owntracks",
    # Third Party
    "dmqtt",
    # Core Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- Add `MQTT_HOST`, `MQTT_USER`, `MQTT_PASS`, `MQTT_PORT`
