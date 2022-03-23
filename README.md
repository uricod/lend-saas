[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://github.com/uricod/lend-saas/blob/master/LICENSE)

# Lend-SaaS
A LendingSaaS Python Client Library


For an overview of the LendSaaS API, [click here]( https://app.swaggerhub.com/apis/lendsaas/LendSaaSETL/1.0.0 ).


#### Requirements
- Python >= 3.6

#### Getting started
`pip install lend-saas`

`lend-saas` is very simple to use -- take a look at the below example:
```python
from lendSaaS import LendClient

ls = LendClient('api_key', 'client_name')

ls.leads.get_leads(limit='20', submittedMinDate='2021-10-11',  submittedMaxDate='2021-11-11')

```

**Available methods:**
#### Leads Object (ls.leads)
- `get_leads(submittedMinDate, submittedMaxDate, offset, limit=1000)` - Get a list of leads to dataframe
- `get_lead(lead_id)` -
Get info about specific lead. Use LeadId from get leads query.
- `get_lead_payment_promise(lead_id)` -
Get info about specific lead. Use LeadId from get leads query.
- `get_lead_external_data(lead_id)` -
Get info about specific lead. Use LeadId from get leads query.
Possible Values are in DocString
- `get_notes(lead_id, startDate, endDate, offset, limit=5000)` -
Get notes about leads. Use LeadId from get leads query.
- `get_ach_schedule(lead_id, startDate, endDate, offset, limit=5000)` -
Get info about ach payment schedule. Use LeadId from get leads query.
- `get_underwriting_info(lead_id, submittedMinDate, submittedMaxDate, offset, limit=5000)` -
Get info about underwriting info. Use LeadId from get leads query.

#### Funding Object (ls.funding)
- `get_account_monitoring(amStatusId, wlpId, includeClosedDeals)` - Get a dataframe of account monitoring. Args are required.
- `get_funding_stats(sdate, edate)` -
Get dataframe of funding stats based on date parameters

#### Underwriting Object (ls.Underwriting)
- `get_offers(leadId, offset, limit=1000)` - Get a list of offers given to dataframe
- `get_positions(leadId, offset, limit=1000)` - Get a list of positions to dataframe - offset and limit are required fields.
- `get_offer(offer_id)` - Get info on specific offer
- `get_stips(leadId, offset, limit=1000)` - Get a list of stips to dataframe
- `get_principals(leadId, offset, limit=1000)` - Get a list of principals to dataframe
- `get_banking_worksheet(leadId, offset, limit=1000)` - Get a list of banking worksheets to dataframe. Needs more work to flatten out actual worksheet column.
- `get_uw_status_history(leadId, offset, limit=1000)` - Get a list of uw status to dataframe
- `get_lead_isos(leadId, offset, limit=1000)` - Get a list of lead isos to dataframe
- `get_syndication_info(leadId, offset, limit=1000)` - Get a list of syndication info to dataframe
- `get_fees(leadId, offset, limit=1000)` - Get a list of fee info to dataframe
- `get_external_data(lead_id, offset, limit=100, source='experian', product=['Credit Profile', 'Bank Statements'])` -
Get info about specific lead. Use LeadId from get leads query.
Possible Values are in DocString

#### TO DO
Finish Tests



