# meetmax-integration

## Overview

The purpose of this integration is to sync registrations receieved in Formstack (and subsequently synced to the NASPO
Data Warehouse) to MeetMax. A few notes on this:

- Companies must be added before adding attendees attached to the company.
- Company names should be standardized prior to loading to avoid duplicates. See the process sections below for more
  details.
- We had issues setting the industry categories custom field and it required post processing by MeetMax by submitting a
  ticket. Ultimately we were sending pipe-separated data of these options.

There is a package called `meetmax` which has all the helpers for interacting with the API. There are a few files that
invoke this to make changes:

- `tests.py` - Tests API calls and data models objects. These should point to test events.
- `sync.py` - Runs a sync of all unsynced registrations. This is determined by checking the `meetmax_id` in the data
  warehouse which gets updated when someone is synced to MeetMax. This also adds new companies prior to syncing
  registrations.

This relies on some views and tables in the data warehouse to do some pre-processing. Those are included here
in `database` for convenience and are located in the `conferences_events` schema in the warehouse.

1. Exchange Registration - Table used to capture registrations from Formstack.
2. Exchange Organizations - Table used for company name de-duplication.
3. Exchange Meetmax - View of pre-processed data for uploading to MeetMax via API
4. Company Dedupe - Query to insert new companies into the exchange organizations table where there names can be cleaned
   up.

This code was not deployed and `sync.py` was run locally on a periodic basis.

## Process

1. Make sure registrations are synced ino the exchange organizations table.
2. Run the query at `database/query_company_dedupe` to add new companies to the exchange organizations table.
3. Review the exchange organizations table where the `reviewed` column is false, providing a `clean_organization` name
   for each original name (these should be the same across variations of the same company)
4. As clean names are set mark the column `reviewed` to true.
5. Run `sync.py` to Add new companies and registrations to meetmax.
6. Review the logs and the exhcnage registrations table for any rows with an error in the `meetmax_status` column

## API Documentation

There are two environments you can log into which have a corresponding API.

https://meetmax.com - Production environment.
https://staging.meetmax.com - Staging environment.

Meetmax API Documentation - https://www.meetmax.com/docs/service/

