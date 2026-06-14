#!/usr/bin/env python3
"""
Butter Code — Client Setup Script
==================================
1. Fill in client-config.json
2. Run: python3 setup.py
3. Import the configured .json files into Make.com

Google IDs — where to find them:
  Form ID:         https://docs.google.com/forms/d/{FORM_ID}/edit
  Spreadsheet ID:  https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit
"""

import json
import os
import sys

CONFIG_FILE = "client-config.json"

SCENARIO_FILES = {
    "leads": [
        "Speed-To-Lead/scenario-1-lead-capture.json",
        "Speed-To-Lead/scenario-2-follow-up-engine.json",
        "Speed-To-Lead/scenario-3-lost-lead-recovery.json",
    ],
    "appointments": [
        "Appointment-Recovery/scenario-1-appointment-logger.json",
        "Appointment-Recovery/scenario-2-reminder-sender.json",
        "Appointment-Recovery/scenario-3-rebooking-engine.json",
        "Appointment-Recovery/scenario-4-win-back-engine.json",
    ],
    "invoices": [
        "Revenue-Recovery/revenue-recovery-engine.json",
    ],
}

REQUIRED_FIELDS = [
    ("business_name",           "Business name"),
    ("owner_name",              "Owner's full name"),
    ("owner_email",             "Owner's email address"),
    ("phone_whatsapp",          "Phone / WhatsApp number"),
    ("bank_name",               "Bank name (for EFT instructions)"),
    ("account_number",          "Bank account number"),
    ("google_form_id",          "Google Form ID"),
    ("spreadsheet_id",          "Google Spreadsheet ID (or per-product IDs below)"),
]


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"ERROR: {CONFIG_FILE} not found in the current directory.")
        sys.exit(1)
    with open(CONFIG_FILE) as f:
        return json.load(f)


def get_sheet_id(config, product):
    specific = config.get(f"spreadsheet_id_{product}", "").strip()
    general = config.get("spreadsheet_id", "").strip()
    result = specific or general
    if not result:
        print(f"  WARNING: No spreadsheet ID found for '{product}'. Placeholder left in place.")
    return result


def check_required(config):
    missing = []
    for key, label in REQUIRED_FIELDS:
        if key == "spreadsheet_id":
            has_any = (
                config.get("spreadsheet_id", "").strip()
                or config.get("spreadsheet_id_leads", "").strip()
                or config.get("spreadsheet_id_appointments", "").strip()
                or config.get("spreadsheet_id_invoices", "").strip()
            )
            if not has_any:
                missing.append(label)
        elif not config.get(key, "").strip():
            missing.append(label)
    return missing


def apply_replacements(filepath, replacements):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements.items():
        if new:
            content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    config = load_config()

    missing = check_required(config)
    if missing:
        print("The following required fields are empty in client-config.json:\n")
        for m in missing:
            print(f"  • {m}")
        print("\nPlease fill them in and re-run this script.")
        sys.exit(1)

    biz   = config.get("business_name", "").strip()
    owner = config.get("owner_name", "").strip()
    email = config.get("owner_email", "").strip()
    phone = config.get("phone_whatsapp", "").strip()
    addr  = config.get("address_or_meeting_link", "").strip() or "[Address / Meeting Link]"
    book  = config.get("booking_link", "").strip() or "[Booking Link]"
    bank  = config.get("bank_name", "").strip()
    acct  = config.get("account_number", "").strip()
    pay   = config.get("payment_link", "").strip() or "EFT preferred — see details above"
    form  = config.get("google_form_id", "").strip()

    common_replacements = {
        "[Client]":                                   biz,
        "[BUSINESS NAME]":                            biz,
        "[OWNER NAME]":                               owner,
        "[OWNER EMAIL ADDRESS]":                      email,
        "[PHONE NUMBER / WHATSAPP NUMBER]":           phone,
        "[ADDRESS OR MEETING LINK]":                  addr,
        "[BOOKING LINK — optional]":                  book,
        "[BOOKING LINK]":                             book,
        "[BANK NAME]":                                bank,
        "[ACCOUNT NUMBER]":                           acct,
        "[PAYMENT LINK — Ozow / PayFast — optional]": pay,
        "[PAYMENT LINK — optional]":                  pay,
        "REPLACE_WITH_FORM_ID":                       form,
    }

    print(f"\nConfiguring scenarios for: {biz}\n")

    total = 0
    for product, files in SCENARIO_FILES.items():
        sheet_id = get_sheet_id(config, product)
        replacements = {**common_replacements, "REPLACE_WITH_SPREADSHEET_ID": sheet_id}
        for filepath in files:
            if not os.path.exists(filepath):
                print(f"  SKIP (file not found): {filepath}")
                continue
            apply_replacements(filepath, replacements)
            print(f"  ✓  {filepath}")
            total += 1

    print(f"\nDone — {total} scenario files configured.\n")
    print("Next steps:")
    print("  1. In Make.com: Create scenario → Import Blueprint → upload each .json file")
    print("  2. Connect the client's Google account when prompted")
    print("  3. Set the schedule for each scenario (see SETUP-GUIDE.md in each folder)")
    print("  4. Activate all scenarios")
    print()
    print("Speed-To-Lead:      3 scenarios  (Scenario 1 instant, Scenarios 2+3 scheduled)")
    print("Appointment Recovery: 4 scenarios  (Scenario 1 instant, Scenarios 2–4 scheduled)")
    print("Revenue Recovery:   1 scenario   (daily schedule)")


if __name__ == "__main__":
    main()
