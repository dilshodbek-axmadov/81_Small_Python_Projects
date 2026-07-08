date_list = [['Sep 10', 'Jun 11', 'Sep 16', 'Dec 15', 'Dec 21', 'Oct 29', 'Nov 18', 'Apr 02', 'Jan 03', 'Aug 10', 'Jun 30', 'Feb 19', 'Mar 04', 'Nov 29', 'Jun 29', 'Jun 30', 'Feb 15', 'Jun 27', 'Jun 09', 'Dec 25', 'Sep 19', 'Jan 02', 'Oct 06'], ['Jun 27', 'Aug 02', 'Jan 19', 'Jul 09', 'Aug 05', 'Jan 17', 'Feb 26', 'Dec 08', 'Jan 30', 'Dec 02', 'May 10', 'Oct 13', 'Apr 19', 'Aug 22', 'Aug 14', 'May 23', 'Jan 11', 'Jul 02', 'Nov 10', 'Sep 08', 'Nov 15', 'Apr 25', 'Jul 13'], ['Jul 21', 'Jun 11', 'Nov 21', 'Mar 10', 'Oct 09', 'Feb 07', 'Feb 25', 'Aug 02', 'Oct 18', 'Aug 24', 'Jul 06', 'Aug 25', 'Sep 01', 'Nov 26', 'Apr 06', 'Nov 06', 'Apr 24', 'Dec 07', 'Jan 24', 'Jul 04', 'Jun 13', 'May 21', 'Mar 11']]

multiple_dates = {}
for index, list_ in enumerate(date_list):
    multiple_dates[index] = {}
    multiple_dates[index]["seen"] = set()
    multiple_dates[index]["duplicates"] = []
    for each_date in list_:
        if each_date not in multiple_dates[index]["seen"]:
            multiple_dates[index]["seen"].add(each_date)
        else:
            if each_date not in multiple_dates[index]["duplicates"]:
                multiple_dates[index]["duplicates"].append(each_date)

count = 0
for dict_ in multiple_dates:
    if multiple_dates[dict_]["duplicates"]:
        count += 1
