# Butter Code Revenue Recovery™ — Setup Guide (V2)
### Free-stack build: Google Sheets + Gmail + Make.com

**Product**: Butter Code Revenue Recovery™
**Price**: R1,500–R3,000/month (standalone) · R3,500–R5,000/month (bundled)
**Promise**: Get invoices paid faster. Chase every overdue invoice automatically. Never send an awkward payment reminder yourself again.

---

## What's included

- **Revenue Recovery Engine**: runs once daily. 6-stage automated reminder ladder from 3 days before due date through to escalation at 30 days overdue. Includes Promise-to-Pay tracking and multi-contact escalation.
- **Invoices sheet template**: 15-column Google Sheet the owner updates when sending a quote or invoice.

---

## Reminder ladder — 6 stages

| Stage | Trigger | Action |
|---|---|---|
| Pre-Due | 1–3 days before due date | Friendly heads-up with payment instructions |
| 1st Overdue | Day 3 overdue, count = 0 | Gentle reminder |
| 2nd Overdue | Day 7 overdue, count = 1 | Slightly firmer follow-up |
| Final Client | Day 14 overdue, count = 2 | Last message to client |
| Escalation | Day 30 overdue, count = 3 | Owner (+ Manager + Finance) alerted via email, auto-reminders stop |
| Promise Missed | Promised Pay Date passed, not paid | Automatic follow-up referencing the missed commitment |

---

## Setup steps

### 1. Create the Invoices Google Sheet
Create a new Google Sheet (or add a tab to an existing one). Name the tab **Invoices**. Paste the header row from `invoices-sheet-template.csv`:

```
Invoice ID, Client Name, Client Email, Description, Amount, Date Sent, Due Date, Promised Pay Date, Status, Last Reminder Sent, Reminder Count, Pre-Due Reminder Sent, Manager Email, Finance Email, Notes
```

Get the Spreadsheet ID from the URL.

### 2. Import the Make.com blueprint
1. Create a new scenario in Make → Import Blueprint → upload `revenue-recovery-engine.json`
2. Replace `REPLACE_WITH_SPREADSHEET_ID` with the Spreadsheet ID from step 1
3. Replace: `[OWNER NAME]`, `[BUSINESS NAME]`, `[OWNER EMAIL ADDRESS]`
4. Replace: `[BANK NAME]`, `[ACCOUNT NUMBER]` in each email template
5. Optionally replace `[PAYMENT LINK — Ozow / PayFast — optional]` with a real payment link if the client has one
6. Connect Google Sheets and Gmail (client's own free account)
7. Set the schedule to run **once daily** (e.g. 08:00, client's local timezone)
8. Activate

### 3. Daily workflow for the client
Every time the client sends an invoice or quote, they add **one row** to the Invoices sheet:

| Field | What to enter |
|---|---|
| Invoice ID | Their own invoice number (e.g. INV-2026-001) |
| Client Name | Customer's full name |
| Client Email | Customer's email address |
| Description | What the invoice is for |
| Amount | Amount in Rand (numbers only, e.g. 5000) |
| Date Sent | Today's date (YYYY-MM-DD) |
| Due Date | Payment due date (YYYY-MM-DD) |
| Promised Pay Date | Leave blank — fill in only if client commits to a specific date |
| Status | `SENT` |
| Reminder Count | `0` |
| Manager Email | Leave blank, or enter if escalation should CC a manager |
| Finance Email | Leave blank, or enter if escalation should CC a finance contact |

Leave Promised Pay Date, Pre-Due Reminder Sent, Last Reminder Sent, and Notes blank — the automation fills these in.

### 4. When a client pays
The owner manually changes **Status** to `PAID`. This immediately stops all further reminders for that row.

### 5. Using Promise-to-Pay
If a client calls or messages to say "I'll pay on Friday the 20th": the owner enters `2026-06-20` in the **Promised Pay Date** column. If that date passes without Status = PAID, the system automatically sends a follow-up referencing the missed promise.

### 6. Escalation contacts (optional)
If the business has a manager or finance contact who should be CC'd on 30-day escalation alerts, fill in `Manager Email` and/or `Finance Email` per row. Leave blank if not applicable — the system handles empty values cleanly.

### 7. Test it
1. Add a test row with Due Date set to 4 days ago, Status = SENT, Reminder Count = 0, your own email as Client Email
2. Run the scenario manually
3. Confirm: a "Friendly reminder" email arrives, Status updates to OVERDUE, Reminder Count updates to 1, a note is added
4. Add a test row with Due Date = tomorrow, Pre-Due Reminder Sent blank — run manually — confirm pre-due email arrives
5. Add a test row with Promised Pay Date = yesterday, Status = OVERDUE — run manually — confirm promise-missed follow-up fires

---

## Handover checklist (30-minute client walkthrough)

- [ ] Show the Invoices sheet and explain what each column does
- [ ] Walk through the 6-stage reminder ladder and what triggers each stage
- [ ] Explain the Status = PAID shortcut to stop all reminders instantly
- [ ] Show the Promise-to-Pay workflow — client commits to a date, owner logs it, system follows up if missed
- [ ] Explain escalation: who gets the 30-day alert, and how to set Manager/Finance Email columns
- [ ] Confirm owner knows to set Status = ESCALATED rows to PAID or a custom note after manual follow-up

---

## KPI tracking (what to review monthly)

| Metric | How to measure |
|---|---|
| Outstanding invoices | Count rows where Status ≠ PAID |
| Days to payment (DSO) | Average: Due Date − Date Sent for PAID rows |
| Collection rate | Count PAID / total invoices in the month |
| Escalations | Count ESCALATED rows — flag clients with recurring escalations for terms review |
| Promise-to-Pay success | Count rows where Promised Pay Date was set and Status = PAID vs. missed |

---

## Best-fit verticals

Accounting firms · Digital agencies · Freelancers & consultants · Construction & contractors · Trades (plumbers, electricians, solar) · Legal professionals · Bookkeepers · Logistics · Any B2B service business issuing invoices

---

## Upsell path

- **Speed-To-Lead™** — for clients who advertise and receive inbound enquiries: instant lead response, 30-day nurture, lost lead recovery. R2,500–R4,000/month.
- **Appointment Recovery™** — for clients who take bookings (salon owners, health practitioners, tutors): cuts no-shows, adds rebooking and win-back automation. R2,000–R3,500/month.

Bundle all 3 for R6,000–R9,000/month: the complete Butter Code back office.
