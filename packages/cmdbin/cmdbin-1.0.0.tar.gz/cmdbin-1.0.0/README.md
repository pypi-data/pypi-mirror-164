# cmdbin.py
cli and api for uploading pastes to https://cmdbin.cc (or another instance of your choosing)
```
usage: cmdbin [-h] [--input INPUT] [--passthrough] [--slugonly] [--raw] [--endpoint ENDPOINT]

cmdbin 1.0.0. - https://github.com/blucobalt/cmdbin.py

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        name of the file to upload, or "-" for stdin. defaults to stdin
  --passthrough, -p     passthrough lines from stdin to stdout
  --slugonly, -s        only return the slug, not the full link
  --raw, -r             return the link for the raw paste
  --endpoint ENDPOINT, -e ENDPOINT
                        specify a specific cmdbin endpoint. defaults to https://cmdbin.cc.
```