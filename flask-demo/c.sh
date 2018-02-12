#!/bin/bash
curl  http://localhost:5000/user/12 -H "Accept: application/json" -X POST -d '{"name":"dengwei"}'
