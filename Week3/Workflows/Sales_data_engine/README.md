# Sales Data Engine – CSV to Supabase

This n8n workflow automates the process of importing sales data from a CSV file in Google Drive, calculating VAT and total amounts, and storing the results in a Supabase database.

---

## Features

- **Daily Scheduled Import**: Automatically runs every day at 7 AM.
- **Fetch CSV from Google Drive**: Finds and downloads the latest sales CSV file.
- **Parse CSV**: Extracts structured sales data.
- **Calculate VAT & Total**: Adds VAT (14%) and computes total amounts for each invoice.
- **Insert into Supabase**: Saves processed invoices into the `sales_data` table for further analysis.

---

## Workflow Nodes

1. **Daily Schedule (7 AM)**
   - Node type: `Schedule Trigger`
   - Triggers the workflow daily at 7 AM.

2. **Find Sales CSV in Drive**
   - Node type: `Google Drive`
   - Searches for the `sales_data.csv` file in your Drive.

3. **Download Sales CSV**
   - Node type: `Google Drive`
   - Downloads the CSV file by file ID.

4. **Parse Sales Data**
   - Node type: `Extract From File`
   - Parses CSV contents into JSON items for further processing.

5. **Calculate VAT & Total**
   - Node type: `Code`
   - Calculates VAT (14%) and total amounts.
   - Formats date to ISO string (`YYYY-MM-DD`).

6. **Insert Invoice into Supabase**
   - Node type: `Supabase`
   - Inserts each invoice into the `sales_data` table.
   - Maps CSV columns to database fields:
     - `InvoiceID` → `invoice_id`
     - `Date` → `date`
     - `Amount` → `amount`
     - `VAT` → `vat`
     - `Total` → `total`

---

## Supabase Setup

1. Create a Supabase project.
2. Create a `sales_data` table with columns:

| Column      | Type       |
|------------|-----------|
| invoice_id  | text      |
| date        | date      |
| amount      | numeric   |
| vat         | numeric   |
| total       | numeric   |
| created_at  | timestamp (default now) |

3. Create n8n credentials for Supabase (`supabaseApi`) to authenticate inserts.

---

## Google Drive Setup

1. Create or locate a Google Drive account.
2. Save sales CSV files in a specific folder.
3. Configure n8n credentials (`googleDriveOAuth2Api`) for access.
4. Ensure the workflow searches for the correct CSV filename (`sales_data.csv`).

---

## How It Works

1. Workflow triggers daily at 7 AM.
2. Finds the sales CSV file in Google Drive.
3. Downloads the CSV file.
4. Parses CSV contents into structured JSON.
5. Calculates VAT and total for each invoice.
6. Inserts each processed invoice into Supabase for storage and analysis.

---

## Notes

- Make sure CSV columns match expected names (`InvoiceID`, `Date`, `Amount`).
- VAT rate can be adjusted in the **Calculate VAT & Total** node.
- This workflow can be extended to trigger alerts on missing files or failed inserts.
- Ensure n8n credentials are properly set for Google Drive and Supabase access.

---

## References

- [n8n Docs](https://docs.n8n.io/)
- [Supabase Docs](https://supabase.com/docs)
- [Google Drive API](https://developers.google.com/drive/api)
