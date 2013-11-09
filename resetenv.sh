#!/bin/zsh
psql -h localhost -U nerdfiles -d postgres << EOF
DROP DATABASE nerdfiles_net;
CREATE DATABASE nerdfiles_net;
EOF
# python manage.py syncdb
# python manage.py loaddata all_data.json
