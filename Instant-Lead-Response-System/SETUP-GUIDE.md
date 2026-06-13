# Instant Lead Response System — Setup Guide
### Free-stack build: Google Forms + Google Sheets + Gmail + Make.com (free tier)

> **v1.1 update**: fixed first-name extraction (now handles single-word names safely) and corrected the row-number reference field (`__IMTROWNUM__`) used by Update Row modules.

This system gives any small service business an instant auto-reply to new enquiries, an immediate owner alert, and an automated follow-up sequence for leads who go quiet — all running on the client's own free Google account and free Make.com account, at zero ongoing cost.

---

## What's included

- **Scenario 1 — Instant Lead Response**: triggers the moment someone submits the enquiry form. Logs the lead, sends them an instant "we got your message" email, flags hot leads by keyword, and alerts the owner immediately.
- **Scenario 2 — Follow-up Engine**: runs once a day. Automatically emails leads who haven't responded on Day 1, Day 3, and Day 7, then marks the lead closed if there's still no response.
- **Leads sheet template**: a single Google Sheet tab that acts as the lead database/CRM.

---

## Setup steps (do this once per client)

### 1. Create the Google Form
Create a new Google Form with these exact field names (must match exactly, including capitalisation):

- **Full Name** (short answer)
- **Email** (short answer, set validation to "Email")
- **Phone** (short answer)
- **Service Needed** (short answer or dropdown — list the client's services)
- **Message** (paragraph)

Get the Form ID from the URL (the long string between `/d/` and `/edit`).

### 2. Create the Leads Google Sheet
Create a new Google Sheet. Add a tab named **Leads**. Paste the header row from `leads-sheet-template.csv` into row 1:

```
Lead ID, Timestamp, Full Name, Email, Phone, Service Interest, Message, Lead Score, Hot Lead, Status, Last Contacted, Next Follow-up, Follow-up Count, Notes
```

Get the Spreadsheet ID from the URL (the long string between `/d/` and `/edit`).

### 3. Import the Make.com blueprints
In Make.com (client's own free account):

1. Create a new scenario → Import Blueprint → upload `scenario-1-instant-lead-response.json`
2. Replace `REPLACE_WITH_FORM_ID` with the Form ID from step 1
3. Replace `REPLACE_WITH_SPREADSHEET_ID` with the Spreadsheet ID from step 2
4. Replace placeholders: `[BUSINESS NAME]`, `[OWNER NAME]`, `[OWNER EMAIL ADDRESS]`, `[PHONE NUMBER / WHATSAPP NUMBER]`
5. Connect Google account (Forms, Sheets) and Gmail account — use the **client's own account**
6. Activate the scenario

Repeat for `scenario-2-follow-up-engine.json`:
1. Import, replace `REPLACE_WITH_SPREADSHEET_ID` and placeholders
2. After import, set the scenario's schedule to run **once daily** (e.g. 09:00, client's local timezone)
3. Activate the scenario

### 4. Customise the hot-lead keywords (optional)
Scenario 1's router checks the enquiry message for words like "urgent", "today", "asap", "price", "quote", "available", "book". Edit this list in the Make scenario to match the client's industry — e.g. a driving school might add "license", "test date"; a salon might add "appointment", "this week".

### 5. Test it
1. Submit a test entry through the Google Form using your own email address
2. Confirm: instant reply email arrives within seconds, owner alert email arrives, a new row appears in the Leads sheet
3. Manually set "Next Follow-up" on a test row to today's date and run Scenario 2 manually to confirm the Day 1 follow-up email sends and the row updates correctly

---

## Handover checklist (for the 30-minute client walkthrough)

- [ ] Show the client their Google Form and how to share/embed the link (Facebook page, website, WhatsApp Business catalogue link, etc.)
- [ ] Show the Leads sheet and explain each column, especially **Status** and **Hot Lead**
- [ ] Explain that closing a deal = manually set Status to "WON" in the sheet (stops follow-ups)
- [ ] Explain that the owner alert email is where they should act first — especially on Hot Leads
- [ ] Show where to edit the email templates inside Make if they want to tweak wording later
- [ ] Note: this all runs on the client's own free Google + Make accounts — no recurring fee to the builder

---

## Upsell path (Phase 2, sold separately later)

Once the client sees this working, the natural upsell is:
1. **WhatsApp integration** — once they set up a WhatsApp Business API connection (via a BSP like Wati/360dialog, paid by the client), the same Make scenarios can be extended to send WhatsApp messages instead of/alongside email.
2. **Invoice/quote follow-up module** — same Sheet+Make architecture, tracks outstanding quotes/invoices and sends payment reminder sequences.
3. **Appointment no-show reducer** — Google Calendar integration that sends 24h/2h booking reminders and flags unconfirmed slots.

Each of these reuses the same foundation, so they're faster (and cheaper) to add than the initial build.
