-- get new company names and standardize them for Exchange 2023

with company_names as (
    select distinct "Company" as name
    from warehouse.pbi_registrations_all_events
    where "EventID" = '61725C13-6C78-41C9-A947-44BCE8ABE2CB'
    and "Status" <> 'Cancelled'
      and "Company" <> ''
)
INSERT INTO warehouse.cvent_organizations(original_name, standardized_name, needs_review)
select company_names.name, company_names.name, True from company_names
left join warehouse.cvent_organizations o on company_names.name = o.original_name
where o.id is null
RETURNING *;