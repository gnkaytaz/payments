http://boto3.readthedocs.io/en/latest/guide/dynamodb.html

pip3 install --download vendor -r requirements.txt --no-binary :all:

Invoice example


To pay this invoice send 0.123 Bitcoins to 123kjljsdf9832

Send by: Regnet
Invoice create: 09/09/2009 09:36
Description:

Invoice data fields:

- id
- client_id
- created
- valid_till
- status (waiting_for_paiment, paid, unvalid)
- transaction_id (null by default)

Payments data fields:

- id
- invoice id
- transaction_id

Investors

- id
- contacts
-- chat_id
- refund_address
