# Appointment No-Show Reducer — Setup Guide
### Free-stack build: Google Calendar + Google Sheets + Gmail + Make.com (free tier)

> **v1.1 update**: replaced the fixed-index attendee lookup with logic that dynamically detects the guest vs. organizer, fixed appointment-time parsing for accurate reminder timing, fixed first-name extraction, and corrected the row-number reference field (`__IMTROWNUM__`).

This system automatically reminds clients about upcoming bookings 24 hours and 2 hours before their appointment — reducing no-shows and giving the owner advance warning if a slot needs to be confirmed or filled.

---

## What's included

- **Scenario 1 — Appointment Logger**: watches the owner's Google Calendar for new bookings (with a guest email attached) and logs them to an Appointments sheet.
- **Scenario 2 — Reminder Sender**: runs every 30 minutes (or hourly for lower-volume businesses). Sends a 24-hour reminder email and a 2-hour reminder email per appointment, and marks past appointments as completed.
- **Appointments sheet template**: tracks each booking and which reminders have been sent.

---

## Important: how bookings need to be made

This system relies on Google Calendar events having a **guest with an email address** attached (i.e. the calendar invite includes the client's email). The cleanest way to achieve this for free:

**Recommended: Google Calendar "Appointment Schedules"** (free, built into any personal Google account) — the owner sets up bookable time slots, shares a booking link, and when a client books, Google Calendar automatically creates an event with the client as a guest, including their email. This is the easiest path and requires no extra setup beyond sharing the booking link.

**Alternative**: if the business already takes bookings another way (phone, WhatsApp, in person), the owner can manually create the Calendar event and add the client as a guest (email required) — takes 30 seconds per booking.

---

## Setup steps

### 1. Create the Appointments Google Sheet
Create a new Google Sheet, add a tab named **Appointments**, and paste the header row from `appointments-sheet-template.csv`:

```
Event ID, Client Name, Client Email, Appointment Time, Service, 24h Reminder Sent, 2h Reminder Sent, Status, Notes
```

Get the Spreadsheet ID from the URL.

### 2. Import Scenario 1 (Appointment Logger)
1. Import `scenario-1-appointment-logger.json` into Make
2. Replace `REPLACE_WITH_SPREADSHEET_ID`
3. Connect Google Calendar and Google Sheets (client's own account)
4. Activate

### 3. Import Scenario 2 (Reminder Sender)
1. Import `scenario-2-reminder-sender.json` into Make
2. Replace `REPLACE_WITH_SPREADSHEET_ID`, `[BUSINESS NAME]`, `[PHONE NUMBER / WHATSAPP NUMBER]`
3. Connect Google Sheets and Gmail
4. After import, set the schedule:
   - **Low volume** (a handful of bookings/week): every 30 minutes
   - **Higher volume** (many bookings/day, to stay within the 1,000 ops/month free limit): hourly
5. Activate

### 4. Set up Google Calendar Appointment Schedules (recommended)
In Google Calendar: Create → Appointment schedule → set available time slots → share the booking page link with clients (add it to WhatsApp Business profile, Instagram bio, Google Business Profile, etc.)

### 5. Test it
1. Create a test Calendar event for ~25 hours from now, with your own email as a guest
2. Run Scenario 1 manually — confirm a row appears in the Appointments sheet
3. Run Scenario 2 manually — confirm the 24h reminder email arrives and the sheet updates to "24h Reminder Sent: YES"

---

## Selling this

R1,500–R2,500 one-time build. Best fit: salons, barbers, tutors, consultants, small clinics/therapists, photographers, driving instructors — anyone taking timed, one-on-one bookings.

**Pitch angle**: even recovering 2-3 no-show slots a month pays for the build many times over — international data shows missed appointments cost the average practice around $200 per slot, with 5-30% no-show rates being typical.

**Combine with #1 and #2**: all three systems share the same Make account + Google account + Gmail connection, so a client buying all three gets a genuinely integrated "back office" — lead capture, follow-up, invoicing, and bookings all running on infrastructure they already own for free.
