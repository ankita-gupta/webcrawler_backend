#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A webcrawler.taskapp worker -l INFO
