import os
import re
import spacy
import argparse
import time as timelib
import glob
from pathlib import Path
from redact_tools import redact_name, redact_date, redact_phone_number, redact_gender, redact_address, redact_email_address

def main():
    time0 = timelib.time()
    parser = argparse.ArgumentParser(description="Redact sensitive information from text files.")
    parser.add_argument('--input', required=True, help="Specify the input file(s) using a pattern, e.g. '*.txt'.")
    parser.add_argument('--names', action='store_true', help="Redact names.")
    parser.add_argument('--emails', action='store_true', help="Redact email addresses.")
    parser.add_argument('--dates', action='store_true', help="Redact dates.")
    parser.add_argument('--phones', action='store_true', help="Redact phone numbers.")
    parser.add_argument('--genders', action='store_true', help="Redact gendered terms.")
    parser.add_argument('--address', action='store_true', help="Redact addresses.")
    parser.add_argument('--output', required=True, help="Specify the output directory.")
    parser.add_argument('--stats', required=True, help="Specify the stats output file.")

    args = parser.parse_args()
    stats_list = []
    stats_list.append("******************************")
    stats_list.append("       Redaction Starts       ")
    stats_list.append("******************************")
    
    total_address_count = 0
    total_emails_count = 0
    total_dates_count = 0
    total_genders_count = 0
    total_names_count = 0 
    total_phone_count= 0

    input_files = glob.glob(args.input)

    for input_file in input_files:
        subtotal = 0
        stats_list.append("------------------------------")
        stats_list.append(f' File {os.path.splitext(os.path.basename(input_file))[0]}                    ')
        stats_list.append("------------------------------")
        stats_list.append(" Redacted Category | Count    ")
        stats_list.append("-------------------|----------")
        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read()
        redacted_text = input_text
        
        if args.address:
            redacted_text, stats, count = redact_address(redacted_text)
            stats_list.append(stats)
            total_address_count += count
            subtotal += count  
        
        if args.emails:
            redacted_text, stats, count = redact_email_address(redacted_text)
            stats_list.append(stats)
            total_emails_count += count
            subtotal += count

        if args.dates:
            redacted_text, stats, count = redact_date(redacted_text)
            stats_list.append(stats)
            total_dates_count += count
            subtotal += count
        
        if args.genders:
            redacted_text, stats, count = redact_gender(redacted_text)
            stats_list.append(stats)
            total_genders_count += count
            subtotal += count

        if args.names:
            redacted_text, stats, count = redact_name(redacted_text)
            stats_list.append(stats)
            total_names_count += count
            subtotal += count
        
        if args.phones:
            redacted_text, stats, count = redact_phone_number(redacted_text)
            stats_list.append(stats)
            total_phone_count += count
            subtotal += count
        
        file_name = os.path.splitext(os.path.basename(input_file))[0] + '.redacted'
        output_file_path = output_file_path = os.path.join(args.output, file_name)
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(redacted_text)
        stats_list.append("------------------------------")
        stats_list.append(f' Subtotal            {subtotal}')
        stats_list.append("------------------------------")
        stats_list.append('\n')

    time1 = timelib.time()
    stats_list.append("******************************")
    stats_list.append("      Redaction Summary       ")
    stats_list.append("******************************")
    stats_list.append("------------------------------")
    stats_list.append(" Redacted Category | Count    ")
    stats_list.append("------------------------------")
    stats_list.append(f" Address           | {total_address_count}")
    stats_list.append(f" Email             | {total_emails_count}")
    stats_list.append(f" Date              | {total_dates_count}")
    stats_list.append(f" Gender            | {total_genders_count}")
    stats_list.append(f" Name              | {total_names_count}")
    stats_list.append(f" Phone Number      | {total_phone_count}")
    total = total_address_count + total_emails_count + total_dates_count + total_genders_count + total_names_count + total_phone_count
    stats_list.append("------------------------------")
    stats_list.append(f' Total               {total}')
    stats_list.append("------------------------------")
    stats_list.append(f' Numbers of files:   {len(input_files)}')
    stats_list.append(" Complete time:      %.2fmin" % ((time1 - time0) / 60))
    stats_output = os.path.join(args.output, args.stats)
    with open(stats_output, 'w', encoding='utf-8') as f:
        for stats in stats_list:
            f.write(stats + "\n")
    
    print_summary = stats_list[-17:]
    print(*print_summary, sep='\n')

if __name__ == "__main__":
    main()