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
#### Leads Resource (ls.leads)
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



