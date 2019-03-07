#!/usr/bin/python3

"""A tiny Python program to check that httpd is running.
Try running this program from the command line like this:
  python3 check_webserver.py
"""

import subprocess


def checkhttpd():
    try:
        cmd = 'ps -A | grep httpd'

        subprocess.run(cmd, check=True, shell=True)
        print("Web Server IS running")

    except subprocess.CalledProcessError:
        print("Starting the httpd service")
        try:
            start = """#!/bin/bash
              sudo yum install httpd -y
              sudo systemctl enable httpd
              sudo service httpd start"""

            subprocess.run(start, check=True, shell=True)
            print("The web server is now running")

        except subprocess.CalledProcessError:
            print("The web server did not start")


def main():
    checkhttpd()


if __name__ == '__main__':
    main()
