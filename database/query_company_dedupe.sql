--Get distinct company names from registrations
with original_companies as (
    SELECT DISTINCT
        organization
    FROM
        conferences_events.exchange_registration
    ),
--Join to existing companies and only include them if they don't exist
new_companies as (
    SELECT
        original_companies.organization as original_organization,
        original_companies.organization as clean_organization,
        false as reviewed
    FROM
        original_companies
    LEFT JOIN
        conferences_events.exchange_organizations ON original_companies.organization = exchange_organizations.original_organization
    WHERE exchange_organizations.id IS NULL
)
--Insert new companies that are not already in the exchange_organizations table.
INSERT INTO conferences_events.exchange_organizations(original_organization, clean_organization, reviewed)
SELECT * FROM new_companies