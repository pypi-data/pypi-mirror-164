# PSU_EXPORT

Enables BI/Cognos data export for `psu_base`-enabled apps

## Installation/Configuration

Step 1: Add `psu-export` to requirements.txt

Step 2: Provide secrets in `local_settings.py`, and/or via `eb setenv`
* BI_EXPORT_ACCESS_KEY *- Get from another developer, or from BI team*
* BI_EXPORT_SECRET_KEY *- Get from another developer, or from BI team*

Step 3: Add `psu_export` and `psu_scheduler` to `INSTALLED_APPS` in `settings.py`
```buildoutcfg
INSTALLED_APPS = [
    ...
    'psu_base',
    'psu_export',
    'psu_scheduler',
]
```

Step 4: Add URLS for psu-export and psu-scheduler to urls.py
```
url('export/', include(('psu_export.urls', 'psu_export'), namespace='export')),
url('scheduler/', include(('psu_scheduler.urls', 'psu_scheduler'), namespace='scheduler')),
```

Step 5: Ensure `HOST_URL` is defined in your AWS settings (as required by psu_base). 
The `HOST_URL` setting can be overridden if needed by a setting named `SCHEDULER_URL`

## Define which models are exported
As a developer, select "Cognos Export Management" from the admin menu.
All installed apps are listed.  Select which apps should be exported.
Individual models and fields must also be selected to be included in the export.

There is also a button to manually run the export on the management page.

## Schedule the export
Define a new schedulable endpoint (admin menu) for "export:models" and then create a 
new scheduled jon (admin menu) for the day(s)/time(s) you want the data exported