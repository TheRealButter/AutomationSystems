# Invoice / Quote Follow-Up Reminder System — Setup Guide
### Free-stack build: Google Sheets + Gmail + Make.com (free tier)

> **v1.1 update**: fixed days-overdue calculation to correctly parse sheet date strings (using `parseDate`), fixed first-name extraction for single-word names, and corrected the row-number reference field (`__IMTROWNUM__`).

This system automatically chases overdue invoices and quotes with a polite, escalating reminder sequence — so the business owner never has to send an awkward "did you see my invoice?" message again.

---

## What's included

- **Invoice Follow-up Reminder Engine**: runs once a day. Checks the Invoices sheet for unpaid items past their due date, and sends:
  - **Day 3**: friendly first reminder
  - **Day 7**: second reminder, slightly firmer
  - **Day 14**: final reminder
  - **Day 30**: stops emailing the client and alerts the owner directly that this needs a personal follow-up
- **Invoices sheet template**: a single Google Sheet tab the owner updates manually when sending a quote/invoice.

---

## Setup steps

### 1. Create the Invoices Google Sheet
Create a new Google Sheet (or add a new tab to an existing one) named **Invoices**. Paste the header row from `invoices-sheet-template.csv`:

```
Invoice ID, Client Name, Client Email, Description, Amount, Date Sent, Due Date, Status, Last Reminder Sent, Reminder Count, Notes
```

Get the Spreadsheet ID from the URL (the long string between `/d/` and `/edit`).

### 2. Import the Make.com blueprint
1. Create a new scenario in Make → Import Blueprint → upload `invoice-followup-reminder-engine.json`
2. Replace `REPLACE_WITH_SPREADSHEET_ID` with the Spreadsheet ID from step 1
3. Replace placeholders: `[OWNER NAME]`, `[BUSINESS NAME]`, `[OWNER EMAIL ADDRESS]`
4. Connect Google Sheets and Gmail (client's own free account)
5. After import, set the scenario schedule to run **once daily** (e.g. 08:00, client's local timezone)
6. Activate the scenario

### 3. Daily workflow for the client
Every time the client sends a quote or invoice, they add **one row** to the Invoices sheet:

| Field | What to enter |
|---|---|
| Invoice ID | Their own invoice number |
| Client Name | Customer's full name |
| Client Email | Customer's email |
| Description | What the invoice is for |
| Amount | Amount in Rand (number only) |
| Date Sent | Today's date |
| Due Date | Payment due date |
| Status | `SENT` |
| Reminder Count | `0` |

That's it — the automation takes over from there.

### 4. When a client pays
The owner manually changes **Status** to `PAID`. This immediately stops all further reminders for that row.

### 5. Test it
1. Add a test row with **Due Date** set to 4+ days in the past, Status = `SENT`, Reminder Count = `0`, and your own email as Client Email
2. Run the scenario manually
3. Confirm: a "friendly reminder" email arrives, and the row updates to Status = `OVERDUE`, Reminder Count = `1`, with a note added

---

## Selling this

**Standalone**: R1,000–R2,000 one-time build, pitched to freelancers, consultants, small contractors, and agencies who invoice clients directly and currently chase payment manually or not at all.

**As an add-on** to the Instant Lead Response System: same Make account, same Gmail connection — just a second sheet tab and a second scenario. Bundle pricing: "Lead response + invoice follow-up: R3,500" vs. "lead response only: R2,500".

**Pitch angle**: "The system sends the awkward reminder, not you." Frame it as protecting the client relationship — automated reminders feel less personal/confrontational than the owner chasing directly, especially for the first two reminders.
