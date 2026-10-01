import csv

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["msisdn","customermsisdn","firstname","lastname","promocode","discount","email"])

    base_msisdn = 579005910009
    base_customermsisdn = 578489322700
    base_firstname = "SAKTHI"
    base_lastname = "VEL"
    base_email_prefix = "success+"
    email_domain = "@simulator.amazonses.com"

    for i in range(10000):
        customermsisdn = f"+{base_customermsisdn + i}"
        msisdn = f"+{base_msisdn + i}"
        firstname = f"{base_firstname}{101+i}"
        lastname = f"{base_lastname}{201+i}"
        email = f"{base_email_prefix}{200001+i}{email_domain}"
        writer.writerow([msisdn, customermsisdn, firstname, lastname, "OFF50", "50%", email])

