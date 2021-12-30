create view exchange_meetmax(id, registration_id, submitted_at, first_name, last_name, company, title, email, phone, registration_type, attendee_role_id, group_name, receive_request, locale, profile, headshot, industries, other_industries, created_at, updated_at, meetmax_id, meetmax_status, rollover, meetings) as
	SELECT r.id,
    r.registration_id,
    r.submitted_at,
    initcap(r.first_name) AS first_name,
    initcap(r.last_name) AS last_name,
        CASE
            WHEN r.registration_type = 'State Member'::text THEN s.full_name
            WHEN r.registration_type = 'Supplier'::text THEN o.clean_organization
            WHEN r.registration_type = 'Supplier - Small Business'::text THEN o.clean_organization
            WHEN r.registration_type = 'NASPO & NASPO ValuePoint Staff'::text THEN o.clean_organization
            WHEN r.registration_type = 'Partner (Academic, Affiliate, Associate, Strategic)'::text THEN o.clean_organization
            ELSE r.organization
        END AS company,
    r.title,
    lower(r.email) AS email,
    r.phone,
    r.registration_type,
        CASE
            WHEN r.registration_type = 'State Member'::text THEN 'NASPO2_STATE_REP'::text
            WHEN r.registration_type = 'Supplier'::text THEN 'NASPO2_SUPPLIER_ATT'::text
            WHEN r.registration_type = 'Supplier - Small Business'::text THEN 'NASPO2_SUPPLIER_ATT'::text
            WHEN r.registration_type = 'NASPO & NASPO ValuePoint Staff'::text THEN 'NASPO2_NASPO_REP'::text
            ELSE 'NASPO2_OTHER_ATTENDEE'::text
        END AS attendee_role_id,
        CASE
            WHEN r.registration_type = 'Partner (Academic, Affiliate, Associate, Strategic)'::text THEN '1'::text
            WHEN r.registration_type = 'Life Member or Honorary Member'::text THEN '2'::text
            WHEN r.registration_type = 'Speaker or VIP'::text THEN '3'::text
            ELSE NULL::text
        END AS group_name,
        CASE
            WHEN r.one_one = 'Yes'::text THEN 'Y'::text
            ELSE 'N'::text
        END AS receive_request,
    replace(r.time_zone, ' Time'::text, ''::text) AS locale,
    r.profile,
    r.headshot,
    replace(regexp_replace(r.industries, '[\n\r]+'::text, '|'::text, 'g'::text), ','::text, ''::text) AS industries,
    r.other_industries,
    r.created_at,
    r.updated_at,
    r.meetmax_id,
    r.meetmax_status,
    r.rollover,
    r.meetings
   FROM conferences_events.exchange_registration r
     LEFT JOIN conferences_events.events e ON r.form_id = e.form_id
     LEFT JOIN conferences_events.states s ON COALESCE(r.state_organization, r.address_state) = s.name::text
     LEFT JOIN conferences_events.regions r2 ON s.region_id = r2.id
     LEFT JOIN conferences_events.exchange_organizations o ON r.organization = o.original_organization
  WHERE r.approval_status = 'Approved'::text AND r.registration_status = 'Active'::text;