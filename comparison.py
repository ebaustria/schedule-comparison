import sys
import csv

with open(sys.argv[1], 'r') as auto:
    with open(sys.argv[2], 'r') as manual:
        difference1 = set(auto).difference(manual)
        print("number of elements present in auto but not in manual:\n", len(difference1))
        print("elements present in automatically generated schedule but not in manual schedule:\n")
        for element in difference1:
            print(element)

with open(sys.argv[1], 'r') as auto:
    with open(sys.argv[2], 'r') as manual:
        difference2 = set(manual).difference(auto)
        print("number of elements present in manual but not in auto:\n", len(difference2))
        print("elements present in manual schedule but not in automatically generated schedule:\n")
        for element in difference2:
            print(element)

with open(sys.argv[1], 'r') as auto:
    len_auto = len(auto.readlines())
    print("size of automatically generated schedule:\n", len_auto)

with open(sys.argv[2], 'r') as manual:
    len_manual = len(manual.readlines())
    print("size of manually entered schedule:\n", len_manual)

with open(sys.argv[1], 'r') as auto:
    with open(sys.argv[2], 'r') as manual:
        csv_auto = csv.reader(auto, delimiter=',')
        csv_manual = csv.reader(manual, delimiter=',')
        print("mismatched rows:\n")
        list_auto = []
        list_manual = []
        for row_auto in csv_auto:
            list_auto.append(row_auto)
        for row_manual in csv_manual:
            list_manual.append(row_manual)
        comparison_list = list(zip(list_auto, list_manual))
        for (row_a, row_m) in comparison_list:
            if row_a != row_m:
                print(row_a)
