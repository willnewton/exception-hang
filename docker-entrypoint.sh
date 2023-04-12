#!/bin/sh

set -e

. /venv/bin/activate

exec gunicorn -b 0.0.0.0:8080 \
     --worker-tmp-dir /dev/shm \
     --workers=4 \
     --worker-class=gthread \
     --threads=2 \
     --timeout 60 \
     'exception_hang:create_app()'
