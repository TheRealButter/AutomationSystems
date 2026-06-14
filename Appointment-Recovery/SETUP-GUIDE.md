# Butter Code Appointment Recovery™ — Setup Guide (V2)
### Free-stack build: Google Calendar + Google Sheets + Gmail + Make.com

**Product**: Butter Code Appointment Recovery™
**Price**: R2,000–R3,500/month
**Promise**: Cut no-shows by 30–70%. Fill cancelled slots. Turn one-time clients into repeat clients.

---

## What's included

- **Scenario 1 — Booking Logger**: watches Google Calendar for new bookings. Instantly logs to sheet and sends a booking confirmation email to the client.
- **Scenario 2 — Reminder Sender**: runs every 30–60 minutes. Sends 4 reminder emails per appointment: 7-day, 48-hour, 24-hour, 2-hour. Marks past appointments COMPLETED.
- **Scenario 3 — Rebooking Engine**: runs daily. 6 weeks after a COMPLETED appointment, automatically prompts the client to rebook.
- **Scenario 4 — Win-Back Engine**: runs weekly. Sends a 60-day and 90-day re-engagement campaign to clients who haven't returned.
- **Appointments sheet template**: 14-column Google Sheet tracking each booking and all reminder flags.

---

## How bookings need to be created

This system works when Google Calendar events have a **guest with an email address** attached.

**Recommended (free)**: Google Calendar "Appointment Schedules" — the owner sets up bookable time slots, shares a booking link, and the client's email is automatically included when they book.

**Alternative**: owner manually creates the Calendar event and adds the client as a guest (30 seconds per booking).

---

## Setup steps

### 1. Create the Appointments Google Sheet
Create a new Google Sheet. Add a tab named **Appointments**. Paste the header row from `appointments-sheet-template.csv`:

```
Event ID, Client Name, Client Email, Appointment Time, Service, 7d Reminder Sent, 48h Reminder Sent, 24h Reminder Sent, 2h Reminder Sent, Confirmation Sent, Status, Rebooking Sent, Win-Back Sent, Notes
```

Get the Spreadsheet ID from the URL.

### 2. Import Scenario 1 (Booking Logger)
1. Import `scenario-1-appointment-logger.json` into Make
2. Replace `REPLACE_WITH_SPREADSHEET_ID`
3. Replace: `[ADDRESS OR MEETING LINK]`, `[PHONE NUMBER / WHATSAPP NUMBER]`, `[BUSINESS NAME]`
4. Connect the client's Google Calendar and Google Sheets accounts
5. Connect Gmail
6. Activate

### 3. Import Scenario 2 (Reminder Sender)
1. Import `scenario-2-reminder-sender.json`
2. Replace `REPLACE_WITH_SPREADSHEET_ID`, `[BUSINESS NAME]`, `[PHONE NUMBER / WHATSAPP NUMBER]`
3. Connect Google Sheets and Gmail
4. Set the schedule:
   - **Low volume** (few bookings/week): every 30 minutes
   - **High volume** (many bookings/day): every 60 minutes — all 4 reminder windows still fire reliably
5. Activate

### 4. Import Scenario 3 (Rebooking Engine)
1. Import `scenario-3-rebooking-engine.json`
2. Replace `REPLACE_WITH_SPREADSHEET_ID`, `[PHONE NUMBER / WHATSAPP NUMBER]`, `[BOOKING LINK]`, `[BUSINESS NAME]`
3. Set schedule to run **once daily**
4. Activate

### 5. Import Scenario 4 (Win-Back Engine)
1. Import `scenario-4-win-back-engine.json`
2. Replace `REPLACE_WITH_SPREADSHEET_ID`, `[PHONE NUMBER / WHATSAPP NUMBER]`, `[BOOKING LINK]`, `[OWNER NAME]`, `[BUSINESS NAME]`
3. Set schedule to run **weekly**
4. Activate

### 6. Test it
1. Create a test Calendar event ~25 hours from now with your own email as a guest
2. Run Scenario 1 manually — confirm: row appears in sheet, confirmation email arrives, all reminder flags = NO except Confirmation Sent = YES
3. Run Scenario 2 manually with hours_until in the 20–28h range — confirm 24h reminder email arrives and flag updates to YES
4. Set a test row to Status = COMPLETED, Appointment Time = 43 days ago, Rebooking Sent = NO — run Scenario 3 manually — confirm rebooking email arrives
5. Set a test row to Status = COMPLETED, Appointment Time = 62 days ago, Win-Back Sent = NO — run Scenario 4 manually — confirm win-back email arrives

---

## Reminder sequence summary

| Reminder | Window | Flag column |
|---|---|---|
| 7-day | 162–174 hours before | 7d Reminder Sent |
| 48-hour | 44–52 hours before | 48h Reminder Sent |
| 24-hour | 20–28 hours before | 24h Reminder Sent |
| 2-hour | 1.5–2.5 hours before | 2h Reminder Sent |

Wide timing windows ensure each reminder fires exactly once regardless of when the scenario runs within that window.

---

## Handover checklist (30-minute client walkthrough)

- [ ] Show the Google Calendar booking flow and how the appointment appears in the sheet
- [ ] Explain the 4-stage reminder sequence and that it runs automatically
- [ ] Show the Rebooking Engine — fires 6 weeks post-appointment, prompts repeat bookings without any owner action
- [ ] Show the Win-Back Engine — 60-day and 90-day campaigns to recover dormant clients
- [ ] Explain Status column: SCHEDULED → COMPLETED (auto) → LAPSED (after win-back sequence)
- [ ] Note ops budget: for high-volume businesses, switch Scenario 2 to hourly to stay within Make free tier

---

## KPI tracking (what to review monthly)

| Metric | How to measure |
|---|---|
| No-show rate | Count rows where Status never hit COMPLETED (manual check or count SCHEDULED rows past their appointment time) |
| Rebooking rate | Count rows where Rebooking Sent = YES vs. new bookings from those clients |
| Win-back rate | Count rows where Win-Back Sent = YES vs. new bookings from those clients |
| Repeat client rate | Count clients with more than 1 row in the Appointments sheet |

---

## Best-fit verticals

Salons & barbers · Hair and beauty · Physiotherapists & chiropractors · Psychologists & therapists · Dentists & medical practices · Personal trainers & fitness coaches · Tutors · Driving instructors · Photographers · Consultants

---

## Upsell path

- **Speed-To-Lead™** — for clients who advertise and get inbound enquiries: instant lead response, 30-day nurture, lost lead recovery. R2,500–R4,000/month.
- **Revenue Recovery™** — for clients who invoice clients (whether for appointments or services): pre-due reminders, 30-day escalation, promise-to-pay tracking. R1,500–R3,000/month.

Bundle all 3 for R6,000–R9,000/month: the complete Butter Code back office.
