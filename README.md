# meetmax-integration

## Overview

The purpose of this integration is to sync registrations receieved in Formstack (and subsequently synced to the NASPO Data Warehouse) to MeetMax. A few notes on this:

 - Companies must be added before adding attendees attached to the company.
 - Company names should be standardized prior to loading to avoid duplicates.
 - We had issues setting the industry categories custom field and it required post processing by MeetMax by submitting a ticket. Ultimately we were sending pipe-separated data of these options.

There is a package called `meetmax` which has all the helpers for interacting with the API. There are a few files that invoke this to make changes:

 - `tests.py` - Tests API calls in the staging environement.
 - `sync.py` - Runs a sync of all unsynced registrations. This is determined by checking the `meetmax_id` in the data warehouse which gets updated when someone is synced to MeetMax.

This relies on some views and tables in the data warehouse to do some pre-processing. Those are included here in `database` for convenience and are located in the `conferences_events` schema in the warehouse.

 1. Exchange Registration - Table used to capture registrations from Formstack.
 2. Exchange Organizations - Table used for company name dedeuplication.
 3. Exchange Meetmax - View of pre-processed data for uploading to MeetMax via API 

This code was not deployed and `sync.py` was run locally on a periodic basis.

## API Documentation

There are two environments you can log into which have a corresponding API.

 https://meetmax.com - Production environment.
 https://staging.meetmax.com - Staging environment.

Meetmax API Documentation - https://www.meetmax.com/docs/service/

