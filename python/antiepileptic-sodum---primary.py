# Hayley C Gorton, Roger T Webb, Mathew J Carr, Marcos Delpozo-Banos, Ann John, Darren M Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"dnbn.","system":"readv2"},{"code":"dnbM.","system":"readv2"},{"code":"dnb7.","system":"readv2"},{"code":"dnbo.","system":"readv2"},{"code":"dnbv.","system":"readv2"},{"code":"dnbr.","system":"readv2"},{"code":"dnby.","system":"readv2"},{"code":"dnb8.","system":"readv2"},{"code":"dnbt.","system":"readv2"},{"code":"dnbL.","system":"readv2"},{"code":"dnbK.","system":"readv2"},{"code":"dnbJ.","system":"readv2"},{"code":"dnbs.","system":"readv2"},{"code":"dnbp.","system":"readv2"},{"code":"dnbq.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('antiepileptic-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["antiepileptic-sodum---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["antiepileptic-sodum---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["antiepileptic-sodum---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
