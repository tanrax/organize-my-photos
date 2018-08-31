#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import os
import click
import time
import calendar
import shutil

EXTENSIONS = ('jpg', 'jpeg', 'gif')

@click.command()
@click.argument('path')
@click.option('--locale', default=False, help='Specifies the language of the months. Example: es_ES')
@click.option('--extension', default=False, help='change file extension for sorting.')
def organize_my_photos(path, locale, extension):
    """ Sort in folder all photos """
    # Set locale
    if locale:
        locale.setlocale(category=locale.LC_ALL, locale=locale)
    # Set extensions
    extensions = EXTENSIONS
    if extension:
        extensions = (extension,)
    # Get all photos
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(extensions):
                # Get path file
                origin = os.path.join(root, file)
                # Get date
                date_mod = time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(os.path.join(root, file))))
                date_list = date_mod.split('/')
                date_mod_day = date_list[0]
                date_mod_month = date_list[1]
                date_mod_year = date_list[2]
                # Make folder: format year/month day -> 2018/abr 23/photo.jpg
                dest_folder = os.path.join(date_mod_year, f'{calendar.month_name[int(date_mod_month)]} {date_mod_day}')
                dest = os.path.join(date_mod_year, f'{calendar.month_name[int(date_mod_month)]} {date_mod_day}', file)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                # Move photo
                shutil.move(origin, dest)

if __name__ == '__main__':
    organize_my_photos()
