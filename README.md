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
#### Items Resource (monday.items)