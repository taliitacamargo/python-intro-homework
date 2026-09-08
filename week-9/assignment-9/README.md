# Assignment 9 — External Libraries & APIs

## Setup

```
pip install -r ../../requirements.txt
```

`warmup3.py` and `mini_project.py` call the REST Countries v5 API, which now
requires an API key (sign up for a free one at https://restcountries.com).
Set it as an environment variable before running either script:

```
export RESTCOUNTRIES_API_KEY="your-key-here"
python3 warmup3.py
python3 mini_project.py
```

## Files

- `warmup1.py` – first API request (agify.io)
- `warmup2.py` – accessing JSON fields with `.get()`
- `warmup3.py` – looping through a JSON list (REST Countries, Europe)
- `warmup4.py` – handling request errors
- `mini_project.py` – interactive Country Explorer CLI
