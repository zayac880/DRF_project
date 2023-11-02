#!/bin/bash

celery -A config beat --loglevel=INFO
