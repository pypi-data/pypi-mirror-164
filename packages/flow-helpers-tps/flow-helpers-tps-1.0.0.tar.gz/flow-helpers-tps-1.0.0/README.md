# flow-helpers

Handy helpers for ETLs and API interfacing.

## APIs & Transformations
* Bing Webmaster Tools
* Firebase
* Google Analytics (Universal Analytics)
* Google BigQuery
* Google Cloud Storage
* Google Drive
* Google Sheets
* Google SearchAds 360
* Impact
* Journera
* Listen360
* ScrapingHub
* Sharepoint

## Data Transfers
* SFTP
* AWS S3
* MSSQL
* Snowflake

## Other
* Time
* Files

## Internal Reference for test pypi
* create test account on test.pypi.org and get token
* using poetry, run `poetry config repositories.test-pypi https://test.pypi.org/legacy/`
* then add token using `poetry config pypi-token.test-pypi <token>`
* use `poetry version patch` to autoincrement new release
* use `poetry build` to build the whls
* use `poetry publish --build -r test-pypi` to build whls and publish to the test pypi repo

## Internal Reference for production pypi
* create account on pypi.org, get token
* using poetry, run `poetry config pypi-token.pypi <token>` to add token
* use `poetry publish --build` to build whls and publish to repo
* 