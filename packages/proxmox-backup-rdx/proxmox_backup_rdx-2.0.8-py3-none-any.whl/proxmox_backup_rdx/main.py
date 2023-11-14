#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Main module of proxmox_backup_rdx
"""

import argparse
import logging

from proxmox_backup_rdx.models.datastore import Datastore
from proxmox_backup_rdx.models.prunejob import PruneJob
from proxmox_backup_rdx.models.syncjob import SyncJob

def script_argument():
    """
    Return arguments passed to the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0.8')
    parser.add_argument('-d', '--datastore', dest='datastore', type=str, required=True,
                        help='Define the name of the RDX tape datastore')
    parser.add_argument('-s', '--sync-job', dest='sync_job_id', type=str, required=True,
                        help='Define ID of the sync job to start')
    parser.add_argument('-p', '--prune-job', dest='prune_job_id', type=str, required=True,
                        help='Define ID of the prune job to start')
    parser.add_argument('-e', '--eject', dest='eject_period', type=str, default="never",
                        choices=["never", "daily", "weekly", "monthly"],
                        help='Define when the RDX tape need to be ejected ')
    parser.parse_args()
    return parser.parse_args()

def main():
    """_summary_
    """
    args = script_argument()
    datastore_name = args.datastore
    syncjob_id = args.sync_job_id
    prunejob_id = args.prune_job_id
    eject_period = args.eject_period

    # Récupère la liste des datastores disponibles et sélectionne
    # le datastore portant le même nom
    datastore = Datastore.get(datastore_name)

    # Active le datastore
    datastore.enable()

    # Lancement de la tâche de synchronisation
    syncjob = SyncJob.get(syncjob_id)
    syncjob.run()

    # Lancement de la tâche de pruning
    prunejob = PruneJob.get(prunejob_id)
    prunejob.run()

    # # Vérifie que la tâche de garbage sur le datastore
    datastore.garbage()

    # Désactive le datastore
    datastore.disable()

    # Ejection de la cassette
    datastore.eject(eject_period)

if __name__ == "__main__":
    main()
