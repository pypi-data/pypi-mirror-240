#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Utils module
"""

import datetime

def last_sunday_of_month(date):
    """Return the date of the last sunday of the month."""
    month = date.month
    year = date.year

    # Définit le numéro de mois suivant
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    # Récupère la date du premier jour du mois suivant
    date = datetime.datetime(year, month, 1)

    # Ajoute à la date le nombre de jour pour atteindre le premier dimanche du mois
    # suivant et soustrait une semaine pour obtenir le dernier dimanche du mois en cours
    date = date + datetime.timedelta(days=6-date.weekday()) - datetime.timedelta(days=7)

    return date
